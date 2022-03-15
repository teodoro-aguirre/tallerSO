from lib2to3.pgen2.token import LEFTSHIFT
import threading, cv2
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter import Tk, Button, Label, LEFT, Toplevel
import imutils

# VARIABLES GLOBALES
NOMBRE_VIDEO = 'videoGrabado.avi'
VENTANA_CAMARA = 'VideoCamara'

# Crear interfaz
window = Tk()
window.title('Principal')
window.geometry("500x300") 

capture = None
salida = cv2.VideoWriter(NOMBRE_VIDEO,cv2.VideoWriter_fourcc(*'XVID'),24,(640,480))



# Iniciar grabación
def operacion_grabar(nombre, segundos):
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
    
# Mostrar el video grabado     
def operacion_video(nombre, segundos):
    
    video = cv2.VideoCapture(nombre)	
    while video.isOpened():
        res, frame = video.read()
        if res:
            cv2.imshow(nombre, frame)	
            if (cv2.waitKey(24) == ord('s')):	
                break
        else:
            break	
    video.release()
    cv2.destroyAllWindows()
    
# Iniciar Camara
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

def ventana_grabar():
 
    def visualizar():
        global capture,salida 
        if capture is not None:
            ret, frame = capture.read()
            if ret == True:
                salida.write(frame)
                frame = imutils.resize(frame, width=640)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)
                lbl_video.configure(image=img)
                lbl_video.image = img
                lbl_video.after(10, visualizar)
            else:
                lbl_video.image = ""
                capture.release()
                salida.release()
                
    def iniciar():
        global capture
        capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        visualizar()

    def finalizar():
        global capture, salida 
        capture.release()
        salida.release()
        
    def iniciar_hilo():    
        hiloiniciar = threading.Thread(target = iniciar)
        hiloiniciar.start()
        
    def finalizar_hilo():    
        hilofinalizar = threading.Thread(target = finalizar)
        hilofinalizar.start() 
         
    ventanagrabar = Toplevel(window)
    ventanagrabar.title('Grabar')
    lbl_video = Label(ventanagrabar)
    lbl_video.grid(column=0, row=1, columnspan=2) 
    btn_iniciar = Button(ventanagrabar, text="Iniciar", width=45, command=iniciar_hilo)
    btn_iniciar.grid(column=0, row=0, padx=5, pady=5)
    btn_finalizar = Button(ventanagrabar, text="Finalizar", width=45, command=finalizar_hilo)
    btn_finalizar.grid(column=1, row=0, padx=5, pady=5)
    
    
# Iniciar grabacion de video
def iniciar_grabacion():
    hilo_grabar = threading.Thread(target = operacion_grabar, args = (' da ', 5))
    hilo_grabar.start()

# Reproducir video mp4 o avi elegido por el usuario    
def iniciar_video():
    window.PATH_VIDEO = filedialog.askopenfile(title="Elige un video",
                                         filetypes=(('Archivos avi', "*.avi"), ("Archivo mp4", "*.mp4"))) 
    print(window.PATH_VIDEO)
    print(window.PATH_VIDEO.name)
    hilo_video = threading.Thread(target = operacion_video, args=(window.PATH_VIDEO.name, 5))
    hilo_video.start()
    
    
# Iniciar webCam
def iniciar_webcam():
    hilo_webcam = threading.Thread(target = video_camara, args=('webcam', 5))
    hilo_webcam.start() 
    
# Agregamos funcioniones al botón
button = Button(window, text="VideoCamara", command = iniciar_webcam).pack(side=LEFT, padx=15, pady=20)
button = Button(window, text="Mostrar Video", command = iniciar_video).pack(side=LEFT, padx=20, pady=30)
button = Button(window, text="Grabar", command = ventana_grabar).pack(side=LEFT, padx=30, pady=40)

window.mainloop() 
    
