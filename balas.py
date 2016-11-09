import pygame

class BALA(pygame.sprite.Sprite):
	def __init__(self, velocidad, posiciones, multimedia):
		pygame.sprite.Sprite.__init__(self)
		self.velocidad=velocidad
		self.posiciones=posiciones
		self.cont_posiciones=0
		self.multimedia=multimedia
		self.image = self.multimedia.getImagen("Bullets", "bullet0", "", "")
		self.rect = self.image.get_rect()
		self.rect.center = self.posiciones[0]
		self.morir=False


	def setPosicion(self, pos):
		#print "pos bala: "+str(pos)
		self.rect.x,self.rect.y=pos


	def update(self):
		if(not self.morir and self.cont_posiciones<len(self.posiciones)):
			pos=self.posiciones[self.cont_posiciones]
			self.setPosicion(pos)
			self.cont_posiciones+=self.velocidad

			


