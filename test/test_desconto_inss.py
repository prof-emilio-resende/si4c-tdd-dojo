from entidades.contribuinte import DadosContribuinte
from entidades.calculoInss import CalculadoraInss
def test_calculo_inss():
   salario_bruto = 3000
   inss = 0.11
   valor_esperado = salario_bruto * inss
   contribuinte = DadosContribuinte(0,salario_bruto)
   assert CalculadoraInss(contribuinte).calcular() == valor_esperado
