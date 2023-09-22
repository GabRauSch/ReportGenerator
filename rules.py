campos = {
    'tipo_registro': 7,
    'nome_rua': slice(142, 172),
    'empresa': slice(72,102),
    'inscricao': slice(18,32),   
    'nome_banco': slice(102,132),  
    'numero_local': slice(172,177),    
    'nome_cidade': slice(192,212), 
    'cep_inicial': slice(212,217), 
    'cep_complemento': slice(217,220), 
    'sigla_estado': slice(220,222),    
    'nome_favorecido': slice(43,73), 
    'date': slice(93,101),    
    'valor_original': slice(119,134),  
    'numero_documento_atribuido_empresa': slice(73,93),
    'index_forma_lancamento': slice(11,13)
}

header = ['empresa', 'inscricao', 'nome_banco', 'nome_rua', 'numero_local', 'nome_cidade', 'cep', 'sigla_estado']
header_field_names = ['Nome da Empresa', 'Numero de Inscricao da Empresa', 'Nome do Banco', 'Nome da Rua', 'Numero do Local', 'Nome da Cidade', 'CEP', 'Sigla do Estado']

details = ['nome_favorecido', 'data_pagamento', 'valor_pagamento', 'numero_documento_atribuido_empresa', 'forma_lancamento']
details_field_names = ["Nome do Favorecido","Data do Pagamento","Valor do Pagamento","Número do Documento Atribuído pela Empresa","Forma de Lançamento"]

forma_lancamento = [
 'Crédito em Conta Corrente',
 'Cheque Pagamento / Administrativo',
 'DOC/TED (1) (2)',
 'Cartão Salário (somente para Tipo de Serviço\'30\')',
 'Crédito em Conta Poupança',
 'Liberação de Títulos HSBC',
 'Emissão de Cheque Salário',
 'Liquidação de Parcelas de Cobrança Não Registrada 09Arrecadação de Tributos Federais',
 'OP à Disposição',
 'Pagamento de Contas e Tributos com Código de Barras',
 'Doc Mesma Titularidade',
 'Pagamentos de Guias',
 'Credito em Conta Corrente Mesma Titularidade',
 'Tributo - DARF Normal',
 'Tributo GPS (Guia da Previdência Social)',
 'Tributo - DARF Simples',
 'Tributo - IPTU - Prefeituras',
 'Pagamento com Autenticação',
 'Tributo - DARJ'
]

