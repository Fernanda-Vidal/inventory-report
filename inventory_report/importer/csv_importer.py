from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(path: str):
        with open(path) as file:
            if "csv" in path:
                reader = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )
                list_dict = [dict for dict in reader]
            else:
                raise ValueError("Arquivo inválido")

            return list_dict
