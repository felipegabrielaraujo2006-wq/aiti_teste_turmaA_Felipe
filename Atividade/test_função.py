import pytest

@pytest.fixture
def numeros():
    return [1,2,3,4,5]

def soma_dobro(numeros):
    return sum(x*2 for x in numeros)

def test_soma_dobro(numeros):
    resultado_real = soma_dobro(numeros)
    resultado_esperado = 30
    assert resultado_real == resultado_esperado