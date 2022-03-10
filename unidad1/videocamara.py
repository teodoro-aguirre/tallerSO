# Importo la librer�a openCV
import cv2

# Esto crea un objeto para la captura
# el 0 indica la webcam de la computadora
# se puede indicar otro valor -1, 1
# indicado el puerto usb al que est� conectada
# la otra videoc�mara
capture = cv2.VideoCapture(0)

# videocamara.isOpened() devuelve True si la c�mara est� preparada
while capture.isOpened():
	# leo la imagen que está en la videoc�mara y la deposito en frame
	# res, tendr� un True en caso de que la lectura haya sido exitosa
	res, frame = capture.read()

	# cv2.imshow() despliega una imagen en una ventana
	# la ventana autom�ticamente se ajusta al tama�o de la imagen
	# El primer par�metro es un t�tulo para la ventana
	# El segundo es la imagen a ser desplegada
	# El m�todo no devuelve valor alguno
	cv2.imshow('webCam', frame)

	# Se muestra la ventana hasta que la tecla presionada sea una 's'
	if cv2.waitKey(1) == ord('s'):
		break

# libero recursos
capture.release()
# Cierro cualquier ventana cv2
cv2.destroyAllWindows()