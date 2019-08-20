from PIL import Image

def main():
	frase = "seguranca de redes".encode()
	arrayBinarioFrase = list(map(bin, bytearray(frase)))
	arrayBinarioFrase = [ binario[2:] for binario in arrayBinarioFrase]
	for indice, binario in enumerate(arrayBinarioFrase):
		while len(binario) < 9:
			binario = "0"+binario
		arrayBinarioFrase[indice] = binario

	img = Image.open("LAND2.BMP").convert("RGB")
	listaRGB = list(img.getdata())
	listaImagemBit = []
	for pixel in listaRGB:
		r,g,b = pixel
		listaImagemBit.append((bin(r)[2:], bin(g)[2:], bin(b)[2:]))


	print(listaImagemBit)



if __name__ == '__main__':
	main()