class Calculadora:

    def adicionar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return a / b

    def fatorial(self, n):
        if not isinstance(n, int):
            raise TypeError("Fatorial só é definido para números inteiros.")

        if n < 0:
            raise ValueError("Fatorial não definido para números negativos.")

        if n == 0:
            return 1

        return n * self.fatorial(n - 1)

    def potencia(self, base, expoente):
        return base ** expoente