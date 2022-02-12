"""
Pontificia Universidad Javeriana
Departamento de electrónica
TG1907
Objetivo 2: Metodos de segmentación - TEST

@author: David Felipe Cuellar Diaz
"""

import os
import segMCS

directory = os.getcwd()

folderin = directory + "/"

tipo=["GRE","NIR","RGB"]

form=[".TIF",".JPG"]

imagein=["","IMG_170805_165709_0138_"]
	
image= folderin + imagein[1] + tipo[2] + form[1]
folder = folderin + "/results/"

matrix= folder + "HSV.txt"

skm=segMCS.segmentacion(image=image,folder=folder,matrix=matrix)

skm.canalrgb()

        
