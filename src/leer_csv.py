#libreria de python csv
import csv

def leer_csc_dict():
    ruta_archivo = 'data/empleados.csv'

    with open(ruta_archivo,'r') as archivo_csv:
        lector_dict = csv.DictReader(archivo_csv)
        for mapa in lector_dict:
            print(mapa)

def leer_csv():
    ruta_archivo = 'data/empleados.csv'

    #option 1
    #archivo = open('ruta_archivo')

    #option2
    with open(ruta_archivo,'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for linea in lector:
            print(linea)

if __name__ == '__main__':
    leer_csv()
    leer_csc_dict()