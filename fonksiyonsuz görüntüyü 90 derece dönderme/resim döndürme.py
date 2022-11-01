# Kütüphane Ekleme
import cv2 
import numpy as np
# Görseli okuma ve ekranda gösterme

resim = cv2.imread("lena.png")
cv2.imshow("Orjinal Resim",resim)

def sagaDondur(resim):
    resimT = resim.transpose() #transpoz alma
    katman,en,boy = np.shape(resimT) # transpoz aldığımızda dizilim de katman başa geliyor
    yeniResim = np.zeros((en,boy,katman), dtype=np.uint8) #tamamı 1 matris 
    
    
    for i in range(en-1):
        for j in range(boy-1):
            for k in range(katman):
                yeniResim[i,j,k] = resimT[k,i,boy-j-1]
            
            
    cv2.imshow("SagaDonmusResim",yeniResim)

sagaDondur(resim)