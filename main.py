# Script para hacer scrapping del valor del dólar en la página del BCV
# Y así obtener el valor del dólar en formato float
# Hecho por: Diego Faria
# Fecha: 29/12/2022

from bs4 import BeautifulSoup # pip i bs4
import requests # pip i requests
import urllib3
import time

# Desactiva advertencia por poblemas de SSL en la página del BCV
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) 

def numero_mes(mes):
    if mes == 'Diciembre':
        return 12
    elif mes == 'Noviembre':
        return 11
    elif mes == 'Octubre':
        return 10
    elif mes == 'Septiembre':
        return 9
    elif mes == 'Octubre':
        return 8
    elif mes == 'Julio':
        return 7
    elif mes == 'Junio':
        return 6
    elif mes == 'Mayo':
        return 5
    elif mes == 'Abril':
        return 4
    elif mes == 'Marzo':
        return 3
    elif mes == 'Febrero':
        return 2
    else:
        return 1

def separar_fecha(fecha):
    fecha = fecha[fecha.index(',') + 2:]
    fecha = fecha.replace('  ', ' ').split(' ')
    fecha[1] = str(numero_mes(fecha[1]))
    return '/'.join(fecha)

response = ''
while response == '':
    try:
        print("Conectando con 'https://www.bcv.org.ve/'")
        response = requests.get('https://www.bcv.org.ve/', verify=False)
        break
    except Exception as e:
        print(str(e))
        print("No se pudo conectar al BCV")
        print("Reintentando en 5 segundos")
        time.sleep(5)
        print("Reintentando...")
        continue

content = response.text
soup = BeautifulSoup(content, 'lxml')

box = soup.find('div', id='dolar')
valor_dolar = round(float(box.find('strong').text.replace(',', '.')), 2)
fecha = soup.find('span', class_='date-display-single').text

print(f"Fecha: {separar_fecha(fecha)}")
print(f"El Valor del dólar es: BsS. {valor_dolar}")