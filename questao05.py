#  Elabore um algoritmo que efetue a soma de todos os números ímpares que são múltiplos de 3 e que se 
# encontram no conjunto inteiros de 1 até 500.

soma = 0

for i in range(1,501,2):
  if i % 3 == 0:
    soma += i

print(soma)