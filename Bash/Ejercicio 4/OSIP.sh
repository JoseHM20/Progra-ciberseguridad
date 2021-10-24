echo "Iniciando programa..."
echo "Analizando sistema operativo, por favor espere..." 

#Detectar sistema operativo

#! /bin/bash

if type -t wevtutil &> /dev/null
then
OS=MSWin
elif type -t scutil &> /dev/null
then
OS=macOS
else
OS=Linux
fi

echo "Tu sistema operativo es:"$OS

#Busqueda de IPs

echo "Iniciando programa de busqueda de IPs..."
echo "Las IPs detectadas son: "

#!/bin/bash
function is_alive_ping() {
         ping -c 1 $1 > /dev/null 2>&1
         [ $? -eq 0 ] | echo "Node with IP: $i is up."
}
for i in 192.168.1.{1..20}
do
           is_alive_ping $i
done

#Borrar despues esto de abajo 

#Parámetros

host=$1
firstport=$2
lastport=$3

#Funcion para escanear puertos

function Start-portscan {
  for ((counter=$firstport; counter<=$lastport; counter++))

  do while{
    (echo >/dev/tcp/$host/$counter) > /dev/null 2>&1 && echo "$counter open"
    done

#llamada de la funcion

portscan
}

./OSIP > OSIP.txt