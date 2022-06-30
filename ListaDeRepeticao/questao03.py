# Desenvolva um programa gerador de tabuada de multiplicação, capaz de gerar a O programa deve a 
# tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja 
# ver a tabuada.

n = int(input("Informe um número: "))

if n >= 1 and n <= 10:
  print(f"\nTabuada de Multiplicação: {n}")
  
  for i in range(11):
    print(f"{n} x {i} = {n*i}")

else:
  print("ERRO! Você deveria digitar um número inteiro entre 1 e 10.")