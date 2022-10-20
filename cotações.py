import time
import requests
import pandas as pd
from datetime import datetime
import tkinter as tk
# importa a classe ttk
from tkinter import ttk


for i in range(1):
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRl,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]



janela = tk.Tk()

janela.title("Cotação de Moedas")

janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg='pink', bg='blue', width=35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")

mensagem2 = tk.Label(text="Selecione a moeda desejada")
mensagem2.grid(row=1, column=0)

# tira a caixa de entrada para colocar a lista suspensa
# moeda = tk.Entry()
# moeda.grid(row=1, column=1)



dicionario_cotacoes = {'dolar':cotacao_dolar,
                       'euro':cotacao_euro,
                       'bitcoin':cotacao_btc

}

print(dicionario_cotacoes)

# transforma o dicionário em uma lista
moedas = list(dicionario_cotacoes.keys())
print(moedas)
# para a lista moedas para a combobox que vai ficar dentro da janela
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)


def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = tk.Label(text="Cotação não encontrada")
    mensagem_cotacao.grid(row=3, column=0)
    if cotacao_moeda:
        mensagem_cotacao["text"] = f'Cotação do {moeda_preenchida} é de {cotacao_moeda} reais'


botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao)
botao.grid(row=2, column=1)

janela.mainloop()