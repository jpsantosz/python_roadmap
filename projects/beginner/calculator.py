def multiplicar(a: float, b: float):
    return a * b

def subtrair(a: float, b: float):
    return a - b

def somar(a: float, b: float):
    return a + b

def dividir(a: float, b: float):
    if b == 0:
        return "Erro: divisão por 0"
    return a / b

operacoes = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir
}

def calcular():
    while True:
        op = input("Qual operação deseja realizar? (+, -, *, /)\n").strip()

        if op not in operacoes:
            print("Operação inválida. Tente novamente.")
            continue

        try:
            primeiro_numero = float(input("Digite o primeiro número: "))
            segundo_numero = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

        resultado = operacoes[op](primeiro_numero, segundo_numero)
        print(f"Resultado: {resultado}")

        desejo = input("Deseja realizar outra operação? (S/N)\n").strip().upper()
        if desejo != "S":
            print("Encerrando calculadora. Até mais!")
            break

calcular()