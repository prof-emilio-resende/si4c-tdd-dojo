def test_salario_base_inss():
    salario_bruto = 3000
    valor_inss = 0.11
    valor_esperado = salario_bruto - (salario_bruto * valor_inss)
    assert calculo_salario_base_inss(salario_bruto) == valor_esperado