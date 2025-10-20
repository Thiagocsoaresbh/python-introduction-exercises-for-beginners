"""
Exercício 3 — Declaração de Variáveis
Objetivo: Mostrar que não precisamos declarar o tipo em Python,
mas que podemos usar type hints em código de produção.
Conceito abordado: atribuição simples e type hints.
Enunciado:
Crie uma variável nota com valor 7.5 e mostre seu tipo.
Depois, declare uma variável nota2 com type hint indicando que é float.
"""

# Variável sem declarar tipo (dinâmica)
nota = 7.5
print("Valor de nota:", nota)
print("Tipo de nota:", type(nota))  # mostra que é float

# Variável com type hint (boa prática em código mais robusto)
nota2: float = 8.0
print("Valor de nota2:", nota2)
