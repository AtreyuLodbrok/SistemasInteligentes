import numpy as np
import matplotlib.pyplot as plt
import random
#from IPython.display import clear_output ##########esta mmda hace que se borre la salida de la 
#celda pero solo seria si lo corremos en jupyter, yo lo estuve probando en .py pero igual jala 
#
# Función para validar si el tablero es cuadrado
# Función para validar si el tablero es cuadrado
def solicitar_tamano_tablero():
    while True:
        try:
            tamano = int(input("Introduce el tamaño del tablero (debe ser un número entero positivo): "))
            if tamano <= 1:
                raise ValueError
            return tamano
        except ValueError:
            print("Error: Debes ingresar un número entero mayor a 1.")

# función para generar las serpientes y  las escaleras
#la neta use puro randin porque eso de usarlo con proba no lo entendí
#y no me dio tiempo de investigar xdd
# otra cosa es que hay que hacer en esta función o en otra, que asegure que salgan ambas
# porque cuando corri varias veces el tablero y por echo de que en la parte de abajo hace 
# la división para calcular la cant de serpientes y escaleras, en algunos solo pone 
# serpientes o escaleras xdddd
def generar_serpientes_y_escaleras(tamano):
    serpientes_escaleras = {}
    num_elementos = tamano // 2  # número de serpientes y escaleras que se colocarán en el tablero

    for _ in range(num_elementos):
        start = random.randint(1, tamano**2 - 1)
        end = random.randint(1, tamano**2 - 1)
        
        if start != end and start > end:  # una serpiente baja posiciones
            serpientes_escaleras[start] = end
        elif start != end and start < end:  # una escalera sube posiciones
            serpientes_escaleras[start] = end

    return serpientes_escaleras

# Función para mostrar el tablero usando matplotlib
def mostrar_tablero(tamano, serpientes_escaleras, jugador_pos, maquina_pos, ax):

    # Dibujar casillas
    for i in range(tamano):
        for j in range(tamano):
            num = tamano * tamano - (i * tamano + j)
            ax.text(j + 0.5, i + 0.5, str(num), ha='center', va='center', fontsize=12)

    # Dibujar serpientes y escaleras
    for key, value in serpientes_escaleras.items():
        start_x, start_y = convertir_a_coordenadas(key, tamano)
        end_x, end_y = convertir_a_coordenadas(value, tamano)
        color = 'green' if key > value else 'yellow'
        ax.plot([start_y + 0.5, end_y + 0.5], [start_x + 0.5, end_x + 0.5], color=color, lw=2)

    # Dibujar las posiciones de los jugadores
    jugador_x, jugador_y = convertir_a_coordenadas(jugador_pos, tamano)
    maquina_x, maquina_y = convertir_a_coordenadas(maquina_pos, tamano)
    ax.text(jugador_y + 0.5, jugador_x + 0.5, 'J', ha='center', va='center', fontsize=16, color='blue')
    ax.text(maquina_y + 0.5, maquina_x + 0.5, 'M', ha='center', va='center', fontsize=16, color='red')

    # Configurar ejes y mostrar
    ax.set_xticks(np.arange(0, tamano, 1))
    ax.set_yticks(np.arange(0, tamano, 1))
    ax.grid(True)
    plt.xlim(0, tamano)
    plt.ylim(0, tamano)
    plt.gca().invert_yaxis()  # el tablero empieza en la parte inferior derecha
    plt.draw()  # dibujar la figura actualizada

# función para convertir la posición a coordenadas de la matriz
def convertir_a_coordenadas(posicion, tamano):
    fila = (tamano * tamano - posicion) // tamano
    columna = (posicion - 1) % tamano
    return fila, columna

# función para lanzar el dado
def lanzar_dado():
    return random.randint(1, 6)

# función principal del juego
def jugar():
    tamano = solicitar_tamano_tablero()
    serpientes_escaleras = generar_serpientes_y_escaleras(tamano)
    jugador_pos = 1
    maquina_pos = 1

    # inicializar figura y ejes para mostrar el tablero
    fig, ax = plt.subplots(figsize=(6, 6))

    while True:
        # mostrar el tablero inicial
        mostrar_tablero(tamano, serpientes_escaleras, jugador_pos, maquina_pos, ax)
        #plt.pause(0.5)  # Pausa para ver el tablero inicial

        # turno del usuario
        input("Presiona Enter para lanzar el dado (Jugador)")
        dado = lanzar_dado()
        jugador_pos += dado
        print(f"Jugador lanzó un {dado}, nueva posición: {jugador_pos}")
        if jugador_pos in serpientes_escaleras:
            jugador_pos = serpientes_escaleras[jugador_pos]
            print(f"Jugador cayó en una serpiente o escalera. Nueva posición: {jugador_pos}")
        if jugador_pos >= tamano**2:
            print("¡El jugador ha ganado!")
            mostrar_tablero(tamano, serpientes_escaleras, jugador_pos, maquina_pos, ax)
            break

        # bostrar el tablero actualizado
        mostrar_tablero(tamano, serpientes_escaleras, jugador_pos, maquina_pos, ax)    #llamamos la función para que nos de los valres del mostrar pero lo debugue y se salta xdd
        

        #clear_output() esta weada tampoco sirvio ptm xdxdxdxdxdddddddxdxdxddd
        #plt.pause(0.5)  # Pausa para ver el tablero actualizado
        #plt.draw()  # Actualizar la figura

        # turno de la máquina
        input("Presiona Enter para lanzar el dado (Máquina)")

        dado = lanzar_dado()
        maquina_pos += dado
        print(f"Máquina lanzó un {dado}, nueva posición: {maquina_pos}")
        if maquina_pos in serpientes_escaleras:
            maquina_pos = serpientes_escaleras[maquina_pos]
            print(f"Máquina cayó en una serpiente o escalera. Nueva posición: {maquina_pos}")
        if maquina_pos >= tamano**2:
            print("¡La máquina ha ganado!")
            mostrar_tablero(tamano, serpientes_escaleras, jugador_pos, maquina_pos, ax)
            break

        # Mmstrar el tablero actualizado
        mostrar_tablero(tamano, serpientes_escaleras, jugador_pos, maquina_pos, ax)
        #plt.show()
    
    plt.show() # esta es la prinsipal pero solo imprimiria la ultima tirada 

# Ejecutar el juego
jugar()