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
        print("porq esse demonho ta sendo execurdp ´prraqeopjasdfjklhs")
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

    def get_file_header_info(self, line):
        empresa = line[72:102].strip()
        inscricao = line[18:32].strip()
        cnpj_formatado = "{0}.{1}.{2}/{3}-{4}".format(
            inscricao[:2],
            inscricao[2:5],
            inscricao[5:8],
            inscricao[8:12],
            inscricao[12:]
        )
        nome_banco = line[102:132].strip()

        self.empresa = empresa
        self.inscricao = cnpj_formatado
        self.nome_banco = nome_banco

    def get_batch_header_info(self, line):
        nome_rua = line[142:172].strip()
        numero_local = line[172:177].strip()
        nome_cidade = line[192:212].strip()
        
        cep_inicial = line[212:217].strip()
        cep_complemento = line[217:220].strip()
        cep = f"{cep_inicial}-{cep_complemento}"

        sigla_estado = line[220:222].strip()
        
        index_forma_lancamento = int(line[11:13].strip()) -1
        forma_lancamento = rules.forma_lancamento[index_forma_lancamento]
                

        self.create_new_object()

        print(self.empresa)

        self.information[self.current_index]['header']["empresa"] = self.empresa
        self.information[self.current_index]['header']["inscricao"] = self.inscricao
        self.information[self.current_index]['header']["nome_banco"] = self.nome_banco
        self.information[self.current_index]['header']["nome_rua"] = nome_rua
        self.information[self.current_index]['header']["numero_local"] = numero_local
        self.information[self.current_index]['header']["nome_cidade"] = nome_cidade
        self.information[self.current_index]['header']["cep"] = cep
        self.information[self.current_index]['header']["sigla_estado"] = sigla_estado
        self.forma_lancamento = forma_lancamento

    def get_details_info(self, line):
        nome_favorecido = line[43:73].strip()
        
        date = line[93:101].strip()
        data_pagamento = datetime.strptime(date, "%d%m%Y").strftime("%d/%m/%Y")
        
        valor_original = line[119:134].strip()
        valor_reais = locale.format_string('%0.2f', int(valor_original) / 100, grouping=True)
        valor_pagamento = f'R$ {valor_reais}'

        numero_documento_atribuido_empresa = line[73:93].strip()

        forma_lancamento = self.forma_lancamento

        data ={
            'nome_favorecido': nome_favorecido,
            'data_pagamento': data_pagamento,
            'valor_pagamento': valor_pagamento,
            'numero_documento_atribuido_empresa': numero_documento_atribuido_empresa,
            'forma_lancamento': forma_lancamento
        }
        
        self.information[self.current_index]["details"].append(data)

    def get_batch_trailer_info(self, line):
        print('this is a trailer')

    def get_file_trailer_info(self, line):
        print('this is a file trailer')

    def main(self):
        try:
            with open(self.nome_arquivo, 'r', encoding='utf-8') as file:
                for line in file:
                    register_type = int(line[rules.campos['tipo_registro']])
                    if register_type == 0:
                        self.get_file_header_info(line)
                    elif register_type == 1:
                        print(line) 
                        self.get_batch_header_info(line)
                    elif register_type == 3:
                        self.get_details_info(line)
                    elif register_type == 5:
                        self.get_batch_trailer_info(line)
                    elif register_type == 9:
                        self.get_file_trailer_info(line)

            GenerateOutput.parseCSV(self.information)
        except FileNotFoundError:
            print('File could not be found')


if __name__ == "__main__":
    CreateReport().main()
