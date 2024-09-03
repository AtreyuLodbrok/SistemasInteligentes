import random
import matplotlib.pyplot as plt
import numpy as np

class SnakesAndLadders:
    def __init__(self, size):
        self.size = size
        self.snakes = []
        self.ladders = []
        self.board = self.create_board()
        self.player_pos = 1
        self.machine_pos = 1

        # Inicializar la figura y el eje para el tablero
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.ax.set_xlim(0, self.size)
        self.ax.set_ylim(0, self.size)
        self.ax.set_xticks(np.arange(0, self.size, 1))
        self.ax.set_yticks(np.arange(0, self.size, 1))
        self.ax.grid(which='both')

    def create_board(self):
        board = {i: i for i in range(1, self.size * self.size + 1)}
        self.add_snakes_and_ladders(board)
        return board

    def add_snakes_and_ladders(self, board):
        num_snakes = random.randint(1, self.size // 2)
        num_ladders = random.randint(1, self.size // 2)

        for _ in range(num_snakes):
            start = random.randint(self.size + 1, self.size * self.size - 1)
            end = random.randint(1, start - self.size)
            board[start] = end
            self.snakes.append((start, end))

        for _ in range(num_ladders):
            start = random.randint(1, self.size * self.size - self.size - 1)
            end = random.randint(start + self.size, self.size * self.size)
            board[start] = end
            self.ladders.append((start, end))

    def draw_board(self):
        self.ax.clear()
        self.ax.set_xlim(0, self.size)
        self.ax.set_ylim(0, self.size)
        self.ax.set_xticks(np.arange(0, self.size, 1))
        self.ax.set_yticks(np.arange(0, self.size, 1))
        self.ax.grid(which='both')

        # Dibujar las celdas
        for i in range(self.size):
            for j in range(self.size):
                pos = i * self.size + (j if i % 2 == 0 else (self.size - j - 1)) + 1
                self.ax.text(j + 0.5, self.size - i - 0.5, str(pos), ha='center', va='center')

        # Dibujar serpientes
        for start, end in self.snakes:
            start_x, start_y = self.get_coordinates(start)
            end_x, end_y = self.get_coordinates(end)
            self.ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], color='red', linewidth=3)
            self.ax.text(start_x + 0.5, start_y + 0.5, 'S', color='red', ha='center', va='center')

        # Dibujar escaleras
        for start, end in self.ladders:
            start_x, start_y = self.get_coordinates(start)
            end_x, end_y = self.get_coordinates(end)
            self.ax.plot([start_x + 0.5, end_x + 0.5], [start_y + 0.5, end_y + 0.5], color='green', linewidth=3)
            self.ax.text(start_x + 0.5, start_y + 0.5, 'L', color='green', ha='center', va='center')

        # Dibujar posiciones del jugador y la máquina
        player_x, player_y = self.get_coordinates(self.player_pos)
        self.ax.text(player_x + 0.5, player_y + 0.5, 'P', color='blue', ha='center', va='center', fontsize=14, fontweight='bold')

        machine_x, machine_y = self.get_coordinates(self.machine_pos)
        self.ax.text(machine_x + 0.5, machine_y + 0.5, 'M', color='orange', ha='center', va='center', fontsize=14, fontweight='bold')

        # Actualizar la figura sin cerrarla
        plt.pause(0.5)

    def get_coordinates(self, position):
        row = (position - 1) // self.size
        col = (position - 1) % self.size
        if row % 2 == 1:
            col = self.size - 1 - col
        return col, self.size - 1 - row

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player):
        roll = self.roll_dice()
        if player == "user":
            print(f"Tiraste un {roll}.")
            self.player_pos = min(self.player_pos + roll, self.size * self.size)
            self.player_pos = self.board[self.player_pos]
            print(f"Ahora estás en la casilla {self.player_pos}.")
        else:
            print(f"La máquina tiró un {roll}.")
            self.machine_pos = min(self.machine_pos + roll, self.size * self.size)
            self.machine_pos = self.board[self.machine_pos]
            print(f"La máquina ahora está en la casilla {self.machine_pos}.")

    def check_winner(self):
        if self.player_pos == self.size * self.size:
            print("¡Felicidades! Has ganado.")
            return True
        elif self.machine_pos == self.size * self.size:
            print("La máquina ha ganado.")
            return True
        return False

    def play(self):
        print("¡Bienvenido al juego de Serpientes y Escaleras!")
        self.draw_board()  # Dibujar el tablero inicial
        while True:
            input("Presiona Enter para tu turno...")
            self.move_player("user")
            self.draw_board()
            if self.check_winner():
                break

            input("Presiona Enter para el turno de la máquina...")
            self.move_player("machine")
            self.draw_board()
            if self.check_winner():
                break

        # Mantener la ventana abierta al final
        plt.show()


# Definir el tamaño del tablero
tamaño = int(input("Introduce el tamaño del tablero (por ejemplo, 5 para un tablero de 5x5): "))
juego = SnakesAndLadders(tamaño)
juego.play()
