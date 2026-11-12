@ECHO OFF
IF EXIST fisier.sql DEL fisier.sql
SET PGPASSWORD=maxim
ECHO Realizam procesarea tabelelor...
(FOR %%t IN ("aplicatiehardware_componenta" "aplicatiehardware_categorie" "aplicatiehardware_brand" "aplicatiehardware_furnizor" "aplicatiehardware_specificatietehnica") DO (
    ECHO Tabelul %%t
    "C:\Program Files\PostgreSQL\18\bin\pg_dump.exe" --column-inserts --data-only --inserts -h localhost -U maxim -p 5432 --schema django -d django_hardware -t %%t >> fisier.sql
))
SET PGPASSWORD=
ECHO Backup complet! Fisierul fisier.sql a fost creat.