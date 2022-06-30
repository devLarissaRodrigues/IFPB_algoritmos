# Faça um programa para apresentar todos os números da sequência a seguir: 0.00, 0.25, 0.50, 0.75, 
# 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 3.75, 4.00
n = 0

while n <= 4:
  if n < 4:
    print("%0.2f" %n, end=", ")
    n += 0.25
  else:
    print("%0.2f" %n, end=" ")
    n += 0.25
  

