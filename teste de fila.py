
último = 10
fila = list(range(1,último+1))
while True:
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operacao = input("Operação (F, A ou S):")
    x=0
    sair=False
    while x<len(operacao):
         if operacao[x] == "A":
            if (len(fila)) > 0:
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
                break
            else:
                print("Fila vazia! Ninguém para atender.")
         elif operacao[x] == "F":
            último+=1 # Incrementa o ticket do novo cliente
            fila.append(último)
            print(fila)
            break
         elif operacao[x]== "S":
            break
            sair=True
         else:
            print("Operação inválida! Digite apenas F, A ou S!")
            break
               
    x+1
