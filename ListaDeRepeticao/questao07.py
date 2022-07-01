# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja  de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

n = 1
contador = 1
total = 0

while True:
  print("Lojas Tabajara\n")
  while n != 0:
    n = float(input(f"Produto {contador}: R$ "))
    contador += 1
    total += n
  print(f"Total: R$ {total}")
  dinheiro = float(input("Dinheiro: R$ "))
  print(f"Troco: R$ {dinheiro-total}\n")
  n = 1
  contador = 1
  total = 0
    
    