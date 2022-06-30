# Faça um programa que calcula a média aritmética de um conjunto de números pares que forem fornecidos pelo usuário. O valor de finalização será a entrada do número 0. Observe que nada impede que o usuário forneça quantos números ímpares quiser, com a ressalva que esses números não serão contabilizados para média. Considere que os números informados sempre serão inteiros positivos ou zero.

n = -1
contador = 0
soma = 0

while n != 0:
  n = int(input("Digite um número inteiro positivo: "))
  if n % 2 == 0 and n != 0:
    contador += 1
    soma += n

print(f"A média dos números pares digitados é {(soma/contador):.2f}")