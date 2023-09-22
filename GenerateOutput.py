import csv

class GenerateOutput:
    @staticmethod
    def parseCSV(data):
        with open('dados.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')

            for item in data:
                header = item['header']
                
                empresa = header['empresa']
                inscricao = header['inscricao']
                nome_banco = header['nome_banco']
                nome_rua = header['nome_rua']
                numero_local = header['numero_local']
                nome_cidade = header['nome_cidade']
                cep = header['cep']
                sigla_estado = header['sigla_estado']

                writer.writerow(['Nome da Empresa', 'Numero de Inscricao da Empresa', 'Nome do Banco', 'Nome da Rua', 'Numero do Local', 'Nome da Cidade', 'CEP', 'Sigla do Estado'])
                writer.writerow([empresa, inscricao, nome_banco, nome_rua, numero_local, nome_cidade, cep, sigla_estado])
                writer.writerow(["Nome do Favorecido","Data do Pagamento","Valor do Pagamento","Número do Documento Atribuído pela Empresa","Forma de Lançamento"])

                for detail in item['details']:
                    nome_favorecido = detail['nome_favorecido']
                    data_pagamento = detail['data_pagamento']
                    valor_pagamento = detail['valor_pagamento']
                    numero_documento_atribuido_empresa = detail['numero_documento_atribuido_empresa']
                    forma_lancamento = detail['forma_lancamento']
                    
                    writer.writerow([nome_favorecido,data_pagamento,valor_pagamento,numero_documento_atribuido_empresa,forma_lancamento])
