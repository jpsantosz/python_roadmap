import random
import string

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt)) 
            if value <= 0:  
                print("Por favor, insira um número positivo.")  
            else:
                return value 
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")  


digits = int(input("Quantos dígitos deseja para sua senha: "))
num_passwords = int(input("Quantas senhas deseja gerar: "))

for i in range(num_passwords):
    
    all_characters = string.digits + string.ascii_letters +string.punctuation
    password = "".join(random.choices(all_characters, k=digits))

    print(password)
    
print(f"{num_passwords} senhas foram geradas com sucesso!")