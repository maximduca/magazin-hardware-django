class MiddlewareNou:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        str_lista_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if str_lista_ip:
            ip_client = str_lista_ip.split(',')[-1].strip()
        else:
            ip_client = request.META.get('REMOTE_ADDR')
        
        request.ip_utilizator = ip_client
        
        response = self.get_response(request)
        return response