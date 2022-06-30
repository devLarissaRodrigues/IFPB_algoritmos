# Desenvolva um programa gerador de tabuadas de uma operação escolhida pelo usuário (1 – adição, 2 
# – subtração, 3 – multiplicação, 4 – divisão). O programa deve a tabuada de qualquer número inteiro 
# entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada.

n = int(input("Informe um número: "))
print("Informe a operação dentro das opções:\n1 – Adição\n2 – Subtração\n3 – Multiplicação\n4 – Divisão")

operacao = int(input("Operação : "))

if operacao == 1:
  print(f"\nTabuada de Adição: {n}")
  for i in range(1, 11):
    print(f"{n} + {i} = {n+i}")
  
elif operacao == 2:
  print(f"\nTabuada de Subtração {n}")
  for i in range(1, 11):
    print(f"{n} - {i} = {n-i}")

elif operacao == 3:
  print(f"\nTabuada de Multiplicação: {n}")
  for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

elif operacao == 4:
  print(f"\nTabuada de Divisão: {n}")
  for i in range(1,11):
    print(f"{n} / {i} = {n/i:.2f}")
