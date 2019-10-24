import calcular from calculoInss.py
import Dadoscontribuinte from contribuinte.py

class Salario_Base():
    def __init__(self, inss, calculo_dependente, valor_renda ):
        self.inss = inss()
        self.calculo_dependente = calculo_dependente()
        self.valor_renda = valor_renda()

        def calculo_salario_bruto (self, inss, calculo_dependente, valor_renda):
            salario_base = valor_renda - inss - calculo_dependente
            return salario_base