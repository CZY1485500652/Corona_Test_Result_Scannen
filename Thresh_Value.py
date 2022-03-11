import cv2
import matplotlib.pyplot as plt



def Thresh_Value_Negatief(Thresh_Value):
  thresh = Thresh_Value
  size = (100, 100)
  for x in range(1, 11):
    filename = 'Train' + '/' + 'Negatief' + '/' + 'CTN-t' + str(x) + '.jpeg'
    img_o = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img_o_r = cv2.resize(img_o, size, interpolation=cv2.INTER_AREA)
    img_o_bw = cv2.threshold(img_o_r, thresh, 255, cv2.THRESH_BINARY)[1]

    plt.subplot(3, 4, x)
    plt.title(str(x))
    plt.imshow(img_o_bw, cmap='gray')


def Thresh_Value_Positief(Thresh_Value):
  thresh = Thresh_Value
  size = (100, 100)
  for x in range(1, 14):
    filename = 'Train/' + 'Positief/' + 'CTP-t' + str(x) + '.jpeg'
    img_o = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img_o_r = cv2.resize(img_o, size, interpolation=cv2.INTER_AREA)
    img_o_bw = cv2.threshold(img_o_r, thresh, 255, cv2.THRESH_BINARY)[1]

    plt.subplot(4, 4, x)
    plt.title(str(x))
    plt.imshow(img_o_bw, cmap='gray')
