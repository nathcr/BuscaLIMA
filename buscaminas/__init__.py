def my_sum(x, y):
    """A function that sums. """
    return x+y
def multiplos_de_cinco_fibonacci(n):
    """Definimos la funcion de los numero de fibonacci"""
    fibs = []
    a, b = 0, 1
    while a <= n: #Determinamos que los numeros sean menor que un n dado
        if a%5==0:  #verificamos que sea multiplo de 5
            fibs.append(a) #Lo añadimos a la lista
        a, b = b, a+b
    return fibs
def my_mul(x, y):
    """A function that multiply. """
    return x*y
