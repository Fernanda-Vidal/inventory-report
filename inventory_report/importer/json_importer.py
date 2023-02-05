from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(path: str):
        with open(path) as file:
            if "json" in path:
                reader = file.read()
                list_dict = json.loads(reader)
            else:
                raise ValueError

            return list_dict
