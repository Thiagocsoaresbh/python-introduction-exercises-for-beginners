"""
Exercício 8 — Estrutura Condicional
Objetivo: Explicar como funciona o if/else em Python.
Conceito abordado: não usamos chaves {} (como em C/Java), mas sim indentação obrigatória.
Enunciado:
Peça ao usuário uma nota. Se for maior ou igual a 6, mostre 'Aprovado'.
Caso contrário, mostre 'Reprovado'.
"""

nota = float(input("Digite a nota do aluno: "))

if nota >= 6:  # condição
    print("Aprovado")  # bloco executado se a condição for verdadeira
else:
    print("Reprovado")  # bloco executado caso contrário
