import csv
import rules

class GenerateOutput:
    @staticmethod
    def parseCSV(data):
        with open('dados.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')

            for item in data:
                header = item['header']
                writer.writerow(rules.header_field_names)
                writer.writerow([header[field] for field in rules.header])
                writer.writerow(rules.details_field_names)
                for detail in item['details']:
                    writer.writerow([detail[field] for field in rules.details])
