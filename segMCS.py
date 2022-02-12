"""
Pontificia Universidad Javeriana
Departamento de electrónica
TG1907
Objetivo 2: Segmentación Multi-color space threshold

@author: David Felipe Cuellar Diaz
"""

#Basado en: https://realpython.com/python-opencv-color-spaces/
import cv2
import numpy as np

#Se inicia la clase segmentación
class segmentacion:

    #definición de funciones
    def __init__(self,image="image.jpg",folder="",scalefactor=1,resize=False,matrix="",onlymask=False):        
        self.image=image
        self.folder=folder
        self.scalefactor=scalefactor
        self.resize=resize
        self.matrix=matrix
        self.onlymask=onlymask
        
    def nothing(self,x):
        pass
    
    # función para máscara en RGB
    def canalrgb(self):
        
	# carga la imagen
        imagein = cv2.imread(self.image)

	# cambia el tamaño de la imagen si es necesario
        if self.resize == True:
            height, width = imagein.shape[:2]
            imagein = cv2.resize(imagein,(int(self.scalefactor*width), int(self.scalefactor*height)), interpolation = cv2.INTER_NEAREST)
        
	# crea una copia de la imagen
        imagecopy=imagein.copy()
        
        cv2.imshow("input", imagein)
        
        # aplica un filtro mediana a la imagen de entrada
        median = cv2.medianBlur(imagein, 5)
	
	# convierte la imagen con filtro mediana en espacio de color HSV
        hsv_median= cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
        
        cv2.namedWindow('output')

        # crea las barras para cambiar el color
        cv2.createTrackbar('HM','output',0,255,self.nothing)
        cv2.createTrackbar('SM','output',0,255,self.nothing)
        cv2.createTrackbar('VM','output',0,255,self.nothing)
        cv2.createTrackbar('Hm','output',0,255,self.nothing)
        cv2.createTrackbar('Sm','output',0,255,self.nothing)
        cv2.createTrackbar('Vm','output',0,255,self.nothing)
        
	# define los valores de cada barra
        cv2.setTrackbarPos('HM','output',80)
        cv2.setTrackbarPos('SM','output',255)
        cv2.setTrackbarPos('VM','output',255)
        cv2.setTrackbarPos('Hm','output',30)
        cv2.setTrackbarPos('Sm','output',60)
        cv2.setTrackbarPos('Vm','output',60)
        

        print("Presione la letra q para guardar y salir")
        
        while True:        

            k = cv2.waitKey(1) & 0xFF
            if k == ord('q'):
                break
        
            # toma los valores definidos para cada barra
            HM = cv2.getTrackbarPos('HM','output')
            SM = cv2.getTrackbarPos('SM','output')
            VM = cv2.getTrackbarPos('VM','output')
            Hm = cv2.getTrackbarPos('Hm','output')
            Sm = cv2.getTrackbarPos('Sm','output')
            Vm = cv2.getTrackbarPos('Vm','output')
        
	    # define los valores máximo y mínimo de umbralización
            min_green = (Hm,Sm,Vm)
            max_green = (HM,SM,VM)
            
	    # crea la máscara en la imagen con filtro mediana en HSV,
	    # dependiendo de los valores de umbralización
            mask = cv2.inRange(hsv_median, min_green, max_green)

	    # realiza una operación entre la imagen original y la máscara
            resultmask = cv2.bitwise_and(imagein, imagein, mask=mask)

            cv2.imshow("mask", mask)
            cv2.imshow("output", resultmask)
	    
            # invierte la máscara y realiza la operación de nuevo entre
            # la imagen original y la máscara invertida
            mask2 = cv2.bitwise_not(mask)
            resultmask2 = cv2.bitwise_and(imagein, imagein, mask=mask2)

            cv2.imshow("mask2", mask2)
            cv2.imshow("output2", resultmask2)
        
	# Guarda todas las imágenes
        if self.onlymask == False :
            print("Usted tiene onlymask = False, en el folder se guardó: ")
            print(" - imagecopy.bmp")
            print(" - mask.bmp")
            print(" - result.bmp")
            print(" - mask2.bmp")
            print(" - result.bmp")
            print(" - HSV.txt")
            
            arr=np.array([[HM,SM,VM,Hm,Sm,Vm]])
            np.savetxt(self.matrix,arr,delimiter=',',fmt='%f')
                    
            cv2.imwrite(self.folder + "imagecopy.bmp",imagecopy) 
    
            cv2.imwrite(self.folder + "mask.bmp",mask)
            cv2.imwrite(self.folder + "result.bmp",resultmask)
            
            cv2.imwrite(self.folder + "mask2.bmp",mask2)
            cv2.imwrite(self.folder + "result2.bmp",resultmask2)        
        
	# Guarda sólo la máscara   
        else:
            print("Usted tiene onlymask = True, en el folder se guardó: ")
            print(" - mask.bmp")
            
            cv2.imwrite(self.folder + "mask.bmp",mask)

        
        cv2.destroyAllWindows()
    
    # Función para máscara en un sólo canal de color   
    def canalir(self):
        
	# carga la imagen
        imagein = cv2.imread(self.image)

	# cambia el tamaño de la imagen si es necesario
        if self.resize == True:
            height, width = imagein.shape[:2]
            imagein = cv2.resize(imagein,(int(self.scalefactor*width), int(self.scalefactor*height)), interpolation = cv2.INTER_NEAREST)

	# crea una copia de la imagen                
        imagecopy=imagein.copy()
        
        cv2.imshow("input", imagein)
        
        # aplica un filtro mediana a la imagen de entrada
        median = cv2.medianBlur(imagein, 5)

	# convierte la imagen con filtro mediana en espacio de color HSV
        hsv_median= cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
        
        cv2.namedWindow('output')
        
	# crea las barras para cambiar el color
        cv2.createTrackbar('VM','output',0,255,self.nothing)
        cv2.createTrackbar('Vm','output',0,255,self.nothing)
        
	# define los valores de cada barra
        cv2.setTrackbarPos('VM','output',255)
        cv2.setTrackbarPos('Vm','output',60)
         
        print("Presione la letra q para guardar y salir")
        
        while True:        

            k = cv2.waitKey(1) & 0xFF
            if k == ord('q'):
                break
        
            # toma los valores definidos para cada barra
            VM = cv2.getTrackbarPos('VM','output')
            Vm = cv2.getTrackbarPos('Vm','output')
        
            # define los valores máximo y mínimo de umbralización
            min_green = (0,0,Vm)
            max_green = (0,0,VM)
            
	    # crea la máscara en la imagen con filtro mediana en HSV,
	    # dependiendo de los valores de umbralización
            mask = cv2.inRange(hsv_median, min_green, max_green)

	    # realiza una operación entre la imagen original y la máscara
            resultmask = cv2.bitwise_and(imagein, imagein, mask=mask)

            cv2.imshow("mask", mask)
            cv2.imshow("output", resultmask)

            # invierte la máscara y realiza la operación de nuevo entre
            # la imagen original y la máscara invertida
            mask2 = cv2.bitwise_not(mask)
            resultmask2 = cv2.bitwise_and(imagein, imagein, mask=mask2)

            cv2.imshow("mask2", mask2)
            cv2.imshow("output2", resultmask2)
        
	# Guarda todas las imágenes
        if self.onlymask == False :
            print("Usted tiene onlymask = False, en el folder se guardó: ")
            print(" - imagecopy.bmp")
            print(" - mask.bmp")
            print(" - result.bmp")
            print(" - mask2.bmp")
            print(" - result.bmp")
            print(" - HSV.txt")
            
            arr=np.array([[0,0,VM,0,0,Vm]])
            np.savetxt(self.matrix,arr,delimiter=',',fmt='%f')
                    
            cv2.imwrite(self.folder + "imagecopy.bmp",imagecopy) 
    
            cv2.imwrite(self.folder + "mask.bmp",mask)
            cv2.imwrite(self.folder + "result.bmp",resultmask)
            
            cv2.imwrite(self.folder + "mask2.bmp",mask2)
            cv2.imwrite(self.folder + "result2.bmp",resultmask2)        

	# Guarda sólo la máscara            
        else:
            print("Usted tiene onlymask = True, en el folder se guardó: ")
            print(" - mask.bmp")
            cv2.imwrite(self.folder + "mask.bmp",mask)
        
        cv2.destroyAllWindows()
