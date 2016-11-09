# coding: utf-8
#------------------------------------------------------------------------------------------------------------------------------------------------
############################################################## LABERINTO ##############################################################
#------------------------------------------------------------------------------------------------------------------------------------------------
#Librerias
import os
import sys
import pygame
from pygame.locals import *
import time
import random
#------------------------------------------------------------------------------------------------------------------------------------------------
ANCHO = 800
ALTO = 640
#------------------------------------------------------------------------------------------------------------------------------------------------
class Mapa(pygame.sprite.Sprite):
	def __init__(self, archivo, multimedia):
		pygame.sprite.Sprite.__init__(self)
		self.image = self.multimedia.getImagen("mapas", "bloque", "", 0)
		self.rect= self.image.get_rect()
		self.mapa = leerMapa(archivo)
		self.fila = len(self.mapa)
		self.columna = len(self.mapa[0])

	def dibujar(self, pantalla):
		for f in range(self.fila):
			for c in range(self.columna):
				if self.mapa[f][c] == 1:
					pantalla.blit(self.bloque, (self.rect_bloque.w*c, self.rect_bloque.h*f))
#------------------------------------------------------------------------------------------------------------------------------------------------
# Quita el ultimo caracter de una lista.
def quitarUltimo(lista):
	for i in range(len(lista)):
		lista[i] = lista[i][:-1]
	return lista
#------------------------------------------------------------------------------------------------------------------------------------------------
# Covierte una cadena en una lista.
def listarCadena(cadena):
	lista = []
		for i in range(len(cadena)):
			if cadena[i] == ".":
				lista.append(0)
			if cadena[i] == "#":
				lista.append(1)
	return lista
#------------------------------------------------------------------------------------------------------------------------------------------------
# Lee un archivo de texto y lo convierte en una lista.
def leerMapa(archivo):
	mapa = open(archivo, "r")
	mapa = mapa.readlines()
	mapa = quitarUltimo(mapa)
	for i in range(len(mapa)):
		mapa[i] = listarCadena(mapa[i])
	return mapa
#------------------------------------------------------------------------------------------------------------------------------------------------

class Personaje(pygame.sprite.Sprite):
	

	def __init__( self ):
		pygame.sprite.Sprite.__init__( self , multimedia)
		self.cambio_x = 0
		self.cambio_y = 0
		self.nivel = None
		self.max_caminar=0
		self.multimedia=multimedia
		self.caminar_derecha = {}
		
		for i in range(0, self.max_caminar):
			self.caminar_derecha[i]= self.

		self.PersonajeIzquierda = {}
		self.PersonajeIzquierda[0] = pygame.image.load('Personaje/Izquierda/1.png').convert_alpha()
		self.PersonajeIzquierda[1] = pygame.image.load('Personaje/Izquierda/2.png').convert_alpha()
		self.PersonajeIzquierda[2] = pygame.image.load('Personaje/Izquierda/3.png').convert_alpha()
		self.PersonajeIzquierda[3] = pygame.image.load('Personaje/Izquierda/4.png').convert_alpha()

		self.PersonajeArriba = {}
		self.PersonajeArriba[0] = pygame.image.load('Personaje/Arriba/1.png').convert_alpha()
		self.PersonajeArriba[1] = pygame.image.load('Personaje/Arriba/2.png').convert_alpha()
		self.PersonajeArriba[2] = pygame.image.load('Personaje/Arriba/3.png').convert_alpha()
		self.PersonajeArriba[3] = pygame.image.load('Personaje/Arriba/4.png').convert_alpha()

		self.PersonajeAbajo = {}
		self.PersonajeAbajo[0] = pygame.image.load('Personaje/Abajo/1.png').convert_alpha()
		self.PersonajeAbajo[1] = pygame.image.load('Personaje/Abajo/2.png').convert_alpha()
		self.PersonajeAbajo[2] = pygame.image.load('Personaje/Abajo/3.png').convert_alpha()
		self.PersonajeAbajo[3] = pygame.image.load('Personaje/Abajo/4.png').convert_alpha()

		self.cual = 0
		self.cuanto = 100
		self.tiempo = 0
		self.horizontal = False
		self.derecha = False
		self.izquierda = False
		self.arriba = False
		self.abajo = False
		self.ObtenerDibujoPersonaje()
		self.rect = self.image.get_rect()

	def ObtenerDibujoPersonaje(self):
		if self.horizontal == True:
		   if self.derecha == True:
			  self.image=self.PersonajeDerecha[self.cual]
		   if self.derecha == False:
			  self.image=self.PersonajeIzquierda[self.cual]
		if self.horizontal == False:
		   if self.arriba == True:
			  self.image=self.PersonajeArriba[self.cual]
		   if self.arriba == False:
			  self.image=self.PersonajeAbajo[self.cual]

	def update(self):
		if self.cual > 3:
		   self.cual = 0
		self.ObtenerDibujoPersonaje()
		self.rect.x += self.cambio_x
		self.rect.y += self.cambio_y

	def AvanzarArriba(self):
		self.cambio_y = -2

	def AvanzarAbajo(self):
		self.cambio_y = +2

	def AvanzarIzquierda(self):
		self.cambio_x = -2

	def AvanzarDerecha(self):
		self.cambio_x = +2

	def Detenerse(self):
		self.cambio_x = 0
		self.cambio_y = 0
