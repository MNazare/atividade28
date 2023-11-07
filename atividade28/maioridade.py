# Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

hoje = date.hoje()
anoHoje = hoje.year()

maiorIdade = []
menorIdade = []

for i in range(8):
    anoNascimento = int(input("digite seu ano de nascimento: "))
    if anoHoje - anoNascimento >= 18:
        maiorIdade.append(anoNascimento)
    else:
        menorIdade.append(anoNascimento)

print(f"quem nasceu em {menorIdade} é menor de idade ")
print(f"quem nasceu em {maiorIdade} é maior de idade ")
                        