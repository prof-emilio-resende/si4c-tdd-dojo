class CalculadoraInss():
    def __init__(self,contribuinte):
        self.contribuinte = contribuinte

    def calcular(self):
        inss = self.contribuinte.valor_renda*(11/100)
        return inss