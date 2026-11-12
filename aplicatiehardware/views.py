from django.http import HttpResponse
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Componenta
from django.shortcuts import render

def get_ip(request):
    req_headers = request.META
    str_lista_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if str_lista_ip:
        return str_lista_ip.split(',')[-1].strip()
    else:
        return request.META.get('REMOTE_ADDR')

class Accesare:
    contor = 1 
    
    def __init__(self, ip_client, url_cerere, parametri={}):
        self.id = Accesare.contor
        Accesare.contor += 1
        self.ip_client = ip_client
        self.url_cerere = url_cerere
        self.parametri = parametri
        self.data_cerere = datetime.now()

    def lista_parametri(self):
        lista = []
        for cheie, valoare in self.parametri.items():
            if valoare == "":
                lista.append((cheie, None))
            else:
                lista.append((cheie, valoare))
        return lista

    def url(self):
        return self.url_cerere
        
    def pagina(self):
        cale_curata = self.url_cerere.split('?')[0]
        return cale_curata.replace('/aplicatiehardware', '')

    def data(self, tip_afisare=None):
        if tip_afisare == "zi":
            format_ales = "%A, %d %B %Y"
        elif tip_afisare == "timp":
            format_ales = "%H:%M"
        else:
            format_ales = "%A, %d %B %Y - Ora: %H:%M"
        text = self.data_cerere.strftime(format_ales)
        zile_en = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        zile_ro = ["Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica"]
        for i in range(7): text = text.replace(zile_en[i], zile_ro[i])
        luni_en = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        luni_ro = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie", "Octombrie", "Noiembrie", "Decembrie"]
        for i in range(12): text = text.replace(luni_en[i], luni_ro[i])
        return f"<h2>Data si ora</h2>\n<p>{text}</p>"

    def __str__(self):
        return (f"id: {self.id}\n"
                f"ip_client: {self.ip_client}\n"
                f"url: {self.url()}\n"
                f"pagina: {self.pagina()}\n"
                f"data: {self.data()}\n"
                f"lista_parametri: {self.lista_parametri()}\n"
                f"-------------------------")

istoric_accesari = []

def inregistreaza_vizita(request):
    a = Accesare(ip_client=get_ip(request), url_cerere=request.get_full_path(), parametri=dict(request.GET.items()))
    istoric_accesari.append(a)

def index(request):
    inregistreaza_vizita(request)
    return HttpResponse("Pagina principala: Magazin de hardware si IoT.")

def info(request):
    inregistreaza_vizita(request)
    
    tip = request.GET.get('data')
    
    vizita_curenta = istoric_accesari[-1]
    
    html = "<h1>Informații despre server</h1>"
    html += "<p>Informatii despre server si componente.</p>"
    
    # traduce data în română
    html += vizita_curenta.data(tip_afisare=tip)
    
    return HttpResponse(html)

def despre(request):
    inregistreaza_vizita(request)
    return HttpResponse("Suntem un magazin infiintat in 2026, pasionati de roboti.")

def istoric(request):
    inregistreaza_vizita(request)
    return HttpResponse("Aici va aparea un istoric al magazinului in viitor.")

def produse(request):
    nrPagina = request.GET.get("pagina")
    
    produse = Componenta.objects.all() 
    
    paginator = Paginator(produse, 5) 
    mesajEroare = None
    
    try:
        obPagina = paginator.page(nrPagina)
    except PageNotAnInteger:
        obPagina = paginator.page(1)
    except EmptyPage:
        obPagina = None
        mesajEroare = "Nu mai sunt produse"
        
    return render(request, 'produse.html',
                    {
                        'pagina': obPagina,
                        'eroare': mesajEroare
                    }
    )

def contact(request):
    inregistreaza_vizita(request)
    return HttpResponse("Pagina de contact este in lucru.")

# Rutare cu Regex din curs (re_path)
def afisare_accesare(request, id):
    inregistreaza_vizita(request)
    for acc in istoric_accesari:
        if acc.id == int(id):
            return HttpResponse(f"<h1>Detalii accesare {id}</h1><pre>{acc}</pre>")
    return HttpResponse("Accesarea nu a fost gasita.")

def pagina_log(request):
    inregistreaza_vizita(request)
    html = "<h1>Log Accesari</h1>"
    
    # Parametri primiti
    html += f"<h2>Parametri primiti ({len(request.GET)}):</h2><ul>"
    for p in request.GET.keys(): html += f"<li>{p}</li>"
    html += "</ul>"
    
    # Accesari in sesiune curenta
    if request.GET.get('accesari') == 'nr':
        html += f"<p>Numar accesari sesiune: {len(istoric_accesari)}</p>"
        
    lista_afisare = istoric_accesari.copy()
    
    ultimele = request.GET.get('ultimele')
    if ultimele:
        if ultimele.isdigit():
            n = int(ultimele)
            if n > len(istoric_accesari):
                html += f"<p style='color:red;'>Exista doar {len(istoric_accesari)} accesari fata de {n} accesari cerute</p>"
            else:
                lista_afisare = istoric_accesari[-n:]
        else:
            html += "<p style='color:red;'>Eroare: 'ultimele' trebuie sa fie numar.</p>"

    iduri = request.GET.getlist('iduri')
    if iduri:
        dubluri = request.GET.get('dubluri', 'false').lower() == 'true'
        iduri_cerute = []
        for string_iduri in iduri:
            iduri_cerute.extend(string_iduri.split(','))
            
        lista_afisare = []
        iduri_vazute = set()
        for i_str in iduri_cerute:
            if i_str.isdigit():
                val = int(i_str)
                if not dubluri and val in iduri_vazute:
                    continue
                for acc in istoric_accesari:
                    if acc.id == val:
                        lista_afisare.append(acc)
                        iduri_vazute.add(val)
                        break

    val_accesari = request.GET.get('accesari')
    val_tabel = request.GET.get('tabel')
    
    if val_accesari == 'detalii':
        html += "<ul>"
        for a in lista_afisare: html += f"<li>{a.data_cerere.strftime('%d-%m-%Y %H:%M:%S')}</li>"
        html += "</ul>"
        
    if val_tabel:
        coloane = ['id', 'ip_client', 'url', 'data'] if val_tabel == 'tot' else val_tabel.split(',')
        html += "<table border='1'><tr>"
        for c in coloane: html += f"<th>{c}</th>"
        html += "</tr>"
        for a in lista_afisare:
            html += "<tr>"
            for c in coloane:
                if c == 'id': html += f"<td>{a.id}</td>"
                elif c == 'url': html += f"<td>{a.url()}</td>"
                else: html += f"<td>-</td>" 
            html += "</tr>"
        html += "</table>"
    if not val_accesari and not val_tabel:
        html += "<h3>Vizite filtrate:</h3><ul>"
        for a in lista_afisare:
            html += f"<li>ID: {a.id} | Pagina: {a.pagina()} | IP: {a.ip_client}</li>"
        html += "</ul>"
        
    # Statistica cea mai vizitata / putin vizitata
    frecvente = {}
    for a in istoric_accesari:
        pag = a.pagina()
        frecvente[pag] = frecvente.get(pag, 0) + 1
        
    if frecvente:
        max_pag = max(frecvente, key=frecvente.get)
        min_pag = min(frecvente, key=frecvente.get)
        html += f"<hr><p>Cea mai accesata: {max_pag} ({frecvente[max_pag]} vizite)</p>"
        html += f"<p>Cea mai putin accesata: {min_pag} ({frecvente[min_pag]} vizite)</p>"

    return HttpResponse(html)
