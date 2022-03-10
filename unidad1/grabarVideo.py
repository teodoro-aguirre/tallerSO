import cv2 
NOMBRE_VIDEO = 'videoSalida.avi'
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

operacionGrabar()