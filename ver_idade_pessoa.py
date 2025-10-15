'''
Primicias
     Verificar a idade de uma pessoa.
Saber a idade da pessoa; 
armazeanar a idade em uma variavel (int);
caso a idade seja maior que 18 anos;
 exibir a mensagem "Você é maior de idade";
 Se não for maior que 18 anos, mostrar a mensagem 'voc~e é maior de idade'
'''
#Criando Estruturas
print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print("\fOlá, Seja bem-vindo! ^u^")
print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

nome_pessoa = str(input(" Qual seu nome? "))
idade_pessoa = int(input(" Qual é sua idade? "))

## Lógica do programa 
# se (if) variável (idade_pessoa) critério (>=) valor (18)
# condição (maior ou igual a 18 anos)
if idade_pessoa >= 18:
    print("Muito bem! Você é maior de idade.^-^")

else:
    print ("Aah, que pena! Você é menor de idade. Tente na próxima! u_u")

print(f"Olá, (nome-pessoa)! Sua idade é (idade-pessoa).")
