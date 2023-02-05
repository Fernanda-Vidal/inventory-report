from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    def generate(list_dict):
        simple = SimpleReport.generate(list_dict)
        companies = Counter(dict["nome_da_empresa"] for dict in list_dict)
        response = f"{simple}\n"

        for nome, qtd in companies.items():
            response += (f"- {nome}: {qtd}")
        return response
