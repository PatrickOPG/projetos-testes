produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 =[558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,88,
7061,438508,237467,489705,328311,591120]
vendas2020=[951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,3248,
31,667179,295633,725316,644622,994303]
vendas = list(zip(vendas2019, vendas2020))

vendas_produtos = dict(zip(produtos, vendas))

lista1=list(vendas_produtos.values())
lista2=list(vendas_produtos.keys())
for chave in lista1:
    v2019,v2020=zip(*lista1)
    #zip(*lista)=desenpacotando em dois valores



print(lista2)
print(v2019)
print(v2020)









