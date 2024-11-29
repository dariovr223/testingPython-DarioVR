import unittest
from app.scripts.charfun import esPalindromo

class TestEsPalindromo(unittest.TestCase):
    def test_palindromos_validos(self):
        """Prueba con frases que son palíndromas."""
        frases_palindromas = [
            "ANAANA",
            "A man a plan a canal Panama",
            "No lemon, no melon",
            "aNnA",  # Palíndromo con mayúsculas y minúsculas
            "Able was I saw eLba",  # Frase intercalada
            "NoLemOn nOmeloN",  # Mezcla de mayúsculas y minúsculas

        ]
        for frase in frases_palindromas:
            resultado = esPalindromo(frase)
            self.assertTrue(
                resultado,
                f"La frase '{frase}' debería ser un palíndromo, pero la función devolvió {resultado}."
            )

    def test_no_palindromos(self):
        """Prueba con frases que no son palíndromas."""
        frases_no_palindromas = [
            "Hola mundo",
            "Python es genial",
            "Esto no es un palíndromo",
        ]
        for frase in frases_no_palindromas:
            resultado = esPalindromo(frase)
            self.assertFalse(
                resultado,
                f"La frase '{frase}' no debería ser un palíndromo, pero la función devolvió {resultado}."
            )
    
    def test_cadena_vacia(self):
        """Prueba con una cadena vacía, que técnicamente es un palíndromo."""
        resultado = esPalindromo("")
        self.assertTrue(
            resultado,
            "Una cadena vacía debería ser considerada un palíndromo."
        )
    
    def test_caracteres_especiales(self):
        """Prueba con caracteres especiales que no afectan el resultado."""
        frases = [
            "!@#$$#@!",
            "...",
            "    "
        ]
        for frase in frases:
            resultado = esPalindromo(frase)
            self.assertTrue(
                resultado,
                f"La frase '{frase}' debería ser un palíndromo, pero la función devolvió {resultado}."
            )

    def test_excepciones_tipo_incorrecto(self):
        """Prueba con entradas que no son cadenas."""
        entradas_invalidas = [12345, None, 5.6, ["a", "b", "c"], {"clave": "valor"}]
        for entrada in entradas_invalidas:
            with self.assertRaises(TypeError, msg=f"Se esperaba TypeError para la entrada {entrada}."):
                esPalindromo(entrada)

if __name__ == "__main__":
    unittest.main()
