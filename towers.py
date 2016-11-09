# -*- coding: utf-8 -*-
import pygame
import random

class TORRE(pygame.sprite.Sprite):
	def __init__(self, indice, vida, multimedia):
		pygame.sprite.Sprite.__init__(self)
		self.indice=indice
		self.vida=vida
		self.tipo=0
		self.multimedia=multimedia
		self.sheet=self.multimedia.getImagen("Towers", "towers", "", "")
		self.imagenes={}
		for x in xrange(4):
			self.imagenes[x]=self.multimedia.sprite_sheet(self.sheet, (4,1), (x, 0))
			
		self.image = self.imagenes[self.tipo]
		self.rect = self.image.get_rect()
		self.ubicada=False
		self.posicion=(0,0)
		self.rect.center = self.posicion

		self.disparar=False
		self.disparos=random.randint(2,6)
		self.cont_disparos=random.randint(30,100)
		self.cont_recargar=random.randint(200, 500)



	def setVida(self, vida):
		self.vida=vida

	def setImagen(self):
		self.image = self.imagenes[self.tipo]
		self.rect = self.image.get_rect()

	def setPosicion(self, pos):
		self.rect.move_ip(pos[0], pos[1])
		#self.rect.bottom=pos[1]
		self.posicion=pos

	def setUbicada(self, ubicada):
		self.ubicada=True

	def update(self):
		if(self.vida<10):
			self.tipo=2
		elif(self.vida<30):
			self.tipo=1
		else:
			self.tipo=0

		self.setImagen()
		self.setPosicion(self.posicion)

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





class TORRES:
	def __init__(self, numero, algoritmo, multimedia):
		self.numero=numero
		self.posiciones=algoritmo[1]
		self.size=algoritmo[0]
		self.multimedia=multimedia
		self.torres=pygame.sprite.Group()
		self.diccionario={}
		self.seleccionar=-1
		self.indice=0
		self.ubicadas=False
		self.seleccionada=False

		for x in xrange(self.numero):
			self.diccionario[x]=TORRE(x, 100, self.multimedia)
			

	def setPosicion(self, pos):
		if(self.seleccionar!=-1):
			if(pos in self.posiciones):
				self.diccionario[self.seleccionar].setPosicion(pos)
				self.diccionario[self.seleccionar].setUbicada(True)
				self.torres.add(self.diccionario[self.seleccionar])
			else:
				self.diccionario[self.seleccionar].setUbicada(False)
				
		self.seleccionar=-1


	

	def seleccionarPosicion(self, pos):
		if pos in self.posiciones:
			print "entro"
			if not self.seleccionada:
				for t in self.torres:
					if t.ubicada and t.rect.x==pos[0] and t.rect.y==pos[1]:
						self.seleccionar=t.indice
						print "seleccionando torre ya ubicada indice: "+str(self.seleccionar)
						self.seleccionada=True
				if not self.seleccionada:
					self.ubicar(pos, self.indice)
					self.indice+=1
					self.seleccionada=False
					self.seleccionar=-1
			else:
				for t in self.torres:
					if t.ubicada and t.rect.x==pos[0] and t.rect.y==pos[1]:
						self.seleccionada=False
						self.seleccionar=-1
				if self.seleccionada:
					print "reubicando torre seleccionada: "+str(self.seleccionar)
					self.ubicar(pos, self.seleccionar)
					self.seleccionada=False
					self.seleccionar=-1


		

	def isUbicadas(self):
		for torre in self.diccionario:
			if not self.diccionario[torre].ubicada:
				return False
		return True

	def ubicar(self, pos, indice):
		if(self.indice<self.numero):
			self.seleccionar=indice
			#print "ubicando torre: "+str(self.seleccionar)+"   en pos: "+str(pos)
			self.setPosicion(pos)

	def update(self):
		for t in self.torres:
			t.update()

	def getTorre(self, indice):
		if indice in self.diccionario:
			return self.diccionario[indice]
		else:
			return self.diccionario[0]

	def dibujar(self, screen):
		#for t in self.torres:
		#print "torre: "+str(t.indice)+"  ubicada en: "+str((t.rect.x, t.rect.y))
		self.torres.draw(screen)




