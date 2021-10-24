#!/bin/bash
Import Emails.txt
echo -e "Analisis de correos electronicos\n"
echo -e "---Iniciando Programa---\n"

sleep 2

#solicitud de datos

echo -e "Necesitaremos pedirte algunes dates para poder avanzar con el proceso de verificacion...\n"
sleep 1
read -sp "Escribe to API Key:" API
echo ""

while IFS= read -r line
do echo "$Email"
done < Emails.txt

#Comprobacion
  function check {
    curl -s "https://haveibeenpwned.com/api/v3/breachedaccount/$Email" -H 'hibp-api-key:'$API
    echo $sitio
    echo -e "Estamos terminando los ultimos detalles..\n"
    sleep 2
}
check