import pygame
from pygame.locals import *
from algoritmos import ALGORITMOS


class MULTIMEDIA:
	def __init__(self):

		#ARCHIVOS MULTIMEDIA
		self.direccion_multimedia="Multimedia"

		#MUSICA
		self.direccion_musica="Musica"
		self.extencion_musica=".mp3"

		#IMAGEN
		self.direccion_imagen="Imagenes"
		self.extencion_imagen=".png"

		self.direccion_fuente="Fuentes"
		self.extencion_fuente=".ttf"

		self.direccion_mapa="Mapas"
		self.extencion_mapa=".txt"


	def getSonido(self, carpeta, sonido):
		return pygame.mixer.Sound(self.direccion_multimedia+"/"+self.direccion_musica+"/"+carpeta+"/"+sonido+self.extencion_musica)

	def getImagen(self, carpeta, imagen, sentido, indice, size=None):
		image= pygame.image.load(self.direccion_multimedia+"/"+self.direccion_imagen+"/"+carpeta+"/"+imagen+sentido+indice+self.extencion_imagen).convert_alpha()
		if size==None:
			#print "image NONE"
			return image
		return pygame.transform.scale(image, size)


	def getFuente(self, fuente, tam):
		return pygame.font.Font(self.direccion_multimedia+"/"+self.direccion_fuente+"/"+fuente+self.extencion_fuente, tam)


	def sprite_sheet(self, sheet, div=(0,0), pos=(0,0), scale=None):

		sheet_rect = sheet.get_rect()
		size=sheet.get_size()

		x,y = size[0]/div[0], size[1]/div[1]


		#print "pos: "+str((pos[0]*x, pos[1]*y))+"   tam: "+str((x, y))
		sheet.set_clip(pygame.Rect(pos[0]*x, pos[1]*y, x, y)) #find sprite you want
		sprite = sheet.subsurface(sheet.get_clip()) #grab the sprite you want 

		if scale==None:
			return sprite
				
		return pygame.transform.scale(sprite, scale)


	def archivo_texto(self, archivo, operacion="r"):
		archivo = open(self.direccion_multimedia+"/"+self.direccion_mapa+"/"+archivo+self.extencion_mapa, operacion) 
		contenido = archivo.read()
		archivo.close()
		return contenido


	def cadena_posiciones(self, cadena, ultima, pos, size, comodin):
		posiciones=[]
		
		#print "cadena: "+cadena+"  ultima: "+str(ultima)+"  comodin: "+comodin
		
		
		
		if ultima+1<len(cadena) and cadena[ultima+1]==comodin:
			#print "comodines a la derecha y son: "+str(cadena.count(comodin))
			for i in xrange(ultima, ultima+cadena.count(comodin)):
				posiciones.append([i*size[0], pos*size[1]])
				ultima=i
		elif ultima-1>=0 and cadena[ultima-1]==comodin:
			#print "comodines a la izquierda y son: "+str(cadena.count(comodin))
			for i in xrange(ultima, ultima-cadena.count(comodin), -1):
				posiciones.append([i*size[0], pos*size[1]])
				ultima=i
		elif cadena[ultima]==comodin:
			#print "no hay comodines a la izquierda y derecha"
			posiciones.append([ultima*size[0], pos*size[1]])

		#print str(posiciones)
		return ultima,posiciones


	def texto_camino(self, texto, comodin, pantalla):

		cadenas=texto.split("\n")
		alto_texto=len(cadenas)
		ancho_texto=len(cadenas[0])
		x=pantalla[0]/(ancho_texto-1)
		y=pantalla[1]/(alto_texto-1)
		posiciones=[]
		
		i=0
		ultima=0
		for cadena in cadenas:
			#print "cadena: "+cadena
			ultima,lista=self.cadena_posiciones(cadena, ultima, i, (x, y), comodin)
			posiciones+=lista
			i+=1

		return [(x,y), posiciones]


	def texto_mapa(self, texto, comodin, pantalla):
		cadenas=texto.split("\n")
		alto_texto=len(cadenas)
		ancho_texto=len(cadenas[0])
		x=pantalla[0]/ancho_texto
		y=pantalla[1]/alto_texto
		posiciones=[]

		i=0
		for cadena in cadenas:
			j=0
			for c in cadena:
				if c!=comodin:
					posiciones.append((j*x, i*y))
				j+=1
			i+=1
		return [(x,y), posiciones]



	def texto_torres(self, texto, comodin, pantalla):
		cadenas=texto.split("\n")
		alto_texto=len(cadenas)
		ancho_texto=len(cadenas[0])
		x=pantalla[0]/ancho_texto
		y=pantalla[1]/alto_texto
		posiciones=[]

		i=0
		for cadena in cadenas:
			j=0
			for c in cadena:
				if c==comodin:
					posiciones.append((j*x, i*y))
				j+=1
			i+=1
		return [(x,y), posiciones]


	def texto_comodin(self, texto, comodin, newcomodin):
		texto=texto.replace(comodin, newcomodin)
		#print texto
		return texto


	def texto_in(self, texto, texto2, comodin, newcomodin):
		print "texto1: \n"+texto+"\nfin"
		print "texto2: \n"+texto2+"\nfin"

		cadenas=texto.split("\n")
		cadenas2=texto2.split("\n")

		texto3=""
		i=0
		for cadena in cadenas2:
			j=0
			for c in cadena:
				if(c==comodin and cadenas[i][j]==cadenas2[i][j]):
					texto3+=newcomodin
				else:
					texto3+=c
				j+=1
			texto3+="\n"
			i+=1

		print "texto3: \n"+texto3+"\nfin"


	def invertir_pos(self, posiciones):
		old=posiciones
		lista=[]
		while(len(old)>0):
			pos=old.pop()
			lista.append(pos)

		return lista

	def posiciones_puntos(self, posiciones):
		lista=[]
		algoritmos=ALGORITMOS()
		for i in range(len(posiciones)-1):
			movimientos=algoritmos.PuntoMedioPantalla(posiciones[i], posiciones[i+1])
			lista+=movimientos
		return lista




	


