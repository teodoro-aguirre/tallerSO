from tkinter import *
from PIL import Image
from PIL import ImageTk
import threading
import cv2
import imutils
def iniciar():
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizar()
def visualizar():
    global cap,salida 
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            salida.write(frame)
            frame = imutils.resize(frame, width=640)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)
        else:
            lblVideo.image = ""
            cap.release()
            salida.release()
def finalizar():
    global cap, salida 
    cap.release()
    salida.release()
def iniciarHilo():    
    hiloiniciar = threading.Thread(target = iniciar)
    hiloiniciar.start()
def finalizarHilo():    
    hilofinalizar = threading.Thread(target = finalizar)
    hilofinalizar.start()      
cap = None
salida = cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),24,(640,480))
root = Tk()
btnIniciar = Button(root, text="Iniciar Grabacion", width=45, command=iniciarHilo)
btnIniciar.grid(column=0, row=0, padx=5, pady=5)
btnFinalizar = Button(root, text="Finalizar Grabacion", width=45, command=finalizarHilo)
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)
lblVideo = Label(root)
lblVideo.grid(column=0, row=1, columnspan=2)  

root.mainloop()