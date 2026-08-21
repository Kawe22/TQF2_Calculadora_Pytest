import pytest
from calculadora import Calculadora


@pytest.fixture
def calculadora():
    return Calculadora()


# Testes unitários de Adição

def test_adicao_numeros_positivos(calculadora):
    assert calculadora.adicionar(5, 3) == 8


def test_adicao_numeros_negativos(calculadora):
    assert calculadora.adicionar(-5, -3) == -8


def test_adicao_numero_positivo_e_negativo(calculadora):
    assert calculadora.adicionar(5, -3) == 2


def test_adicao_com_zero(calculadora):
    assert calculadora.adicionar(5, 0) == 5


# Testes unitários de Subtração

def test_subtracao_numeros_positivos(calculadora):
    assert calculadora.subtrair(10, 4) == 6


def test_subtracao_resultado_negativo(calculadora):
    assert calculadora.subtrair(4, 10) == -6


def test_subtracao_numeros_negativos(calculadora):
    assert calculadora.subtrair(-10, -4) == -6


def test_subtracao_com_zero(calculadora):
    assert calculadora.subtrair(5, 0) == 5


# Testes unitários de Multiplicação

def test_multiplicacao_numeros_positivos(calculadora):
    assert calculadora.multiplicar(4, 5) == 20


def test_multiplicacao_numeros_negativos(calculadora):
    assert calculadora.multiplicar(-4, -5) == 20


def test_multiplicacao_positivo_e_negativo(calculadora):
    assert calculadora.multiplicar(4, -5) == -20


def test_multiplicacao_por_zero(calculadora):
    assert calculadora.multiplicar(10, 0) == 0


# Testes unitários de Divisão

def test_divisao_numeros_positivos(calculadora):
    assert calculadora.dividir(10, 2) == 5


def test_divisao_resultado_decimal(calculadora):
    assert calculadora.dividir(5, 2) == 2.5


def test_divisao_com_numero_negativo(calculadora):
    assert calculadora.dividir(-10, 2) == -5


def test_divisao_por_zero(calculadora):
    with pytest.raises(ZeroDivisionError):
        calculadora.dividir(10, 0)


# Testes unitários de Fatorial

def test_fatorial_numero_positivo(calculadora):
    assert calculadora.fatorial(5) == 120


def test_fatorial_de_zero(calculadora):
    assert calculadora.fatorial(0) == 1


def test_fatorial_de_um(calculadora):
    assert calculadora.fatorial(1) == 1


def test_fatorial_numero_negativo(calculadora):
    with pytest.raises(ValueError):
        calculadora.fatorial(-5)


def test_fatorial_numero_decimal(calculadora):
    with pytest.raises(TypeError):
        calculadora.fatorial(3.5)


# Testes unitários de Potência

def test_potencia_expoente_positivo(calculadora):
    assert calculadora.potencia(2, 3) == 8


def test_potencia_expoente_negativo(calculadora):
    assert calculadora.potencia(2, -2) == 0.25


def test_potencia_expoente_zero(calculadora):
    assert calculadora.potencia(5, 0) == 1


def test_potencia_base_negativa(calculadora):
    assert calculadora.potencia(-2, 3) == -8