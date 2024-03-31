def verifica_fibonacci(numero):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    fib1, fib2 = 0, 1
    
    # Enquanto o valor de fib1 for menor ou igual ao número fornecido
    while fib1 <= numero:
        # Se o número fornecido for igual a fib1, ele pertence à sequência de Fibonacci
        if fib1 == numero:
            return True
        # Atualiza os valores de fib1 e fib2 para os próximos números da sequência
        fib1, fib2 = fib2, fib1 + fib2
    
    # Se o número não foi encontrado na sequência até aqui, significa que não pertence
    return False

# Função principal
def main():
    # Número a ser verificado na sequência de Fibonacci
    numero = 245  # Você pode alterar este número conforme necessário
    
    # Verifica se o número pertence à sequência de Fibonacci e imprime o resultado
    if verifica_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# Chama a função principal
if __name__ == "__main__":
    main()
