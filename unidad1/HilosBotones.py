from lib2to3.pgen2.token import LEFTSHIFT
import threading, time
import cv2
from tkinter import filedialog
from tkinter import *

NOMBRE_VIDEO = 'videoSalida.avi'

# Mostrar el video grabado     
def operacionvideo(nombre, segundos):
    
    video = cv2.VideoCapture(nombre)	
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

# Iniciar grabación
def operacionGrabar(nombre, segundos):
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

VENTANA_CAMARA = 'WebCam'

def video_camara(nombre, segundos):
    global VENTANA_CAMARA
    capture = cv2.VideoCapture(0)
    while(capture.isOpened()):
        res, frame = capture.read()
        
        cv2.imshow(VENTANA_CAMARA, frame)

        if(cv2.waitKey(1) == ord('s')):
            break

    capture.release()
    cv2.destroyAllWindows()


# Iniciar grabacion con hilos
def iniciarGrabacion():
    hilo_grabar = threading.Thread(target = operacionGrabar, args = (' da ', 5))
    hilo_grabar.start()
    
def iniciarVideo():
    # global PATH_VIDEO
    root.PATH_VIDEO = filedialog.askopenfile(title="Elige una foto",
                                         filetypes=(('Archivos avi', "*.avi"), ("Archivo mp4", "*.mp4"))) 
    print(root.PATH_VIDEO)
    print(root.PATH_VIDEO.name)
    hilo_video = threading.Thread(target = operacionvideo, args=(root.PATH_VIDEO.name, 5))
    hilo_video.start()
    
def iniciarWebCam():
    hilo_webcam = threading.Thread(target = video_camara, args=('webcam', 5))
    hilo_webcam.start()  
  

# Enlezamos la función a la acción del botón
btn = Button(root, text="Camara", command = iniciarWebCam).pack(side=LEFT, padx=15, pady=20)
btn = Button(root, text="Mostrar Video", command = iniciarVideo).pack(side=LEFT, padx=20, pady=30)
btn = Button(root, text="Grabar", command = iniciarGrabacion).pack(side=LEFT, padx=30, pady=40)

root.mainloop() 