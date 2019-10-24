from entidades.contribuinte import DescontoDependente

def test_enquadramento_sem_desconto():
    e = DescontoDependente(2,1000)
    valor_esperado = e.enquadramento()
    assert valor_esperado == 0