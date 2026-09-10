import pandas as pd
from tkinter import Tk, filedialog

janela = Tk()
janela.withdraw()

caminho = filedialog.askopenfilename(
    title="Escolha o arquivo de dados",
    filetypes=[("Arquivos CSV","*.csv"),("Todos os arquivos","*.*")]
)

print("Caminho escolhido",caminho)

df = pd.read_csv(caminho,encoding="latin-1",sep=";")

tecnicos = [
    "RAFAEL HENRIQUE CONSTANTINO",
    "CLAUDINEI DE PAULA",
    "PABLO HENRIQUE BULIN TAVARES",
    "SAULO HENRIQUE DE SOUZA"
]

df = df[df["TECNICO"].isin (tecnicos)]

colunas = df[["COD_CLIENTE",
              "COD_SUPORTE",
              "DATA_ABERTURA",
              "DATA_ENCERRAMENTO",
              "TECNICO",
              "CATEGORIA",
              "ESTADO",
              "DEFEITO",
              "BAIRRO"]].copy()


colunas["MATERIAL"] =""

colunas["DATA_ABERTURA"] = pd.to_datetime(colunas["DATA_ABERTURA"],format="%d/%m/%Y",errors="coerce")
colunas["DATA_ENCERRAMENTO"] = pd.to_datetime(colunas["DATA_ENCERRAMENTO"],format="%d/%m/%Y",errors="coerce")

colunas["TEMPO"] = (colunas["DATA_ENCERRAMENTO"] - colunas["DATA_ABERTURA"]).dt.days
colunas.loc[colunas["TEMPO"] < 0, "TEMPO"] = None

colunas = colunas[[
    "COD_CLIENTE",
    "COD_SUPORTE",
    "DATA_ABERTURA",
    "DATA_ENCERRAMENTO",
    "TECNICO",
    "MATERIAL",
    "CATEGORIA",
    "ESTADO",
    "DEFEITO",
    "BAIRRO",
    "TEMPO"
]]

colunas.to_excel("relatorio_final.xlsx", index=False)
print("Pronto! Arquivo salvo como relatorio_final.xlsx")