# Faça um programa que calcule o retorno de um investimento financeiro fazendo as contas mês 
# a mês, sem usar a fórmula de juros compostos
# • O usuário deve informar quanto será investido por mês e qual será a taxa de juros mensal
# • O programa deve informar o saldo do investimento após um ano (soma das aplicações 
# mês a mês considerando os juros compostos), e perguntar ao usuário se ele deseja que 
# seja calculado o ano seguinte, sucessivamente
# • Por exemplo, caso o usuário deseje investir R$ 100,00 por mês, e tenha uma taxa de juros 
# de 1% ao mês, o programa forneceria a seguinte saída:
# Saldo do investimento após 1 ano: R$ 1268.25
# Deseja processar mais um ano? (S/N)


deseja_continuar = 'S'
soma_investimento = 0

while deseja_continuar == "S" or deseja_continuar == 's':
  investimento = float(input("Digite qual o valor do investimento: R$ "))
  taxa_mensal = float(input("Digite a taxa mensal: "))
  
  for i in range(12):
    investimento = (investimento + (taxa_mensal*investimento))
  
  print("Juros: %0.2f" %investimento)

  deseja_continuar = input("Deseja processar mais um ano? (S/N) ")
  
