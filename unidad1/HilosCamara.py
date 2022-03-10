from lib2to3.pgen2.token import LEFTSHIFT
import threading
import cv2
from tkinter import *
NOMBRE_VIDEO = 'videoSalida.avi'

# Definimos una función a ejecutar al clic el botón
def operacionvideocamara():
    videocamara = cv2.VideoCapture(0) 	
    while (videocamara.isOpened()):
        res, frame = videocamara.read()
        cv2.imshow('VideoCamara', frame)	
        if (cv2.waitKey(1) == ord('s')):	
            break
    videocamara.release() 
    cv2.destroyAllWindows()
        
def operacionvideo():
    global NOMBRE_VIDEO
    video = cv2.VideoCapture(NOMBRE_VIDEO)	
    while video.isOpened():
        res, frame = video.read()
        if res:
            cv2.imshow('MiVideo', frame)	
            if (cv2.waitKey(24) == ord('s')):	
                break
        else:
            break	
    video.release()
    cv2.destroyAllWindows()


def operacionGrabar():
    global NOMBRE_VIDEO
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    captura = cv2.VideoCapture(0)
    salida = cv2.VideoWriter(NOMBRE_VIDEO, fourcc, 20.0, (640, 480))
    while captura.isOpened():
        ret, imagen = captura.read()
        if ret == True:
            cv2.imshow('video', imagen)
            salida.write(imagen)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else: 
            break
    captura.release()
    salida.release()
    cv2.destroyAllWindows()

root = Tk()
root.title('Multimedia')
root.geometry("500x300") 

# Enlezamos la función a la acción del botón
btn = Button(root, text="Camara", command = operacionvideocamara).pack(side=LEFT, padx=15, pady=20)
btn = Button(root, text="Mostrar Video", command = operacionvideo).pack(side=LEFT, padx=20, pady=30)
btn = Button(root, text="Grabar", command = operacionGrabar).pack(side=LEFT, padx=30, pady=40)

root.mainloop() 