from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path: str):
        with open(path) as file:
            if "xml" in path:
                reader = file.read()
                list_dict = xmltodict.parse(reader["dataset"]["record"])
            else:
                raise ValueError

            return list_dict
