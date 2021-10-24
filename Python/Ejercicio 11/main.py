# EJERCICIO 11

# Participantes:
# Gerardo Gámez Serna
# Jose Luis Hernandez Meza
# Francisco Javier Valerio Lara

import time
import argparse
import requests
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os

# Iniciamos argparse
parser = argparse.ArgumentParser(
    description = "Programa para buscar imagenes en la web"
    )

# Añadimos los argumentos que requiramos
parser.add_argument("-link", "--link", type = str, help = "Escriba la URL de la que desee descargar las imagenes")
parser.add_argument("-r", "--ruta", type = str, help = "Escriba la ruta de guardado de las imagenes")

# Analizar los argumentos
args = parser.parse_args()
print(args)

link = args.link
ruta = args.ruta

print("INICIANDO PROGRAMA...\n")
time.sleep(2)

def download(link):
    while 1 == 1:
        count = count + 1
        if link.status_code == 200:
            print("Pagina encontrada\n")
            time.sleep(1)
            print("Descargando imagen...\n")
            time.sleep(2)
            img = requests.get(args.link).content
            with open("imagen" + count + ".jpg", "wb") as handler:
                handler.write(img)
                print ("Se ha descargado la imagen")

        elif link.status_code != 200:
            print("No se encontro la pagina, vuelva a intentarlo")
            exit()

def GPS(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        # Parse geo references.
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
        input()

def meta(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    GPS(ret)
    return ret

def printMeta(ruta):
    while 1 == 1:
        conta = 1
        numero = conta + 1
        os.chdir(ruta)
        for root, dirs, files in os.walk(".", topdown = False):
            for name in files:
                print(os.path.join(root, name))
                print ("[+] Metadata for file: %s " %(name))
                input()
                try:
                    exifData = {}
                    exif = meta(name)
                    for metadata in exif:
                        print ("Metadata: %s - Value: %s " %(metadata, exif[metadata]))
                    print ("\n")
                except:
                    import sys, traceback
                    traceback.print_exc(file=sys.stdout)
                f = open ("meta" + numero + ".txt",'w')
                f.write("Imagen" + numero, metadata)
                f.close()
printMeta()