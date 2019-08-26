from PIL import Image

def tranformarFraseBinario(frase):
	arrayBinarioFrase = list(map(bin, bytearray(frase)))
	arrayBinarioFrase = [ binario[2:] for binario in arrayBinarioFrase]
	for indice, binario in enumerate(arrayBinarioFrase):
		while len(binario) < 9:
			binario = "0"+binario
		arrayBinarioFrase[indice] = binario
	return arrayBinarioFrase

def transformarImagemRGBBinario(imagem):
	listaImagemBit = []
	for pixel in imagem:
		r,g,b = pixel
		listaImagemBit.append((bin(r)[2:], bin(g)[2:], bin(b)[2:]))
	return listaImagemBit

def transformarBinarioImagemRGB(listaRGB):
	listaImagem = []
	for binario in listaRGB:
		r,g,b = binario
		listaImagem.append((int(r,2), int(g,2), int(b,2)))
	return listaImagem

def main():
	frase = "ola amigo, tudo bem?".encode()
	fraseBinario = tranformarFraseBinario(frase)

	img = Image.open("LAND2.BMP").convert("RGB")
	listaRGB = list(img.getdata())
	img.close()
	imagemBinario = transformarImagemRGBBinario(listaRGB)

	for indiceLetra, letraBinario in enumerate(fraseBinario):
		contadorPixel = 0
		# Escrita na primeira tripla 
		r, g, b = imagemBinario[indiceLetra*3]
		r = r[:-1] + letraBinario[contadorPixel]
		contadorPixel+=1 
		g = g[:-1] + letraBinario[contadorPixel]
		contadorPixel+=1
		b = b[:-1] + letraBinario[contadorPixel]
		contadorPixel+=1
		imagemBinario[indiceLetra*3] = (r,g,b)

		#Escrita na segunda tripla
		r, g, b = imagemBinario[(indiceLetra*3) + 1]
		r = r[:-1] + letraBinario[contadorPixel]
		contadorPixel+=1
		g = g[:-1] + letraBinario[contadorPixel]
		contadorPixel+=1
		b = b[:-1] + letraBinario[contadorPixel]
		contadorPixel+=1
		imagemBinario[(indiceLetra*3) + 1] = (r,g,b)

		# Escrita da terceira tripla
		r, g, b = imagemBinario[(indiceLetra*3) + 2]
		r = r[:-1] + letraBinario[contadorPixel]
		contadorPixel+=1
		g = g[:-1] + letraBinario[contadorPixel]
		contadorPixel+=1
		b = b[:-1] + letraBinario[contadorPixel]

		imagemBinario[(indiceLetra*3) + 2] = (r,g,b)

	indiceLetra = len(fraseBinario)
	r, g, b = imagemBinario[indiceLetra*3]
	r = r[:-1] + '0' 
	g = g[:-1] + '0'
	b = b[:-1] + '0'
	imagemBinario[indiceLetra*3] = (r,g,b)

	r, g, b = imagemBinario[(indiceLetra*3) + 1]
	r = r[:-1] + '0'
	g = g[:-1] + '0'
	b = b[:-1] + '0'
	imagemBinario[(indiceLetra*3) + 1] = (r,g,b)

	r, g, b = imagemBinario[(indiceLetra*3) + 2]
	r = r[:-1] + '0'
	g = g[:-1] + '1'
	b = b[:-1] + '1'

	imagemBinario[(indiceLetra*3) + 2] = (r,g,b)	

	imagemBinario = transformarBinarioImagemRGB(imagemBinario)
	img = Image.new("RGB", (1024,768))
	img.putdata(imagemBinario)
	img.save('out.bmp',
    	format = 'BMP',
        quality = 100)
	img.close()
	
if __name__ == '__main__':
	main()