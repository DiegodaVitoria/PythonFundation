nome = input("Digite o nome do paciente: ")
idade = int(input("QUal a idedade ? :"))
prioridade = "NÃO tem"

if idade >= 65:
    prioridade = "tem"
print("O paciente " + nome + " tem ", idade, "anos de idade, portanto ele " + prioridade + " prioridade ")
