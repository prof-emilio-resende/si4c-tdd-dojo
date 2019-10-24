from entidades.contribuinte import DadosContribuinte

def test_desconto_dependente():
    contribuinte = DadosContribuinte(2,2000)
    valor_dependente = contribuinte.calculo_dependente()
    assert valor_dependente == 379.18