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
__version__ = "0.0.1"
__author__ = "Paulo Cesar"
__licence__ = "Unlicence"
# Dunder - Identificador

import os
# padrão snake case -- Pascal Case : CurrentLanguage
current_language = os.getenv("LANG", "en_US")[:5]       

msg = "Hello, Word!"

if current_language == "pt_BR":
    msg = "Óla, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"    
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"        

print(msg)   # Este programa imprime Hello world
