# Se valor total da compra for menor que R$ 2500.00 o desconto será de 0%;
# Se valor total da compra for igual ou maior que R$ 2500.00 e menor que R$ 6000.00 o desconto será de 4%;
# Se valor total da compra for igual ou maior que R$ 6000.00 e menor que R$ 10000.00 o desconto será de 7%;
# Se valor total da compra for igual ou maior que R$ 10000.00 o desconto será de 11%;

# Deve-se implementar o print com uma mensagem de boas-vindas que apareça o seu nome [EXIGÊNCIA DE CÓDIGO 1 de 6];
# Deve-se implementar o input do valor unitário e da quantidade do produto [EXIGÊNCIA DE CÓDIGO 2 de 6];
# Deve-se implementar o desconto conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];
# Deve-se implementar o valor total sem desconto e o valor total com desconto [EXIGÊNCIA DE CÓDIGO 4 de 6];
# Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];  
# Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];

programmerName =  "Gabriel Regis da Silva"
print("Bem vindo ao programa de", programmerName + "!")

#inputs para capturar os valores de valor unitario e quantidade
unitValue = int(input("Valor unitário: "))
quantityValue = int(input("Quantidade de produto: "))

minQuantity = 3


# variavel global para soma final ao usuário digitar os valores
total = unitValue * quantityValue
                       
# operadores para as condições exigidas pelo programa
if quantityValue >= minQuantity:
  if total < 2500:
    print("A quantidade não está dentro do mínimo para obter desconto o valor de sua compra é", "R$", total, "(desconto de 0%)")

  elif total >= 2500 and total < 6000:
    print("Valor do produto sem desconto", "R$", total)
    descount = total - (total * 4) / 100
    print("Valor do produto com desconto", "R$", descount, "(desconto de 4%)")

  elif total >= 6000 and total < 10000:
    print("Valor do produto sem desconto", "R$", total)
    descount = total - (total * 7) / 100
    print("Valor do produto com desconto", "R$", descount, "(desconto de 7%)")  

  elif total >= 10000:
    print("Valor do produto sem desconto", "R$", total)
    descount = total - (total * 11) / 100
    print("Valor do produto com desconto", "R$", descount, "(desconto de 11%)")
  else:
  (print("a quantidade mínima para compra em atacado é ", minQuantity))