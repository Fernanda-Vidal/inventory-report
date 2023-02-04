from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list_dict):
        empresas = []

        oldest = min(dict["data_de_fabricacao"] for dict in list_dict)
        next_expiration = min(
            dict["data_de_validade"] for dict in list_dict
        )

        for d in list_dict:
            empresas.append(d["nome_da_empresa"])

        return f"""
            Data de fabricação mais antiga: {oldest}
            Data de validade mais próxima: {next_expiration}
            Empresa com mais produtos: {Counter(empresas).most_common(1)[0][0]}
            """
