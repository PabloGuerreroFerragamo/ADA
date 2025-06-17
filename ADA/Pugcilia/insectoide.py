import re
import urllib.request
from urllib.parse import urljoin


def validar_email(email):
    """
    Validacion de una dirección de correo electrónico, True si es válido, False si no
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None


def extraer_datos_de_url(url):
    try:
        # Abrir la URL y leer su contenido
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')

            # Extraer todas las URLs
            urls_encontradas = re.findall(r'href=["\'](.*?)["\']', html)
            urls_absolutas = [urljoin(url, u) for u in urls_encontradas if u]

            # Extraer todos los correos electrónicos
            emails_encontrados = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)
            emails_validos = [e for e in emails_encontrados if validar_email(e)]

            return urls_absolutas, emails_validos
    except Exception as e:
        print(f"Error al procesar {url}: {e}")
        return [], []


def main():
    print("EXTRACTOR DE URLs Y CORREOS ELECTRÓNICOS")

    # Pedir 3 URLs al usuario
    urls = []
    for i in range(3):
        url = input(f"\nIngrese la URL #{i + 1}: ").strip()
        urls.append(url)

    # Archivos para guardar los resultados
    archivo_urls = open('urls_encontradas.txt', 'w')
    archivo_emails = open('emails_encontrados.txt', 'w')

    # Procesar cada URL
    for i, url in enumerate(urls, 1):
        print(f"\n\n=== RESULTADOS PARA URL {i} ===")
        print(f"Analizando: {url}")
        urls_encontradas, emails_encontrados = extraer_datos_de_url(url)

        # Mostrar y guardar URLs encontradas
        print(f"\nURLs encontradas en URL {i}:")
        for u in urls_encontradas:
            print(u)
            archivo_urls.write(u + '\n')

        # Mostrar y guardar emails encontrados
        print(f"\nCorreos electrónicos encontrados en URL {i}:")
        for e in emails_encontrados:
            print(e)
            archivo_emails.write(e + '\n')

        print(f"\nResumen URL {i}:")
        print(f"- Total URLs encontradas: {len(urls_encontradas)}")
        print(f"- Total emails válidos encontrados: {len(emails_encontrados)}")

    # Cerrar archivos
    archivo_urls.close()
    archivo_emails.close()

    print("\n\n=== RESUMEN FINAL ===")
    print("Proceso completado. Resultados guardados en:")
    print("- urls_encontradas.txt")
    print("- emails_encontrados.txt")


if __name__ == "__main__":
    main()