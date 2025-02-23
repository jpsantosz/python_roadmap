# Escreva uma função que recebe uma string contendo apenas ( e ) e verifica se os parênteses estão corretamente balanceados.

def get_valid_string(string):
    while True:
        frase = input(string)  
        
        # Se encontrar um caractere inválido, peça a entrada novamente
        if any(char not in '()' for char in frase):  
            print("Por favor, insira uma string válida contendo apenas '(' e ')'.")
            continue
        
        return frase  # Retorna apenas se for válida

def is_balanced(string):
    stack = []
    
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False  # Se encontrar ')' sem um '(' correspondente, está desbalanceado
            stack.pop()  # Remove um '(' correspondente
    
    return len(stack) == 0 

frase = get_valid_string("insira uma string válida contendo apenas '(' e ')': ")
print(is_balanced(frase))