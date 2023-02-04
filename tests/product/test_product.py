from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="café",
        nome_da_empresa="melita",
        data_de_fabricacao="19/10/2022",
        data_de_validade="20/02/2023",
        numero_de_serie=2,
        instrucoes_de_armazenamento="local seco",
    )
    assert product.id == 1
    assert product.nome_do_produto == 'café'
    assert product.nome_da_empresa == "melita"
    assert product.data_de_fabricacao == "19/10/2022"
    assert product.data_de_validade == "20/02/2023"
    assert product.numero_de_serie == 2
    assert product.instrucoes_de_armazenamento == "local seco"