#------------------------------------------------------------------------------------------------------------------------------------------------
class SkullN1(pygame.sprite.Sprite):
	def __init__(self, coordenadas, imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Skull.png")
		self.rect = self.image.get_rect()
		self.rect.center = coordenadas
		self.actualizacion = pygame.time.get_ticks()
		self.maximo = self.rect.bottom+5
		self.minimo = self.rect.top-5
		self.dy = 1

	def update(self):
		if self.actualizacion + 40 < pygame.time.get_ticks():
		   self.rect.move_ip(0,self.dy)
		   if self.rect.bottom > self.maximo or self.rect.top < self.minimo:
			  self.dy = -self.dy
		   self.actualizacion= pygame.time.get_ticks()

class SkullPantalla(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ListaSkull = pygame.sprite.Group()
		self.Skull = pygame.image.load("Skull.png")
		self.transparente = self.Skull.get_at((0,0))
		self.Skull.set_colorkey(self.transparente)
		posicionskull = [[545, 580]]

		for recorrido in posicionskull:
			skull = SkullN1((recorrido[0],recorrido[1]), self.Skull)
			self.ListaSkull.add(skull)

	def update(self):
		self.ListaSkull.update()

	def draw(self, pantalla):
		self.ListaSkull.draw(pantalla)
#------------------------------------------------------------------------------------------------------------------------------------------------
class PicaN1(pygame.sprite.Sprite):
	def __init__(self, coordenadas, imagen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Pica.png")
		self.rect = self.image.get_rect()
		self.rect.center = coordenadas
		self.actualizacion = pygame.time.get_ticks()
		self.maximo = self.rect.bottom+5
		self.minimo = self.rect.top-5
		self.dy = 1

	def update(self):
		if self.actualizacion + 40 < pygame.time.get_ticks():
		   self.rect.move_ip(0,self.dy)
		   if self.rect.bottom > self.maximo or self.rect.top < self.minimo:
			  self.dy = -self.dy
		   self.actualizacion= pygame.time.get_ticks()

class PicaPantalla(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ListaPica = pygame.sprite.Group()
		self.Pica = pygame.image.load("Pica.png")
		self.transparente = self.Pica.get_at((0,0))
		self.Pica.set_colorkey(self.transparente)
		posicionpica = [[735, 480]]

		for recorrido in posicionpica:
			pica = PicaN1((recorrido[0],recorrido[1]), self.Pica)
			self.ListaPica.add(pica)

	def update(self):
		self.ListaPica.update()

	def draw(self, pantalla):
		self.ListaPica.draw(pantalla)
#------------------------------------------------------------------------------------------------------------------------------------------------
class Zombie1(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
		pygame.sprite.Sprite.__init__(self)

		self.Zombie1Derecha = {}
		self.Zombie1Derecha[0] = pygame.image.load('Zombie1/Derecha/1.png').convert_alpha()
		self.Zombie1Derecha[1] = pygame.image.load('Zombie1/Derecha/2.png').convert_alpha()
		self.Zombie1Derecha[2] = pygame.image.load('Zombie1/Derecha/3.png').convert_alpha()
		self.Zombie1Derecha[3] = pygame.image.load('Zombie1/Derecha/4.png').convert_alpha()
		self.Zombie1Derecha[4] = pygame.image.load('Zombie1/Derecha/5.png').convert_alpha()
		self.Zombie1Derecha[5] = pygame.image.load('Zombie1/Derecha/6.png').convert_alpha()
		self.Zombie1Derecha[6] = pygame.image.load('Zombie1/Derecha/7.png').convert_alpha()
		self.Zombie1Derecha[7] = pygame.image.load('Zombie1/Derecha/8.png').convert_alpha()

		self.Zombie1Izquierda = {}
		self.Zombie1Izquierda[0] = pygame.image.load('Zombie1/Izquierda/1.png').convert_alpha()
		self.Zombie1Izquierda[1] = pygame.image.load('Zombie1/Izquierda/2.png').convert_alpha()
		self.Zombie1Izquierda[2] = pygame.image.load('Zombie1/Izquierda/3.png').convert_alpha()
		self.Zombie1Izquierda[3] = pygame.image.load('Zombie1/Izquierda/4.png').convert_alpha()
		self.Zombie1Izquierda[4] = pygame.image.load('Zombie1/Izquierda/5.png').convert_alpha()
		self.Zombie1Izquierda[5] = pygame.image.load('Zombie1/Izquierda/6.png').convert_alpha()
		self.Zombie1Izquierda[6] = pygame.image.load('Zombie1/Izquierda/7.png').convert_alpha()
		self.Zombie1Izquierda[7] = pygame.image.load('Zombie1/Izquierda/8.png').convert_alpha()

		self.actualizacion = pygame.time.get_ticks()
		self.cual = 0
		self.izquierda = False
		self.obtenerDibujo()
		self.rect = self.image.get_rect()
		self.rect.topleft = (posX, posY)
		self.dx = 1

	def obtenerDibujo(self):
		if self.izquierda:
		   self.image=self.Zombie1Izquierda[self.cual]
		else:
		   self.image=self.Zombie1Derecha[self.cual]

	def update(self):
		if self.actualizacion + 100 < pygame.time.get_ticks():
		   self.cual += 1
		   if self.cual > 7:
			  self.cual = 0
		   self.obtenerDibujo()
		   self.actualizacion= pygame.time.get_ticks()

		if self.rect.right > 768:
		   self.izquierda = True
		if self.rect.left < 448:
		   self.izquierda = False

		if self.izquierda == True:
		   self.rect.move_ip(-self.dx,0)
		else:
		   self.rect.move_ip(self.dx,0)

class Zombie1N1(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ListaZombie1 = pygame.sprite.Group()

		posicionzombie1 = [[624, 31]]
		for recorrido in posicionzombie1:
			zombie1 = Zombie1(recorrido[0],recorrido[1])
			self.ListaZombie1.add(zombie1)

	def update(self):
		self.ListaZombie1.update()

	def draw(self, pantalla):
		self.ListaZombie1.draw(pantalla)
#------------------------------------------------------------------------------------------------------------------------------------------------
class Zombie2(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
		pygame.sprite.Sprite.__init__(self)

		self.Zombie2Arriba = {}
		self.Zombie2Arriba[0] = pygame.image.load('Zombie2/Arriba/1.png').convert_alpha()
		self.Zombie2Arriba[1] = pygame.image.load('Zombie2/Arriba/2.png').convert_alpha()
		self.Zombie2Arriba[2] = pygame.image.load('Zombie2/Arriba/3.png').convert_alpha()

		self.Zombie2Abajo = {}
		self.Zombie2Abajo[0] = pygame.image.load('Zombie2/Abajo/1.png').convert_alpha()
		self.Zombie2Abajo[1] = pygame.image.load('Zombie2/Abajo/2.png').convert_alpha()
		self.Zombie2Abajo[2] = pygame.image.load('Zombie2/Abajo/3.png').convert_alpha()

		self.actualizacion = pygame.time.get_ticks()
		self.cual = 0
		self.abajo = False
		self.obtenerDibujo()
		self.rect = self.image.get_rect()
		self.rect.topleft = (posX, posY)
		self.dy = 1

	def obtenerDibujo(self):
		if self.abajo:
		   self.image=self.Zombie2Abajo[self.cual]
		else:
		   self.image=self.Zombie2Arriba[self.cual]

	def update(self):
		if self.actualizacion + 100 < pygame.time.get_ticks():
		   self.cual += 1
		   if self.cual > 2:
			  self.cual = 0
		   self.obtenerDibujo()
		   self.actualizacion= pygame.time.get_ticks()

		if self.rect.top < 224:
		   self.abajo = True
		if self.rect.bottom > 480:
		   self.abajo = False

		if self.abajo == True:
		   self.rect.move_ip(0,self.dy)
		else:
		   self.rect.move_ip(0,-self.dy)

class Zombie2N1(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ListaZombie2 = pygame.sprite.Group()

		posicionzombie2 = [[134, 352]]
		for recorrido in posicionzombie2:
			zombie2 = Zombie2(recorrido[0],recorrido[1])
			self.ListaZombie2.add(zombie2)

	def update(self):
		self.ListaZombie2.update()

	def draw(self, pantalla):
		self.ListaZombie2.draw(pantalla)
#------------------------------------------------------------------------------------------------------------------------------------------------
#INICIALIZACION DE VARIABLES
pygame.init()
#------------------------------------------------------------------------------------------------------------------------------------------------
#COLORES
blanco = (255,255,255)
negro = (0,0,0)
amarillo = (255,255,0)
dorado = (231,174,24)
azulclaro = (0,255,255)
violeta = (204,0,102)
rojo = (255,0,0)
rojooscuro = (190,17,17)
verde = (0,255,0)
azul = (0,0,255)
morado = (153,51,255)
naranja = (255,128,0)
gris = (128,128,128)
#------------------------------------------------------------------------------------------------------------------------------------------------
#DIMENSIONES DE LA VENTANA
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("LABERINTO")
#------------------------------------------------------------------------------------------------------------------------------------------------
#PERSONAJE NIVEL 1
personaje = Personaje()
#------------------------------------------------------------------------------------------------------------------------------------------------
#VARIABLES DE JUEGO
salir = False
reloj = pygame.time.Clock()
#------------------------------------------------------------------------------------------------------------------------------------------------
#################################################### FUNCION PRINCIPAL DE INICIO DEL JUEGO ####################################################
#------------------------------------------------------------------------------------------------------------------------------------------------
def Nivel1():
	#IMAGEN DE FONDO NIVEL 1
	Fondo=pygame.image.load("Fondo.jpg").convert_alpha()
	mapa = Mapa("mapa.txt")
	#PERSONAJE
	PersonajeGrupo = pygame.sprite.RenderUpdates(personaje)
	personaje.rect.x = 32
	personaje.rect.y = 32
	ListaSpritesActivos = pygame.sprite.Group()
	ListaSpritesActivos.add(personaje)
	#CREACION DE SKULL
	GrupoSkull = []
	GrupoSkull.append(SkullPantalla())
	DibujoSkull = GrupoSkull[0]
	personaje.posicionskull = DibujoSkull
	#CREACION DE PICA
	GrupoPica = []
	GrupoPica.append(PicaPantalla())
	DibujoPica = GrupoPica[0]
	personaje.posicionpica = DibujoPica
	#CREACION DE ZOMBIE 1
	GrupoZombie1 = []
	GrupoZombie1.append(Zombie1N1())
	DibujoZombie1 = GrupoZombie1[0]
	personaje.posicionzombie1 = DibujoZombie1
	#CREACION DE ZOMBIE 2
	GrupoZombie2 = []
	GrupoZombie2.append(Zombie2N1())
	DibujoZombie2 = GrupoZombie2[0]
	personaje.posicionzombie2 = DibujoZombie2
#------------------------------------------------------------------------------------------------------------------------------------------------
	salir = False
	global event
	while salir != True:
	   reloj.tick(60)
	   tecla = pygame.key.get_pressed()
	   for event in pygame.event.get():
		   if event.type == pygame.QUIT:
			  sys.exit()
		   if tecla[pygame.K_ESCAPE]:
			  sys.exit()
#------------------------------------------------------------------------------------------------------------------------------------------------
	   if event.type == pygame.KEYDOWN:

		  if tecla[pygame.K_RIGHT]:
			 personaje.horizontal = True
			 personaje.derecha = True
			 if pygame.time.get_ticks()-personaje.tiempo > personaje.cuanto:
				personaje.tiempo = pygame.time.get_ticks()
				personaje.cual +=1
			 personaje.AvanzarDerecha()

		  if tecla[pygame.K_LEFT]:
			 personaje.horizontal = True
			 personaje.derecha = False
			 if pygame.time.get_ticks()-personaje.tiempo > personaje.cuanto:
				personaje.tiempo = pygame.time.get_ticks()
				personaje.cual +=1
			 personaje.AvanzarIzquierda()

		  if tecla[pygame.K_UP]:
			 personaje.horizontal = False
			 personaje.arriba = True
			 if pygame.time.get_ticks()-personaje.tiempo > personaje.cuanto:
				personaje.tiempo = pygame.time.get_ticks()
				personaje.cual +=1
			 personaje.AvanzarArriba()

		  if tecla[pygame.K_DOWN]:
			 personaje.horizontal = False
			 personaje.arriba = False
			 if pygame.time.get_ticks()-personaje.tiempo > personaje.cuanto:
				personaje.tiempo = pygame.time.get_ticks()
				personaje.cual +=1
			 personaje.AvanzarAbajo()
#------------------------------------------------------------------------------------------------------------------------------------------------
	   if event.type == pygame.KEYUP:
		  personaje.cual = 0

		  if tecla[pygame.K_UP]:
			 personaje.Detenerse()

		  if tecla[pygame.K_DOWN]:
			 personaje.Detenerse()

		  if tecla[pygame.K_LEFT]:
			 personaje.Detenerse()

		  if tecla[pygame.K_RIGHT]:
			 personaje.Detenerse()
#------------------------------------------------------------------------------------------------------------------------------------------------
	   ColisionSkull = pygame.sprite.spritecollide(personaje, personaje.posicionskull.ListaSkull, False)
	   for skull in ColisionSkull:
		  print "+1 Skull"
		  skull.kill()
#------------------------------------------------------------------------------------------------------------------------------------------------
	   ColisionPica = pygame.sprite.spritecollide(personaje, personaje.posicionpica.ListaPica, False)
	   for pica in ColisionPica:
		  print "+1 Pica"
		  pica.kill()
#------------------------------------------------------------------------------------------------------------------------------------------------
	   ColisionPersonajeZombie1 = pygame.sprite.spritecollide(personaje, personaje.posicionzombie1.ListaZombie1, False)
	   for zombie1 in ColisionPersonajeZombie1:
		   personaje.kill()
#------------------------------------------------------------------------------------------------------------------------------------------------
	   ColisionPersonajeZombie2 = pygame.sprite.spritecollide(personaje, personaje.posicionzombie2.ListaZombie2, False)
	   for zombie2 in ColisionPersonajeZombie2:
		   personaje.kill()
#------------------------------------------------------------------------------------------------------------------------------------------------
	   pantalla.blit(Fondo,(0,0))
	   mapa.dibujar(pantalla)

	   if personaje.rect.right > ANCHO-32:
		  personaje.rect.right = ANCHO-32
	   if personaje.rect.left < 32:
		  personaje.rect.left = 32
	   if personaje.rect.top < 32:
		  personaje.rect.top = 32
	   if personaje.rect.bottom > ALTO-32:
		  personaje.rect.bottom = ALTO-32

	   ListaSpritesActivos.update()
	   ListaSpritesActivos.draw(pantalla)
	   DibujoSkull.update()
	   DibujoSkull.draw(pantalla)
	   DibujoPica.update()
	   DibujoPica.draw(pantalla)
	   DibujoZombie1.update()
	   DibujoZombie1.draw(pantalla)
	   DibujoZombie2.update()
	   DibujoZombie2.draw(pantalla)
	   pygame.display.update()
#------------------------------------------------------------------------------------------------------------------------------------------------
while salir != True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
		   salir = True
		else:
		   Nivel1()
	pygame.display.flip()
pygame.quit()

