class Item(pygame.sprite.Sprite):
	def __init__(self, coordenadas, item, multimedia):
		pygame.sprite.Sprite.__init__(self)
		self.image = multimedia.getImagen("items", item, "", "")
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