import string

def gradeAlfabeto():
	alfabeto = string.ascii_lowercase
	grid = {}
	for posicao in range(0,26):
		letraAtual = alfabeto[posicao]
		try:
			letraAnterior = alfabeto[posicao-1]
			grid[letraAtual] = grid[letraAnterior][1:] + letraAnterior
		except:
			grid[letraAtual] = alfabeto

	return grid


def main():
	frase =  "W gags domj a esgpi so eiu dm goze qnyjaaxa hikinq frmh tvkdea irvwfea eaee frmh peefoa se gvugw"
	fraseSemEspaco = frase.lower().replace(" ", "")

	arquivoSenhas = open("senhas.txt", "r")	
	
	senhas = arquivoSenhas.read().lower().replace("\n\n"," ").replace("\n"," ").replace("?","").replace(",","").replace("ç", "c").replace("é", "e").split(" ")
	senhas = set(senhas)

	arquivoSenhas.close()

	arquivoResultado = open("out.txt", "w")
	for senha in senhas:
		fraseNova = ""
		arquivoResultado.write("-------------------"+senha+"---------- \n")
		vetor = ""
		for indice in range(0, len(fraseSemEspaco)):
			vetor += senha[indice % len(senha)]

		alfabeto = string.ascii_lowercase
		grade_alfabeto = gradeAlfabeto()

		for indice, letra in enumerate(fraseSemEspaco):
			indiceLetra = grade_alfabeto[vetor[indice]].index(letra)
			fraseNova += alfabeto[indiceLetra]

		msg_final = ""
		contador = 0

		for i in range(len(frase)):
			if(frase[i] == " "):
				msg_final += " "
				continue
			elif (frase[i].isupper()):
				msg_final += fraseNova[contador].upper()
				contador += 1
			else:
				msg_final += fraseNova[contador]
				contador += 1

		arquivoResultado.write(msg_final + "\n")
		arquivoResultado.write("----------------------------------\n")



if __name__ == '__main__':
	main()