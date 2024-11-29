"""
charfun.py
Programa que determina si una cadena proporcionada por el
usuario es palíndroma. Para ello se preguntará por teclado al
usuario tantas veces como quiera hasta que escriba la palabra
salir.
Ultima Modificación. 21/11/2024
Autor. Gregorio Coronado Morón
Dependencias. Unicodedata
"""
import unicodedata

def esPalindromo(cadena):
    """
    Función que verifica si una cadena es palíndroma.
    Ignora espacios, mayúsculas, tildes y caracteres especiales.
    """
    # Validar tipo de entrada
    if not isinstance(cadena, str):
        raise TypeError("La entrada debe ser una cadena de texto.")
    
    # Normalizar la cadena (eliminar tildes y convertir a minúsculas)
    cadena_normalizada = unicodedata.normalize('NFD', cadena)  # Normaliza para descomponer los caracteres con tilde
    cadena_limpia = ''.join(char.lower() for char in cadena_normalizada if char.isalnum())
    
    # Comparar la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]

# Código principal que solicita entrada y verifica palíndromos
if __name__ == "__main__":
    while True:
        frase = input("Introduce una frase (o escribe 'salir' para terminar): ")
        if frase.lower() == "salir":
            print("Programa finalizado.")
            break
        else:
            # Comprobar si es palíndromo
            if esPalindromo(frase):
                print("La frase es palíndroma.")
            else:
                print("La frase no es palíndroma.")
