from entidades.contribuinte import DadosContribuinte
from entidades.calculoIsencao import calculadora_isencao

def test_calculo_isencao():
    salario_bruto = 3500
    salario_base = 2735.02
    isencao = 1903.98
    valor_esperado =  salario_base - isencao

    contribuinte = DadosContribuinte(2, salario_bruto)

    assert calculadora_isencao(contribuinte).calcular() == valor_esperado