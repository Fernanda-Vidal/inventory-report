import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        with open(path) as file:
            report_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            list_dict = [dict for dict in report_reader]

            if type == 'simples':
                return SimpleReport.generate(list_dict=list_dict)
            else:
                return CompleteReport.generate(list_dict=list_dict)
