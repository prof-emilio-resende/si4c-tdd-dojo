from entidades.contribuinte import DadosContribuinte

def test_captura_dados():
    teste_captura = DadosContribuinte(5,5000)
    assert teste_captura.n_dependentes == 5
    assert teste_captura.valor_renda == 5000