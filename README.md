# Tratamento de OS — Relatório de Produtividade

Script em Python que automatiza o tratamento de ordens de serviço (OS) exportadas
de um sistema de campo e gera um relatório de produtividade por técnico.

O que antes era feito manualmente no Excel (reordenar colunas, calcular tempo de
atendimento, filtrar técnicos) passou a ser feito automaticamente em segundos.

## O que o script faz

- Abre uma janela para o usuário selecionar o arquivo CSV de origem
- Lê o CSV tratando encoding e separador (padrão brasileiro)
- Seleciona e reordena as colunas relevantes para o relatório
- Converte as datas e calcula o tempo de atendimento em dias
- Filtra apenas os técnicos que compõem o relatório
- Exporta o resultado final em Excel (.xlsx)

## Problemas resolvidos

- **Encoding:** o CSV de origem vem em `latin-1`; o script trata isso na leitura
- **Separador:** as colunas são separadas por `;`, não por `,`
- **Datas como texto:** as datas vêm como texto e são convertidas para data real
  antes do cálculo, respeitando o formato brasileiro (dia/mês/ano)
- **Regras de negócio no tempo:** tempo negativo (data invertida) ou sem data
  fica em branco, e não gera número incorreto

## Como usar

1. Instale as dependências:

2. Rode o script:

4. Selecione o arquivo CSV na janela que abrir. O relatório será gerado como
   `relatorio_final.xlsx` na mesma pasta.

## Tecnologias

- Python
- pandas
- openpyxl
- tkinter (seleção de arquivo)
