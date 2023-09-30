import tkinter as tk
import random

# Función para deshabilitar una fila y una columna específica
def disable_row_column(row, col):
    if matrix[row][col]["enabled"]:
        matrix[row][col]["enabled"] = False
        selected_count = 0  # Reiniciar el contador de selecciones
        update_grid()

# Función para seleccionar un lugar de la matriz disponible aleatoriamente
def select_random_location():
    available_locations = [(i, j) for i in range(10) for j in range(5) if matrix[i][j]["enabled"]]
    if available_locations:
        return random.choice(available_locations)
    else:
        return None

# Función para actualizar la vista de la matriz en la GUI
def update_grid():
    for i in range(10):
        for j in range(5):
            cell = matrix[i][j]
            if cell["enabled"]:
                grid_labels[i][j].config(text=cell["content"], bg="white")
            else:
                grid_labels[i][j].config(text=cell["content"], bg="gray")

# Función para manejar la selección aleatoria
def handle_random_selection():
    global selected_count  # Usamos la variable global
    if selected_count < 5:
        random_location = select_random_location()
        if random_location:
            row, col = random_location
            grid_labels[row][col].config(bg="yellow")
            selected_count += 1

# Función para reiniciar la matriz y habilitar todas las celdas
def reset_matrix():
    global selected_count  # Usamos la variable global
    selected_count = 0  # Reiniciar el contador de selecciones
    for i in range(10):
        for j in range(5):
            matrix[i][j]["enabled"] = True
    update_grid()

# Crear una matriz de 10x5 inicialmente habilitada y con contenido vacío
matrix = [[{"enabled": True, "content": ""} for _ in range(5)] for _ in range(10)]

# Crear la ventana principal
root = tk.Tk()
root.title("Matriz Interactiva")

# Crear una matriz de etiquetas en la GUI para representar la matriz
grid_labels = [[tk.Label(root, width=5, height=2, bg="white") for _ in range(5)] for _ in range(10)]

# Colocar las etiquetas en la ventana
for i in range(10):
    for j in range(5):
        grid_labels[i][j].grid(row=i, column=j)
        grid_labels[i][j].bind("<Button-1>", lambda event, row=i, col=j: disable_row_column(row, col))

# Botón para seleccionar un lugar aleatorio
random_button = tk.Button(root, text="Seleccionar aleatoriamente", command=handle_random_selection)
random_button.grid(row=10, column=0, columnspan=5)

# Botón para reiniciar la matriz
reset_button = tk.Button(root, text="Reiniciar Matriz", command=reset_matrix)
reset_button.grid(row=11, column=0, columnspan=5)

# Inicializar el contador para el número de selecciones realizadas
selected_count = 0

# Iniciar la GUI
update_grid()
root.mainloop()
