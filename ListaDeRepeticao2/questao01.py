# Escreva um programa em Python que calcule o valor de H, sendo que ele é determinado pelo 
# somatório a seguir:
# H = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50

numerador = denominador = soma = 0

for i in range(1,100):
  if i % 2 != 0:
    numerador = i
    denominador += 1
    relacao = numerador/denominador
    soma += relacao

print("A soma de H é igual a %.4f" %soma)