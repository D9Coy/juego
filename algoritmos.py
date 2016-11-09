class ALGORITMOS:

	def PuntoMedioPantalla(self, puntoi, puntof):
		lista=[]
		x0,y0=puntoi
		x1,y1=puntof
		dx1=x1-x0
		dy1=y1-y0

		dx=abs(dx1)
		dy=abs(dy1)
		x=x0
		y=y0
		lista.append((x,y))
		hor=dy < dx
		if (x1-x0) > 0 :
			dirx=1
		else:
			dirx=-1

		if (y1-y0) > 0 :
			diry=1
		else:
			diry=-1

		if hor:
			d= (dy*2)-dx
			de=dy*2
			dne=(dy-dx)*2
		else:
			d=(dx*2)-dy
			de=dx*2
			dne=(dx-dy)*2
		if hor:
			while x != x1:
				if d<=0:
					d=d+de
				else: 
					y=y+diry
					d=d+dne
								
				x=x+dirx
				lista.append((x,y))
		else:
			while y != y1:
				if d<=0:
					d=d+de
				else:
					x=dirx+x
					d=d+dne	
				y=y+diry
				lista.append((x,y))
		return lista

	def circuloBre(self, punto,radio, sentido):
		puntos=[]
		l1=[]#crea varias listas
		l2=[]
		l3=[]
		l4=[]
		l5=[]
		l6=[]
		l7=[]
		l8=[]
		x=radio
		y=0
		e=0
		xo,yo=punto[0]+(radio if sentido==3 else -radio),punto[1]#centro de la circunferencia aleatorios, es decir empieza aleatoriamente entre los valores de 100 y 400 para x
		puntos=[]                
		while y <= x:#
			l1.append((xo+y,yo-x))#primer pedazito
			l2.append((xo+x,yo-y))#siguientes pedazos, es decir, cada append calcula 1/8 de circunferencia
			l3.append((x+xo,yo+y))
			l4.append((xo+y,yo+x))
			l5.append((xo-y,yo+x))
			l6.append((xo-x,yo+y))
			l7.append((xo-x,yo-y))
			l8.append((xo-y,yo-x))
			e=e+2*y+1#calcular que tanto se tiene que mover al siguiente pixel, si se tiene que mover hacia un lado o hacia arriba/abajo
			y=y+1
			if 2*e > (2*x - 1):
				x=x-1
				e=e-2*x+1
		if(sentido=="-x"):
			l2.reverse()#para invertir las listas, esto se hace porque esos 4 puntos se calculan en forma inversa
			l4.reverse()
			l6.reverse()
			l8.reverse()
			puntos=l3+l4+l5+l6+l7+l8+l1+l2#concateno todas las listas resultantes en una sola
		elif(sentido=="x-"):
			l1.reverse()#para invertir las listas, esto se hace porque esos 4 puntos se calculan en forma inversa
			l3.reverse()
			l5.reverse()
			l7.reverse()
			puntos=l2+l1+l8+l7+l6+l5+l4+l3
		elif(sentido=="+x"):
			l1.reverse()#para invertir las listas, esto se hace porque esos 4 puntos se calculan en forma inversa
			l3.reverse()
			l5.reverse()
			l7.reverse()
			puntos=l6+l5+l4+l3+l2+l1+l8+l7
		elif(sentido=="x+"):
			l2.reverse()#para invertir las listas, esto se hace porque esos 4 puntos se calculan en forma inversa
			l4.reverse()
			l6.reverse()
			l8.reverse()
			puntos=l7+l8+l1++l2+l3+l4+l5+l6
		elif(sentido=="+y"):
			l2.reverse()#para invertir las listas, esto se hace porque esos 4 puntos se calculan en forma inversa
			l4.reverse()
			l6.reverse()
			l8.reverse()
			puntos=l5+l6+l7+l8+l1+l2+l3+l4
		elif(sentido=="y+"):
			l1.reverse()#para invertir las listas, esto se hace porque esos 4 puntos se calculan en forma inversa
			l3.reverse()
			l5.reverse()
			l7.reverse()
			puntos=l4+l3+l2+l1+l8+l7+l6+l5
		elif(sentido=="-y"):
			l1.reverse()#para invertir las listas, esto se hace porque esos 4 puntos se calculan en forma inversa
			l3.reverse()
			l5.reverse()
			l7.reverse()
			puntos=l8+l7+l6+l5+l4+l3+l2+l1
		elif(sentido=="y-"):
			l2.reverse()#para invertir las listas, esto se hace porque esos 4 puntos se calculan en forma inversa
			l4.reverse()
			l6.reverse()
			l8.reverse()
			puntos=l1+l2+l3+l4+l5+l6+l7+l8
				
		
		return puntos