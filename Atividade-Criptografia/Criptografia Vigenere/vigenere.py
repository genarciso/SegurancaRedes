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
	frase = frase.lower()

	arquivoSenhas = open("senhas.txt", "r")	
	senhas = arquivoSenhas.read().replace("\n"," ").replace("?","").replace(",","").lower().split(" ")
	arquivoSenhas.close()

	arquivoResultado = open("out.txt", "w")
	for senha in senhas:
		arquivoResultado.write("-------------------"+senha+"----------")
		


		arquivoResultado.write("----------------------------------")

	print(gradeAlfabeto())



if __name__ == '__main__':
	main()