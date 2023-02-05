from inventory_report.inventory.product import Product


def test_relatorio_produto():
    # pass  # Seu teste deve ser escrito aqui
    produto = Product(
        1,
        "café",
        "melita",
        "19/10/2022",
        "20/02/2023",
        2,
        "local seco"
    )
    retorno = (
            f"O produto {produto.nome_do_produto}"
            f" fabricado em {produto.data_de_fabricacao}"
            f" por {produto.nome_da_empresa} com validade"
            f" até {produto.data_de_validade}"
            f" precisa ser armazenado {produto.instrucoes_de_armazenamento}."
        )

    assert repr(produto) == retorno
