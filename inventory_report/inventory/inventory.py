import xmltodict
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        if "csv" in path:
            list_dict = CsvImporter.import_data(path)

        if "json" in path:
            list_dict = JsonImporter.import_data(path)

# https://pypi.org/project/xmltodict/
        if "xml" in path:
            with open(path) as file:
                content = file.read()
                list_dict = xmltodict.parse(content)

        complete = CompleteReport.generate(list_dict=list_dict)
        simple = SimpleReport.generate(list_dict=list_dict)

        return simple if type == "simples" else complete
