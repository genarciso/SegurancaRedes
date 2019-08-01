import sys

data = sys.argv[1]
arqMensagem = open(sys.argv[2], "r")
mensagem = arqMensagem.read()
arqMensagem.close()
mensagemSemEspaco = mensagem.replace(" ","")

contadorData = data.split('/')
contadorData[2] = contadorData[2][-2:]
dataJunta = "".join(contadorData)

vetorNumero = []
print(len(dataJunta))
for index, letra in enumerate(mensagemSemEspaco):
	indice = dataJunta[index%len(dataJunta)]
	vetorNumero[index] = indice

arqSalvarMensagem = open(sys.argv[3], "w")

print(vetorNumero)