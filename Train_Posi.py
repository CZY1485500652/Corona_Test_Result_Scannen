import cv2
import matplotlib.pyplot as plt


xp, yp = [], []

def Train_Positief(xp, yp):
  
  size = (100, 100)
  thresh = 180

  print("__________________________________________________________")
  print("                     Train Positief")
  while True:
    
    for f in range(1, 13):
      filename = "Train" + "/" +"Positief" + "/" + "CTP-t" + str(f) + ".jpeg"
      img = cv2.imread(filename)
      img_o = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
      img_r = cv2.resize(img_o, size, interpolation = cv2.INTER_AREA)
      img_bw = cv2.threshold(img_r, thresh, 255, cv2.THRESH_BINARY)[1]
      
      b = 0
      w = 0
      
      for x in range(100):
        for y in range(100):
          if img_bw[x, y] == 255:
            w += 1
            
      w = int(w) / 100000 * 100
      b = 100 - float(w)
      
      xp.append(float(b))
      yp.append(float(w))
  
      print(str(filename) + " B -->" + str(w) + " , W --> " + str(b))
    break
  print() 
  print("Train Positief file 0% --> |====================|> 100%")
  print("__________________________________________________________")
  print()
  print()
  #plt.imshow(img_bw, cmap='gray')
