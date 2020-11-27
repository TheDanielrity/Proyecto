from random import randrange

def tablero_inicial(tablero):
    for fila in range(len(tablero)):
        print("+"+"-------+"*3)
        print("|"+"       |"*3, end="\n|")
        for columna in range(len(tablero)):
            print("   "+str(tablero[fila][columna])+"   |", end="")
        print("\n|"+"       |"*3)

    print("+"+"-------+"*3)

def movimiento_casilla(tablero):
	continuar = False	
	while not continuar:
		ficha_movida = input("Ingresa tu movimiento: ")
		continuar = len(ficha_movida) == 1 and ficha_movida >= '1' and ficha_movida <= '9' 
		if not continuar:
			print("Movimiento erróneo, ingrésalo nuevamente") 
			continue
		ficha_movida = int(ficha_movida) - 1 	
		fila = ficha_movida // 3 	
		columna = ficha_movida % 3		
		posicion = tablero[fila][columna]	
		continuar = posicion not in ['O','X'] 
		if not continuar:	
			print("¡Campo ocupado, ingresa nuevamente!")
			continue
	tablero[fila][columna] = 'O'
	print("🡣  Tu casilla utilizada.")


def casillas_libres(tablero):
	libre = []	
	for fila in range(3): 
		for columna in range(3): 
			if tablero[fila][columna] not in ['O','X']: 
				libre.append((fila,columna)) 
	return libre


def ganador(tablero, posicion):
	if posicion == "X":	
		quien_es = 'maquina'	
	elif posicion == "O": 
		quien_es = 'yo'	
	else:
		quien_es = None	
	diagonal1 = diagonal2 = True 
	for rc in range(3):
		if tablero[rc][0] == posicion and tablero[rc][1] == posicion and tablero[rc][2] == posicion:	
			return quien_es
		if tablero[0][rc] == posicion and tablero[1][rc] == posicion and tablero[2][rc] == posicion: 
			return quien_es
		if tablero[rc][rc] != posicion: 
			diagonal1 = False
		if tablero[2 - rc][2 - rc] != posicion: 
			diagonal2 = False
	if diagonal1 or diagonal2:
		return quien_es
	return None

def dibuja_movimiento(tablero):
	libre = casillas_libres(tablero) 
	conteo = len(libre)
	if conteo > 0:	
		random = randrange(conteo)
		fila, columna = libre[random]
		tablero[fila][columna] = 'X'

tablero = [ [3 * columna + fila + 1 for fila in range(3)] for columna in range(3) ] 
tablero[1][1] = 'X' 
libre = casillas_libres(tablero)
tu_nombre = input("Ingresa tu nombre: ")
mi_turno = True 
while len(libre):
	tablero_inicial(tablero)
	if mi_turno:
		movimiento_casilla(tablero)
		victoria = ganador(tablero,'O')

	else:
		print("🡣  Casilla utilizada de la máquina.")	
		dibuja_movimiento(tablero)
		victoria = ganador(tablero,'X')
	if victoria != None:
		break
	mi_turno = not mi_turno		
	libre = casillas_libres(tablero)

tablero_inicial(tablero)
if victoria == 'yo':
	print("¡Has ganado "+ tu_nombre +"!")
elif victoria == 'maquina':
	print("¡La computadora te ha ganado!")
else:
	print("¡Ha ocurrido un Empate!")
