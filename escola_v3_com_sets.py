


# #! /usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por salas que frequentas cada uma das 
atividades.
"""
__Version__ = "0.1.0"
sala = {
    "sala1": ["Erick", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}
aula = {
    "ingles": ["Erick", "Maia", "Joana", "Antonio", "Carlos"],
    "musica": ["Erick", "Carlos", "Maria"],
    "danca":  ["Gustavo", "Sofia", "Joana", "Antonio"]
}
atividades = {
    "Inglês":"ingles",
    "Música": "musica",
    "Dança": "danca",
}
for atividade  in atividades.values():
    print(f"Alunos da atividade {atividade}\n")
    for aluno in aula[atividade]: 
        for aluno in sala["sala1"]:
            if aluno in sala["sala1"]:
             print(f"Sala 1:{aluno} ")
# Listar alunis em cada atividade por sala

#print(atividades["Inglês"])

# for nome_atividade in atividades:

#     print(f"Alunos da atividade {nome_atividade}\n")
#     print("-" * 40)

#     atividade_sala1 =[]
#     atividade_sala2 =[]

#     for aluno in sala["sala1"]:
#         print(aluno)   
#         if aluno in sala["sala1"]:
#             atividade_sala1.append(aluno)
#         elif aluno in sala["sala2"]:
#             atividade_sala2.append(aluno) 

#     print(f"Sala1", atividade_sala1)
#     print(f"Sala2", atividade_sala2)
# # 
#     # print()
#     # print("#" * 40)
