from PIL import Image

def transformarImagemRGBBinario(imagem):
	listaImagemBit = []
	for pixel in imagem:
		r,g,b = pixel
		listaImagemBit.append((bin(r)[2:], bin(g)[2:], bin(b)[2:]))
	return listaImagemBit

def transformarFraseBinariaString(arrayBinario): 
	frase = ''.join(chr(int(letraBinaria,2)) for letraBinaria in arrayBinario)
	return frase

def main():
	# Ler imagem
	img = Image.open("out.bmp").convert("RGB")
	listaRGB = list(img.getdata())
	img.close()
	imagemBinario = transformarImagemRGBBinario(listaRGB)

	fraseBinaria = []
	# Pegar a tripla de pixeis
	sair = True
	contador = 0
	while sair: 
		parteLetra = ""
		r, g, b = imagemBinario[contador]
		contador+=1 
		parteLetra = g[-1:]+b[-1:]
		r, g, b = imagemBinario[contador]
		contador+=1 
		parteLetra += r[-1:]+g[-1:]+b[-1:]
		r, g, b = imagemBinario[contador]
		contador+=1 
		parteLetra += r[-1:]+g[-1:]+b[-1:]

		if (parteLetra == '00000011'):
			sair = False
		else :
			fraseBinaria.append(parteLetra)
	
	print(transformarFraseBinariaString(fraseBinaria))
if __name__ == '__main__':
	main()