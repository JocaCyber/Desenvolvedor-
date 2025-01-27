def is_fibonacci_number(n):
    # Inicializando os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1

    # Gerando a sequência até atingir ou ultrapassar o número informado
    while a <= n:
        if a == n:
            return True  # Se o número estiver na sequência
        a, b = b, a + b

    return False  # Se o número não estiver na sequência


# Entrada do número (pode ser alterado para entrada do usuário)
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verificando se o número pertence à sequência
if is_fibonacci_number(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

