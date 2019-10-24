class DadosContribuinte():
    def __init__(self, n_dependentes, valor_renda):
        self.n_dependentes = n_dependentes
        self.valor_renda = valor_renda
        self.valor_dependente = 189.59

    def calculo_dependente(self, n_dependentes, valor_dependente):
        return self.n_dependentes * self.valor_dependente