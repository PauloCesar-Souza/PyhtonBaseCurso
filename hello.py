# #!C:\projects\Curso_Python_BrunoRocha\PyhtonBaseCurso\hello.py  -> SHEBANG
"""Hello World Multi Linguas
Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.
Como usar:
Tenha a variável LANG devidamente configurada ex:
    export LANG=pt_BR
Execução:
    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.3"
__author__ = "Paulo Cesar"
__licence__ = "Unlicence"
# Dunder - Identificador

#from ast import arguments
import os
import sys


arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:
    # TODO: Tratar Value Error
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    arguments[key] = value      # type: ignore

# padrão snake case -- Pascal Case : CurrentLanguage
current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição 
    if "LANG" in os.environ:
        current_language = os.getenv("LANG") 
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]   

msg = {
    "en_US":"Hello, Word!",
    "pt_BR":"olá, Mundo!",
    "it_IT":"Ciao, Mondo!",
    "es_SP":"Hola, Mundo!",
    "fr_FR":"Bonjour, Monde!",
} 

print(msg[current_language] * int(arguments["count"]))

# sets (hash Table) - 0(1) - constante
# dicts (Hash Table)

# Ordem Complexidade o(n)
# if current_language == "pt_BR":
#     msg = "Óla, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"    
# elif current_language == "es_SP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde!"        

#print(msg)   # Este programa imprime Hello world