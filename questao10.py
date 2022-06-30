# Construa um programa que leia uma quantidade indeterminada de números inteiros positivos e  identifique qual foi o maior número digitado. O final da série de números digitada deve ser indicado pela entrada de -1

n = 0
maior = 0

while n != -1:
  n = int(input("Digite um número inteiro positivo: "))
  if n > maior:
    maior = n
  
print(f"O maior número digitado foi {maior}")