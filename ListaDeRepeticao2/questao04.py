# Faça um programa que apresente o menu de opções a seguir, permita ao usuário escolher a 
# opção desejada, receba os dados necessários para executar a operação e exiba o resultado. 
# Verifique a possibilidade de opção inválida e no caso do salário apenas não permita salários 
# # menores ou igual a zero, e nesse caso solicite uma nova digitação do salário: Menu de opções:
# 1. Imposto
# 2. Novo Salário
# 3. Salário Líquido
# 4. Finalizar o Programa

opcao = 0

while opcao != 4:
  print("*" * 25, "\nMENU DE OPÇÕES:\n1. Imposto\n2. NovoSalário\n3. Salário Líquido\n4. Finalizar o Programa\n"+"*"*25)
  opcao = int(input("Digite uma das opções: "))
  
  if opcao == 1:
    salario = float(input("Digite seu salário: R$ "))
    if salario <= 0:
      salario = float(input("Digite seu salário: R$ "))
    if salario > 0 and salario < 1000:
      imposto = 0.05 * salario
    elif salario >= 1000 and salario <= 1500:
      imposto = 0.01 * salario
    else:
      imposto = 0.015 * salario
    print("Imposto: R$", imposto)

  elif opcao == 2:
    salario = float(input("Digite seu salário: R$ "))
    if salario <= 0:
      salario = float(input("Digite seu salário: R$ "))
    if salario > 0 and salario < 1000:
      aumento = salario + (0.05 * salario)
    elif salario >= 1000 and salario <= 1250:
      aumento = salario + (0.07 * salario)
    elif salario > 1250 and salario < 1500:
      aumento = 100
    else:
      aumento = 150

    print("Aumento: R$", aumento)

  elif opcao == 3:
    salario = float(input("Digite seu salário: R$ "))
    if salario <= 0:
      salario = float(input("Digite seu salário: R$ "))
    if salario > 0 and salario < 1000:
      imposto = 0.05 * salario
    elif salario >= 1000 and salario <= 1500:
      imposto = 0.01 * salario
    else:
      imposto = 0.015 * salario

    salario_liquido = salario - imposto
    print("Salário líquido: R$", salario_liquido)

  elif opcao != 4:
    print("Opção inválida\n")