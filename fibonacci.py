def is_fibonacci(n):

    a, b = 0, 1
    
    while b < n:
        a, b = b, a + b
    
    if b == n or n == 0:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

numero = 21

resultado = is_fibonacci(numero)
print(resultado)