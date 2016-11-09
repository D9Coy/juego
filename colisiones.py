import pygame

class COLISIONES:

	def Sprite(self, sprite,grupo_sprites, grupo_sprites2, desaparecer, funcion):
		colisiones=pygame.sprite.spritecollide(sprite,grupo_sprites2,desaparecer)
		for sprites in colisiones:
			funcion(sprite, grupo_sprites, sprites)


			
	#def Donde_Colisiono(self, sprite1, sprite2):
		#sprite1.

	
