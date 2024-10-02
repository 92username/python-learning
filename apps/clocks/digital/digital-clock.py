import tkinter as tk
import time

# Função para atualizar o tempo no relógio
def update_time():
    current_time = time.strftime('%H:%M:%S')  # Formato de horas
    label.config(text=current_time)  # Atualiza o texto do relógio
    label.after(1000, update_time)   # Repetir a cada 1000ms (1 segundo)

# Janela principal do Tkinter
root = tk.Tk()
root.title("Relógio Digital")
root.configure(bg='black')  # Fundo preto

# Definir o tamanho da janela (ajustável conforme preferências)
root.geometry('500x200')

# Configurar o estilo do texto do relógio
font_style = ("Digital-7", 100)  # Fonte digital grande
label = tk.Label(root, font=font_style, bg="black", fg="green")  # Fundo preto, texto verde
label.pack(anchor='center')

# Chamar a função para começar o relógio
update_time()

# Iniciar o loop da interface
root.mainloop()
