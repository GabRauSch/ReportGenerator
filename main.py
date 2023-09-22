import rules
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
from GenerateOutput import GenerateOutput

class CreateReport:
    def __init__(self):
        self.nome_arquivo = 'modelo_arquivo.txt'
        self.information = []
        self.current_index = -1
        self.empresa = ''
        self.inscricao = ''
        self.nome_banco = ''
        self.forma_lancamento = ''

    def create_new_object(self):
        data = {
                "header": {
                    "empresa": "",
                    "inscricao": "",
                    "nome_banco": "",
                    "nome_rua": "",
                    "numero_local": "",
                    "nome_cidade": "",
                    "cep": "",
                    "sigla_estado": "",
                    "forma_lancamento": "",
                },
                "details": []
        }
        self.current_index+=1
        self.information.append(data)

    def assign_file_header_info(self, line):
        empresa = line[rules.campos['empresa']].strip()
        inscricao = line[rules.campos['inscricao']].strip()
        cnpj_formatado = "{0}.{1}.{2}/{3}-{4}".format(
            inscricao[:2],
            inscricao[2:5],
            inscricao[5:8],
            inscricao[8:12],
            inscricao[12:]
        )
        nome_banco = line[rules.campos['nome_banco']].strip()

        self.empresa = empresa
        self.inscricao = cnpj_formatado
        self.nome_banco = nome_banco

    def assign_batch_header_info(self, line):
        nome_rua = line[rules.campos['nome_rua']].strip()
        numero_local = line[rules.campos['numero_local']].strip()
        nome_cidade = line[rules.campos['nome_cidade']].strip()
        
        cep_inicial = line[rules.campos['cep_inicial']].strip()
        cep_complemento = line[rules.campos['cep_complemento']].strip()
        cep = f"{cep_inicial}-{cep_complemento}"

        sigla_estado = line[rules.campos['sigla_estado']].strip()
        
        index_forma_lancamento = int(line[rules.campos['index_forma_lancamento']].strip()) -1
        forma_lancamento = rules.forma_lancamento[index_forma_lancamento]
                
        self.create_new_object()

        print(self.empresa)

        header_info = {
            "empresa": self.empresa,
            "inscricao": self.inscricao,
            "nome_banco": self.nome_banco,
            "nome_rua": nome_rua,
            "numero_local": numero_local,
            "nome_cidade": nome_cidade,
            "cep": cep,
            "sigla_estado": sigla_estado
        }

        self.information[self.current_index]['header'].update(header_info)
        self.forma_lancamento = forma_lancamento


    def assign_details_info(self, line):
        nome_favorecido = line[rules.campos['nome_favorecido']].strip()
        
        date = line[rules.campos['date']].strip()
        data_pagamento = datetime.strptime(date, "%d%m%Y").strftime("%d/%m/%Y")
        
        valor_original = line[rules.campos['valor_original']].strip()
        valor_reais = locale.format_string('%0.2f', int(valor_original) / 100, grouping=True)
        valor_pagamento = f'R$ {valor_reais}'

        numero_documento_atribuido_empresa = line[rules.campos['numero_documento_atribuido_empresa']].strip()

        forma_lancamento = self.forma_lancamento

        data ={
            'nome_favorecido': nome_favorecido,
            'data_pagamento': data_pagamento,
            'valor_pagamento': valor_pagamento,
            'numero_documento_atribuido_empresa': numero_documento_atribuido_empresa,
            'forma_lancamento': forma_lancamento
        }
        
        self.information[self.current_index]["details"].append(data)

    def assign_batch_trailer_info(self, line):
        pass

    def assign_file_trailer_info(self, line):
        pass

    def main(self):
        try:
            with open(self.nome_arquivo, 'r', encoding='utf-8') as file:
                register_handlers = {
                    0: self.assign_file_header_info,
                    1: self.assign_batch_header_info,
                    3: self.assign_details_info,
                    5: self.assign_batch_trailer_info,
                    9: self.assign_file_trailer_info,
                }
                for line in file:
                    register_type = int(line[rules.campos['tipo_registro']])
                    if register_type in register_handlers:
                        register_handlers[register_type](line)

            GenerateOutput.parseCSV(self.information)
        except FileNotFoundError:
            print('File could not be found')


if __name__ == "__main__":
    CreateReport().main()
