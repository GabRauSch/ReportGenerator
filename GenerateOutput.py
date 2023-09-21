import pandas as pd
import json


class GenerateOutput:
    @staticmethod
    def parseCSV(data):
        detalhes = []
        
        for lote in data['lotes']:
            header_data = data['header']
            
            for detalhe in lote['detalhes']:
                detalhes.append([
                    header_data['empresa'],
                    header_data['inscricao'],
                    header_data['nome_banco'],
                    lote['nome_rua'],
                    lote['numero_local'],
                    lote['nome_cidade'],
                    lote['cep'],
                    lote['sigla_estado'],
                    detalhe['nome_favorecido'],
                    detalhe['data_pagamento'],
                    detalhe['valor_pagamento'],
                    detalhe['numero_documento_atribuido_empresa'],
                    lote['forma_lancamento']
                ])

        df = pd.DataFrame(detalhes)

        df.to_csv('dados.csv', index=False, sep=';')
