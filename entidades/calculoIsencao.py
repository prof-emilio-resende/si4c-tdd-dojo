from entidades.contribuinte import DadosContribuinte
from entidades.calculoInss import CalculadoraInss

class calculadora_isencao():
    def __init__(self,contribuinte):
        self.c = contribuinte

    def calcular(self):
        inss = CalculadoraInss(self.c)
        salario_base = self.c.valor_renda - self.c.calculo_dependente() - inss.calcular()
        return salario_base