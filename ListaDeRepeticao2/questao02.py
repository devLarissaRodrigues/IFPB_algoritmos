# Faça um programa que solicite um número inteiro positivo para usuário e informe se esse número é primo.

n = int(input("Digite um número inteiro positivo: "))
acumulador = 0

for i in range(1, n+1):
  if n % i == 0:
    acumulador +=1
  
if acumulador == 2:
  print(f"O número {n} é primo.")
else:
  print(f"O número {n} não é primo!")