# Faça um programa que receba o salário de um funcionário chamado Jorge. Sabe-se que outro  funcionário, Saulo, tem salário equivalente a um terço do salário de Jorge. Jorge aplicará seu salário integralmente na caderneta de poupança, que rende 2% ao mês, e Saulo aplicará seu salário  integralmente no fundo de renda fixa, que rende 5% ao mês. O programa deverá calcular e exibir na  tela a quantidade de meses necessários para que o valor pertencente a Saulo iguale ou ultrapasse o  valor pertencente a Jorge.

salario_jorge = float(input("Digite o salário de Jorge: R$ "))
salario_saulo = salario_jorge/3
mes = 0

while salario_jorge > salario_saulo:
  salario_jorge += (salario_jorge * 0.02)
  salario_saulo += (salario_saulo * 0.05)
  mes += 1

print(f"Em {mes} meses, o salário de Saulo será igual ou superior ao de Jorge")
    
  




