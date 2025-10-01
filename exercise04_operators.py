"""
Exercício 4 — Operadores Matemáticos
Objetivo: Explorar operadores aritméticos básicos em Python.
Conceito abordado: +, -, *, /, //, %, **.
Enunciado:
Peça ao usuário dois números inteiros e mostre os resultados
das operações de soma, subtração, multiplicação, divisão,
divisão inteira, resto e potência.
"""

# Entrada de dados
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

# Operações matemáticas
print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)       # divisão normal, resultado float
print("Divisão inteira:", a // b)  # resultado sem casas decimais
print("Resto da divisão:", a % b)
print("Potência:", a ** b)     # a elevado a b
