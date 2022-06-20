email_tmpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
 
Este produto é ótimo para resolver 
%(texto)s
     
Clique afora em %(link)s
    
Apenas %(quantidade)d disponiveis!
Preço promocional %(preço).2f
"""

clientes = ["Maria", "João", "Bruno"]

clientes = ["Maria", "João", "Paulo Cesar"]

for cliente in clientes:
    print(email_tmpl % {"nome": cliente, "produto": "caneta",   
        "texto": "Escrever muito bem", "link": "https://canetaslegais.com",
        "quantidade": "1", "preço": 50.5,
         }
     )
