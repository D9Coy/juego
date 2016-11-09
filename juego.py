# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------------------------------------------------------------------------
#librerias externas
#------------------------------------------------------------------------------------------------------------------------------------------------
import os
import sys
import pygame
from pygame.locals import *
import time
import random


#------------------------------------------------------------------------------------------------------------------------------------------------
#Librerias internas
#------------------------------------------------------------------------------------------------------------------------------------------------
from multimedia import MULTIMEDIA
from menu import MENU
from zombiez import ZOMBIEZ
from mapa import MAPA
from towers import TORRES
from balas import BALA
from algoritmos import ALGORITMOS
from colisiones import COLISIONES
#------------------------------------------------------------------------------------------------------------------------------------------------



class JUEGO:

	def __init__(self):
		self.ANCHO = 1200
		self.ALTO = 600
		self.multimedia=MULTIMEDIA()

		self.salirjuego = False
		self.iniciarjuego=False
		self.iniciarcreditos=False
		self.nuevojuego=False
		self.mostraropciones=False
		self.mostrarmenuinicio=False
		self.mostrarmenupausa=False
		self.ubicartorres=False

		self.opciones_inicio = [
		("Jugar", self.comenzar_nuevo_juego), 
		("Opciones", self.mostrar_opciones), 
		("Creditos", self.creditos), 
		("Salir", self.salir_del_programa)
		]

		self.opciones_pausa = [
		("Continuar", self.continuar_juego), 
		("Nuevo Juego", self.comenzar_nuevo_juego),
		("Opciones", self.mostrar_opciones), 
		("Creditos", self.creditos), 
		("Salir", self.salir_del_programa)
		]


		
		
		pygame.font.init()
		self.screen = pygame.display.set_mode((self.ANCHO, self.ALTO))
		self.reloj = pygame.time.Clock()

		self.run()


	def resetOpciones(self):
		self.salirjuego = False
		self.iniciarjuego=False
		self.iniciarcreditos=False
		self.nuevojuego=False
		self.mostraropciones=False
		self.mostrarmenuinicio=False
		self.mostrarmenupausa=False
		self.ubicartorres=False

	def continuar_juego(self):
		self.resetOpciones()
		self.iniciarjuego=True
		

	def comenzar_nuevo_juego(self):
		self.resetOpciones()
		self.nuevojuego=True

	def mostrar_opciones(self):
		self.resetOpciones()
		self.mostraropciones=True

	def creditos(self):
		self.resetOpciones()
		self.iniciarcreditos=True

	def mostrar_menu_pausa(self):
		self.resetOpciones()
		self.mostrarmenupausa=True

	def mostrar_menu_inicio(self):
		self.resetOpciones()
		self.mostrarmenuinicio=True

	def ubicar_torres(self):
		self.resetOpciones()
		self.ubicartorres=True

	def salir_del_programa(self):
		import sys
		sys.exit(0)


	def MostrarOpciones(self):
		pass

	def IniciarCreditos(self):
		pass

	def iniciar_nuevo_juego(self):
		self.resetOpciones()
		self.ubicartorres=True
		self.fondo = self.multimedia.getImagen("Fondos", "fondo", "", "1", (self.ANCHO, self.ALTO))
		self.mapa=MAPA(self.multimedia.texto_mapa(self.multimedia.archivo_texto("mapa"), "x", (self.ANCHO, self.ALTO)), self.multimedia)
		self.torres=TORRES(3, self.multimedia.texto_torres(self.multimedia.archivo_texto("mapa"), "t", (self.ANCHO, self.ALTO)), self.multimedia)
		self.zombiez=ZOMBIEZ(10, self.multimedia, (self.ANCHO, self.ALTO))
		self.balas_zombiez=pygame.sprite.Group()
		self.balas_torres=pygame.sprite.Group()
		self.algoritmos=ALGORITMOS()
		self.colisiones=COLISIONES()


	def ubicar_torres(self):
		self.resetOpciones()
		self.ubicartorres=True

	def UbicarTOrres(self):
		self.mapa.dibujar(self.screen)
		self.torres.update()
		self.torres.dibujar(self.screen)




	def iniciar_juego(self):
		pass

	def impactar(self, sprite1, grupo1, sprite2):
		sprite2.setVida(sprite2.vida-1)
		grupo1.remove(sprite1)




	def Update(self):

		self.fondo = self.multimedia.getImagen("Fondos", "fondo", "", "1", (self.ANCHO, self.ALTO))

		self.mapa.dibujar(self.screen)
		self.torres.update()
		self.torres.dibujar(self.screen)
		self.zombiez.update()
		self.zombiez.dibujar(self.screen)
		for z in self.zombiez.zombiez:
			if z.disparar:
				if z.vida<=0:
					self.zombiez.zombiez.remove(z)
				else:
					torre=self.torres.getTorre(random.randint(0, self.torres.numero-1))
					self.balas_zombiez.add(BALA(3, self.algoritmos.PuntoMedioPantalla(z.rect.center, torre.rect.center), self.multimedia))
					z.disparar=False

		for t in self.torres.torres:
			if t.vida<=0:
				self.torres.torres.remove(t)
			else:
				if t.disparar:
					zombie=self.zombiez.getZombie(random.randint(0, self.torres.numero-1))
					self.balas_torres.add(BALA(5, self.algoritmos.PuntoMedioPantalla(t.rect.center, zombie.rect.center), self.multimedia))
					t.disparar=False
				
		for b in self.balas_zombiez:
			b.update()
			self.colisiones.Sprite(b, self.balas_zombiez, self.torres.torres, False, self.impactar)

		for b in self.balas_torres:
			b.update()
			self.colisiones.Sprite(b, self.balas_torres, self.zombiez.zombiez, False, self.impactar)

		self.balas_zombiez.draw(self.screen)
		self.balas_torres.draw(self.screen)

		


	def run(self):
		
		self.menu_inicio = MENU(self.opciones_inicio, [(255,0,0), ((255,255,255))], self.multimedia)
		self.menu_pausa= MENU(self.opciones_pausa, [(255,0,0), ((255,255,255))], self.multimedia)

		self.mostrarmenuinicio=True
		

		self.fondo = self.multimedia.getImagen("Fondos", "fondo_menu", "", "0", (self.ANCHO, self.ALTO))
		
		

		#self.multimedia.texto_comodin(self.multimedia.archivo_texto("mapa0"), "p", " ")

		while not self.salirjuego:

			self.screen.blit(self.fondo, (0, 0))
			


			tecla = pygame.key.get_pressed()
			for e in pygame.event.get():
				if e.type == QUIT:
					self.resetOpciones()
					self.salirjuego=True
				if tecla[pygame.K_ESCAPE] and not self.mostrarmenuinicio:
					self.mostrar_menu_pausa()
				
				if self.ubicartorres and tecla[pygame.K_KP_ENTER] and self.torres.isUbicadas():
					self.resetOpciones()
					self.iniciarjuego=True
				

				if(self.ubicartorres and pygame.mouse.get_pressed()[0]):
					mouse_pos=pygame.mouse.get_pos()
					mouse_pos=mouse_pos[0]/self.mapa.size[0],mouse_pos[1]/self.mapa.size[1]
					mouse_pos=mouse_pos[0]*self.mapa.size[0],mouse_pos[1]*self.mapa.size[1]
					self.torres.seleccionarPosicion(mouse_pos)

					


			if(self.ubicartorres):
				self.UbicarTOrres()
			
			if(self.mostrarmenuinicio):
				self.fondo = self.multimedia.getImagen("Fondos", "fondo_menu", "", "0", (self.ANCHO, self.ALTO))
				self.fondo = pygame.transform.scale(self.fondo, (self.ANCHO, self.ALTO))
				self.menu_inicio.actualizar()
				self.menu_inicio.imprimir(self.screen)

			if(self.mostrarmenupausa):
				self.fondo = self.multimedia.getImagen("Fondos", "fondo_menu", "", "0", (self.ANCHO, self.ALTO))
				self.fondo = pygame.transform.scale(self.fondo, (self.ANCHO, self.ALTO))
				self.menu_pausa.actualizar()
				self.menu_pausa.imprimir(self.screen)

			if(self.iniciarjuego):
				#print "runing"
				self.Update()

			if(self.mostraropciones):
				#print "runing opciones"
				self.MostrarOpciones()

			if(self.iniciarcreditos):
				#print "runing creditos"
				self.IniciarCreditos()

			if(self.nuevojuego):
				#print "runing nuevo juego"
				self.iniciar_nuevo_juego()
				

			pygame.display.flip()
			self.reloj.tick(60)

		pygame.quit()


juego=JUEGO()
juego.run()
