from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list_dict):
        comp = []

        oldest = min(dict["data_de_fabricacao"] for dict in list_dict)
        next_expiration = min(dict["data_de_validade"] for dict in list_dict)

        for d in list_dict:
            comp.append(d["nome_da_empresa"])

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {next_expiration}\n"
            f"Empresa com mais produtos: {Counter(comp).most_common(1)[0][0]}"
            )
