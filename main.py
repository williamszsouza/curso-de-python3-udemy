import random

cpf = ''
for i in range(9):
    cpf += str(random.randint(0,9))


contador_regressivo = 10

resultado = 0
for numero in cpf:
    resultado += int(numero) * contador_regressivo
    contador_regressivo -= 1

primeiro_digito = ((resultado * 10)%11)    

primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0


contador_regressivo2 = 11
cpf = cpf + str(primeiro_digito)

resultado2 = 0
for num in cpf:
    resultado2 += int(num) * contador_regressivo2
    contador_regressivo2 -= 1

segundo_digito = ((resultado2*10) % 11)

segundo_digito = segundo_digito if segundo_digito <= 9 else 0
cpf = cpf + str(segundo_digito)

print(f"cpf final: {cpf}")