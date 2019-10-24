class TabelaInss():
    def __init__(self, valor_renda):
        self._valor_renda = valor_renda

    def calculo_tabela_inss(self, valor_renda):
        if (valor_renda >= 1903.99 and valor_renda <= 2826.65):
            calculo = 7.5 * valor_renda
            calculo = calculo/100
        elif (valor_renda>=2826.66 and valor_renda <= 3751.05):
            calculo = 15 * valor_renda
            calculo = calculo/100
        elif (valor_renda>=3751.06 and valor_renda <= 4664.68):
            calculo = 22.50 * valor_renda
            calculo = calculo/100
        else:
            calculo = 27.50 * valor_renda
            calculo = calculo/100
        return valor_renda - calculo