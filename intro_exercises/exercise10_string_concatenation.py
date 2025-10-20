"""
Exercício 10 — Concatenação de Strings
Objetivo: Mostrar diferentes formas de juntar strings.
Conceito abordado: uso de +, vírgula no print e f-string.
Enunciado:
Crie duas variáveis com o primeiro e o último nome de uma pessoa.
Mostre o nome completo de três formas diferentes.
"""

primeiro_nome = "João"
ultimo_nome = "Silva"

# Usando +
print("Nome completo (com +): " + primeiro_nome + " " + ultimo_nome)

# Usando vírgula → adiciona espaço automaticamente
print("Nome completo (com vírgula):", primeiro_nome, ultimo_nome)

# Usando f-string → mais elegante
print(f"Nome completo (com f-string): {primeiro_nome} {ultimo_nome}")
