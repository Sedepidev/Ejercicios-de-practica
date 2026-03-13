'''
La idea es crear un programa para calcular la relacion de aspecto de una imagen
que obtendremos de un URL.
'''


import requests       # para descargar la imagen desde internet
from PIL import Image # para abrir la imagen y leer su tamaño
from io import BytesIO # para tratar los bytes descargados como un archivo
import math           # para simplificar la relación de aspecto (ej: 16:9)


def obtener_relacion_aspecto(url_imagen):
    try:
        # Descargamos la imagen desde la URL
        # timeout=10 significa: si tarda más de 10 segundos, cancelar
        respuesta = requests.get(url_imagen, timeout=10)

        # Si la URL no existe o hay un error HTTP (404, 500...), lanza excepción
        respuesta.raise_for_status()

        # Convertimos los bytes descargados en un objeto imagen
        # BytesIO permite tratar bytes en memoria como si fuera un archivo
        imagen = Image.open(BytesIO(respuesta.content))

        # .size devuelve una tupla (ancho, alto) en píxeles
        ancho, alto = imagen.size

        # Calculamos el máximo común divisor para simplificar la fracción
        # Ejemplo: gcd(1920, 1080) = 120  →  1920/120 : 1080/120  =  16:9
        divisor = math.gcd(ancho, alto)
        ratio_w = ancho // divisor
        ratio_h = alto  // divisor

        # Mostramos los resultados
        print(f"Ancho:               {ancho} px")
        print(f"Alto:                {alto} px")
        print(f"Relación de aspecto: {ratio_w}:{ratio_h}")

        return ratio_w, ratio_h

    except requests.exceptions.ConnectionError:
        print("Error: no se pudo conectar. Revisa la URL o tu conexión a internet.")
    except requests.exceptions.Timeout:
        print("Error: la descarga tardó demasiado. Intenta de nuevo.")
    except requests.exceptions.HTTPError as e:
        print(f"Error HTTP: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

    return None


if __name__ == "__main__":
    url = input("Ingresa la URL de la imagen: ")
    obtener_relacion_aspecto(url)