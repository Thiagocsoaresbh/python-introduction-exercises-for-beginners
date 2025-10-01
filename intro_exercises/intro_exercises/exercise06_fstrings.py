"""
Exercício 6 — f-strings e Formatação
Objetivo: Mostrar como usar f-strings em Python para interpolar valores em strings.
Conceito abordado: f-strings e formatação de valores (:.2f, :d, :s).
Enunciado:
Peça ao usuário o nome e a nota de uma disciplina.
Mostre a saída formatada com f-strings.
"""

nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))

# :s → string | :.2f → float com 2 casas decimais | :d → inteiro decimal
print(f"Aluno: {nome:s}")
print(f"Nota: {nota:.2f}")
print(f"Nota arredondada para inteiro: {int(nota):d}")
