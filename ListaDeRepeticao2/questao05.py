# Maria comprou vários tipos de doce de banana, de diversos fornecedores. Após provar e guardar 
# os doces, Maria quis saber qual o doce mais barato e o valor total da compra. Para ajudar Maria 
# e outras pessoas que desejam comprar doce, faça um programa em Python que receba de início 
# a quantidade total de doces comprados e em seguida, o peso (em gramas) e o valor (em R$) de 
# cada doce comprado. Calcule e exiba o preço unitário (R$ por quilograma) de cada doce e no 
# final, informe o número do doce mais barato e o peso total e o gasto total realizado.


contador = 0
peso_total = 0
preco_total = 0
doce_mais_barato = 10000000000000000000000

total_doces = int(input("Informe o total de doces comprados: "))

while contador < total_doces:
  contador += 1
  print(f"\nDoce {contador}:")
  peso_grama = float(input("Informe o Peso (g): "))
  preco = float(input("Informe o Preço (R$): "))
  peso_kg = peso_grama/1000
  preco_unitario = preco/peso_kg
  print(f"Preço unitário calculado = R$ {preco_unitario}/kg")
  peso_total += peso_grama
  preco_total += preco_unitario
  print("Preco total", preco_total)
  
  if preco_unitario < doce_mais_barato:
    doce_mais_barato = preco_unitario
    mais_barato = contador

print(f"\nDados Finais da Compra:\nProduto mais barato: Doce {mais_barato}\nForam comprados {peso_total}g de doce por R$ {preco_total:.2f}")