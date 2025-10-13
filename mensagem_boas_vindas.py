'''
primicias
Pedir o nome e idade;
Armazenar em str, armazenar em int
Exibe em tela a mensagem
Concateados com o nome e idade
'''
print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
print("\fBem vindo a CDT!")
print("\n¨¨¨¨¨¨¨¨¨¨¨¨¨¨")

nome_pessoa = str(input("Qual seu nome?"))

idade_pessoa = int(input("Qual é sua idade?"))

altura_pessoa = float(input("Qual é sua altura?"))

cartão_pessoa = str(input("Qual é o número do seu cartão?"))

print(f"Olá, {nome_pessoa}")
print(f"Sua idade é {idade_pessoa}")
print(f"Sua altura é {altura_pessoa}")
print(f"Número do seu cartão que irei roubar é {cartão_pessoa}")