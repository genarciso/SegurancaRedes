import sys

def main(): 
	alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ?,"
	arqMensagem = open("mensagemCriptografada", "r")
	mensagemCriptografada = arqMensagem.read()
	arqMensagem.close()

	novoArqMensagem = open("mensagemDescriptografada.txt", "w")
	for contador in range(len(alfabeto)):
		novaMensagem = ""
		
		for letra in mensagemCriptografada:
			if alfabeto.find(letra) != -1:
				indice = alfabeto.find(letra)
				indice += contador
				novaMensagem += alfabeto[indice%55]
			else :
				novaMensagem += letra
		novoArqMensagem.write("----------- Mensagem " + str(contador) + " ------- \n")
		novoArqMensagem.write(str(novaMensagem) + "\n")
		novoArqMensagem.write("---------------------------------------\n")
	novoArqMensagem.close()

if __name__ == '__main__':
	main()

	