from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    def import_data(path: str):
        with open(path) as file:
            if "xml" in path:
                list_dict = list(
                    xmltodict.parse(file.read())["dataset"]["record"]
                )
            else:
                raise ValueError("Arquivo inválido")

            return list_dict
