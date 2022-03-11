import cv2
import matplotlib.pyplot as plt



xt, yt = [], []
def Test_Picture_Analyse(filename, xt, yt):
  filename = filename
  size = (100, 100)
  thresh = 170
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
      
  xt.append(float(b))
  yt.append(float(w))

  
  plt.subplot(1, 4, 1)
  plt.title("Original")
  plt.imshow(img)
  
  plt.subplot(1, 4, 2)
  plt.title("Processed")
  plt.imshow(img_r)
  
  plt.subplot(1, 4, 3)
  plt.title("Binary Graph")
  plt.imshow(img_bw, cmap='gray')

  plt.subplot(1, 4, 4)
  plt.scatter(xt, yt, marker='X', c='black')
