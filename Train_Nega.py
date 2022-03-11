import matplotlib.pyplot as plt


xn, yn = [], []

def Train_Negatief(xn, yn):
  
  size = (100, 100)
  thresh = 150

  print("__________________________________________________________")
  print("                          Train Negatief file             ")
 
  while True:
    
    for f in range(1, 11):
      filename = "Train" + "/" +"Negatief" + "/" + "CTN-t" + str(f) + ".jpeg"
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
      
      xn.append(float(b))
      yn.append(float(w))
  
      print(str(filename) + " B -->" + str(w) + " , W --> " + str(b))
    break
  print()
  print("Train Negatief file 0% --> |====================|> 100%")
  print("__________________________________________________________")
  
  print() 
  print()
  #plt.imshow(img_bw, cmap='gray')
