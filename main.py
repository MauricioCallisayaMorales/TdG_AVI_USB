import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread
from asistente import AsistenteVoz  # Asegúrate de importar AsistenteVoz desde asistente.py
import sys

class AplicacionAsistente:
    def __init__(self, root):
        self.ventana = root
        self.ventana.title("Asistente de Voz")
        self.ventana.geometry("600x500")  # Aumenta la altura de la ventana para acomodar los botones

        self.label = tk.Label(self.ventana, text="Asistente de Voz", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.consola_texto = ScrolledText(self.ventana, height=15, width=70, wrap=tk.WORD)  # Incrementa el tamaño del campo de texto
        self.consola_texto.pack(pady=10)

        # Botones
        self.frame_botones = tk.Frame(self.ventana)
        self.frame_botones.pack(pady=10)

        self.boton_1 = tk.Button(self.frame_botones, text="Leer Texto", command=self.funcion_boton_1)
        self.boton_1.grid(row=0, column=0, padx=5, pady=5)

        self.boton_2 = tk.Button(self.frame_botones, text="Dictar Texto", command=self.funcion_boton_2)
        self.boton_2.grid(row=0, column=1, padx=5, pady=5)

        self.boton_3 = tk.Button(self.frame_botones, text="Buscar Información", command=self.funcion_boton_3)
        self.boton_3.grid(row=0, column=2, padx=5, pady=5)

        self.boton_4 = tk.Button(self.frame_botones, text="Leer Documento", command=self.funcion_boton_4)
        self.boton_4.grid(row=0, column=3, padx=5, pady=5)

        self.boton_5 = tk.Button(self.frame_botones, text="Leer Texto en Línea", command=self.funcion_boton_5)
        self.boton_5.grid(row=0, column=4, padx=5, pady=5)

        self.asistente = AsistenteVoz(self.actualizar_consola, self.cerrar)
        self.iniciar_escucha()

    def actualizar_consola(self, mensaje):
        self.consola_texto.insert(tk.END, mensaje + "\n")
        self.consola_texto.see(tk.END)

    def iniciar_escucha(self):
        Thread(target=self.asistente.activar_comandos).start()

    def cerrar(self):
        self.asistente.detener_evento.set()
        self.ventana.quit()

    # Métodos para botones
    def funcion_boton_1(self):
        print("Botón 1 presionado")

    def funcion_boton_2(self):
        print("Botón 2 presionado")

    def funcion_boton_3(self):
        print("Botón 3 presionado")

    def funcion_boton_4(self):
        print("Botón 4 presionado")

    def funcion_boton_5(self):
        print("Botón 5 presionado")

def redirect_stdout_to_tkinter(text):
    app.actualizar_consola(text)

def main():
    root = tk.Tk()
    global app
    app = AplicacionAsistente(root)
    sys.stdout.write = lambda text: redirect_stdout_to_tkinter(text)
    sys.stderr.write = lambda text: redirect_stdout_to_tkinter(text)
    root.protocol("WM_DELETE_WINDOW", app.cerrar)
    root.mainloop()

if __name__ == "__main__":
    main()
