# -*- coding: cp1252 -*-
import cv2 # Importo la librería openCV

capture = cv2.VideoCapture(0) 	# Esto crea un objeto para la captura
									# el 0 indica la webcam de la computadora
									# se puede indicar otro valor -1, 1
									# indicado el puerto usb al que está conectada
									# la otra videocámara

while (capture.isOpened()):		# videocamara.isOpened() devuelve True si la cámara está preparada
	
	res, frame = capture.read()	# leo la imagen que está en la videocámara y la deposito en frame
									# res, tendrá un True en caso de que la lectura haya sido exitosa
 
	cv2.imshow('webCam', frame)	# cv2.imshow() despliega una imagen en una ventana
										# la ventana automáticamente se ajusta al tamaño de la imagen
										# El primer parámetro es un título para la ventana
										# El segundo es la imagen a ser desplegada
										# El método no devuelve valor alguno

	if (cv2.waitKey(1) == ord('s')):	# Se muestra la ventana hasta que la tecla presionada sea una 's'
		break
 	
capture.release() # libero recursos
cv2.destroyAllWindows() # Cierro cualquier ventana cv2