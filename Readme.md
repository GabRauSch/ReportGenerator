# Gerador relatorio bancário

Este gerador de relatório tem como objetivo transcrever para CSV os dados trazidos de um arquivo modelo, seguindo a documentação desse.

## Utilizando

```cmd
py main.py NOME_ARQUIVO_DADOS.txt NOME_DESTINO
```

Você pode alterar "NOME_ARQUIVOS_DADOS.txt" para o nome de sua preferencia, porém o programa lerá apenas .txt
Você pode alterar NOME_DESTINO para o nome de sua preferencia


## Logica do programa

Este programa segue a leitura das regras da documentação da NEXXERA no arquivo de avaliação de candidatos.
Estas regras estão descritas em rules.py, com a tabela de posição de caractéres e regras do G029 necessario para esse teste

O programa foi feito desta maneira para facilitar a escalabilidade e adição de novos elementos no documento.
