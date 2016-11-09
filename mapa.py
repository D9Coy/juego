# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class PARED(pygame.sprite.Sprite):
	def __init__(self, pos, size,  multimedia):
		pygame.sprite.Sprite.__init__(self)
		self.multimedia=multimedia
		self.image = self.multimedia.getImagen("Mapas", "pared", "", "0", size)
		self.rect= self.image.get_rect()
		self.rect.x,self.rect.y=pos


class MAPA:
	def __init__(self, algoritmo, multimedia):
		self.paredes = pygame.sprite.Group()
		self.posiciones=algoritmo[1]
		self.size=algoritmo[0]
		self.multimedia=multimedia

		for pos in self.posiciones:
			#print "posicion: "+str(pos)+" tamaño: "+str(posiciones[0])
			self.paredes.add(PARED(pos, self.size, self.multimedia))


	def dibujar(self, pantalla):
		self.paredes.draw(pantalla)

	def getParedes(self):
		return self.paredes