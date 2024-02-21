#Verificação de pertencimento à sequência de Fibonacci:

def pertence_a_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False

numero = int(input("Digite um numero para verificar se pertence a sequencia de Fibonacci: "))
if pertence_a_fibonacci(numero):
    print(f"O numero {numero} pertence a sequencia de Fibonacci.")
else:
    print(f"O numero {numero} NAO pertence a sequencia de Fibonacci.")
