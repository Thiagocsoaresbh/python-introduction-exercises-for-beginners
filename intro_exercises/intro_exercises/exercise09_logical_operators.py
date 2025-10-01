"""
Exercício 9 — Operadores Lógicos
Objetivo: Apresentar os operadores lógicos em Python.
Conceito abordado: 'and', 'or', 'not' em comparação com '&&' e '||' de outras linguagens.
Enunciado:
Peça duas notas ao usuário. Aprove se ambas forem >= 6.
Caso contrário, verifique se pelo menos uma foi >= 6.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# 'and' → ambas condições precisam ser verdadeiras
if nota1 >= 6 and nota2 >= 6:
    print("Aprovado direto (as duas notas boas).")

# 'or' → pelo menos uma condição precisa ser verdadeira
elif nota1 >= 6 or nota2 >= 6:
    print("Recuperação (uma das notas foi boa).")

# 'not' → negação lógica
else:
    if not (nota1 >= 6 or nota2 >= 6):
        print("Reprovado (nenhuma nota foi suficiente).")
