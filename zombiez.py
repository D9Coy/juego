# -*- coding: utf-8 -*-
import pygame
import random
from algoritmos import ALGORITMOS

class ZOMBIE(pygame.sprite.Sprite):
	def __init__(self, tipo, algoritmo, vida, velocidad, multimedia, salida):
		pygame.sprite.Sprite.__init__(self)
		self.camino=algoritmo[1]
		self.size=algoritmo[0]
		self.tipo=tipo
		self.tipos = { 0:[0,0], 1:[3,0], 2:[6,0], 3:[0,4], 4:[3,4], 5:[6,4] }
		self.cont_camino=0
		self.max_camino=3
		self.salida=salida
		#print "camino: "+str(self.camino)
		self.camino=multimedia.invertir_pos(self.camino)
		#print "camino invertido: "+str(self.camino)
		self.vida=vida
		self.velocidad=velocidad
		self.multimedia=multimedia
		self.algoritmos=ALGORITMOS()

		self.aceleracion=1
		self.movimientos=self.multimedia.posiciones_puntos(self.camino)
		self.cont_movimientos=0

		self.cambio_x = 0
		self.cambio_y = 0

		self.max_caminar=0
		self.cont_cambio=0
		self.max_cambio=10
		#self.sentidos=["abajo","derecha","arriba","izquierda"]
		#self.sentidos=["arriba","derecha","izquierda", "abajo"]
		self.sentidos=["abajo","izquierda","derecha","arriba"]
		self.sentido="izquierda"
		self.accion="caminar"
		

		self.cont_caminar=0
		self.max_caminar=3
		self.caminar= {}
		
		#self.sheet=self.multimedia.getImagen("Zombiez", "7ZombieSpriteSheet", "", "")
		self.sheet=self.multimedia.getImagen("Zombiez", "ZombieSheet", "", "")


		cont_i=self.tipos[self.tipo][1]
		for s in self.sentidos:
			cont_j=self.tipos[self.tipo][0]
			for i in range(self.max_caminar):
				#print "caminar["+s+str(i)+"] = "+str((cont_j, cont_i))			
				self.caminar[s+str(i)]= self.multimedia.sprite_sheet(self.sheet, (12,8), (cont_j, cont_i), self.size)
				cont_j+=1
			cont_i+=1

		self.posicion=self.movimientos[0]
		self.image = self.caminar[self.sentido+str(self.cont_caminar)]
		self.ancho,self.alto=self.dimension=self.image.get_size()
		self.rect=self.image.get_rect()
		self.rect.x,self.rect.y=self.posicion

		self.disparar=False
		self.disparos=random.randint(2,6)
		self.cont_disparos=random.randint(30,100)
		self.cont_recargar=random.randint(200, 500)
		

	def setPosicion(self, posicion):
		self.rect.x,self.rect.y=self.posicion=posicion

	def setVida(self, vida):
		self.vida=vida


	def setImagen(self):
		if self.cont_cambio<self.max_cambio:
			self.cont_cambio+=1
		else:
			if self.cont_caminar<self.max_caminar-1:
				self.cont_caminar+=1
			else:
				self.cont_caminar=0
			self.cont_cambio=0

		self.image = self.caminar[self.sentido+str(self.cont_caminar)]
		self.ancho,self.alto=self.dimension=self.image.get_size()
		self.rect=self.image.get_rect()
		
		

	def setMover(self, movimientos):
		self.movimientos=movimientos


	def mover(self):
		nuevo_mov=self.movimientos[self.cont_movimientos]
		#print "nuevo_mov: "+str(nuevo_mov)
		self.cambio_x, self.cambio_y = nuevo_mov[0]-self.posicion[0], nuevo_mov[1]-self.posicion[1]

		if self.cambio_x>0:
			self.sentido="derecha"
		if self.cambio_x<0:
			self.sentido="izquierda"
		if self.cambio_y>0:
			self.sentido="abajo"
		if self.cambio_y<0:
			self.sentido="arriba"

		self.setImagen()
		self.setPosicion(nuevo_mov)
		


	def update(self):
		if(self.salida<=0):
			if(self.cont_movimientos<len(self.movimientos)):
				self.mover()
				self.cont_movimientos+=self.velocidad
				self.cont_camino=self.max_camino

				if not self.disparar:
					if self.cont_disparos>0:
						self.cont_disparos-=1
					else:
						if self.disparos>0:
							self.disparos-=1
							self.disparar=True
							self.cont_disparos=random.randint(30,100)
						else:
							if self.cont_recargar>0:
								self.cont_recargar-=1
							else:
								self.cont_recargar=random.randint(200, 500)
								self.disparos=random.randint(2,6)
		else:
			self.salida-=1


		

class ZOMBIEZ:
	"""docstring for ZOMBIEZ"""
	def __init__(self, numero, multimedia, screen_dimension):
		self.numero = numero
		self.multimedia=multimedia
		self.zombiez=pygame.sprite.Group()
		self.diccionario={}
		for i in range(numero):
			texto=self.multimedia.archivo_texto("mapa"+str(random.randint(0,8)))
			texto=self.multimedia.texto_comodin(texto, "p", " ")
			self.diccionario[i]=ZOMBIE(random.randint(0,5), self.multimedia.texto_camino(texto, "x", screen_dimension), 5, random.randint(1,2), self.multimedia, random.randint(21, 59)*i)
			#mapa=self.multimedia.archivo_texto("mapa")
			#mapa=self.multimedia.texto_comodin(mapa, "p", " ")
			#self.multimedia.texto_in(texto, mapa, "x", "O")
			self.zombiez.add(self.diccionario[i])


	def getZombie(self, indice):
		if indice in self.diccionario:
			return self.diccionario[indice]
		else:
			return self.diccionario[0]

	def update(self):
		for zombie in self.zombiez:
			zombie.update()

	def dibujar(self, screen):
		self.zombiez.draw(screen)


			


			


