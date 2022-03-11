from Train_Nega import Train_Negatief
from Train_Posi import Train_Positief
from Thresh_Value import Thresh_Value_Negatief
from Thresh_Value import Thresh_Value_Positief
from Test_Picture_Analyse import Test_Picture_Analyse
from Machine_Learning import SVM
from Machine_Learning import KNN




xn, yn = [], []
xp, yp = [], []
xt, yt = [], []


Train_Negatief(xn, yn)
print()
Train_Positief(xp, yp)


#Thresh_Value_Negatief(150)
#Thresh_Value_Positief(180)


'''
filename = input("Enter the name of file : ")
Test_Picture_Analyse(filename, xt, yt)
SVM(xn, yn, xp, yp, xt, yt, filename)
#KNN(xn, yn, xp, yp, xt, yt, filename, 1)
'''

'''
SVM_R = 26
KNN_R = 19
print()
print("==========================================================")
for x in range(1, 16):
  result = 'Negatief'
  filename = 'Test/' + 'Negatief/' + 'CTN-' + str(x) + '.jpg'
  Test_Picture_Analyse(filename, xt, yt)
  SVM(xn, yn, xp, yp, xt, yt, filename)
  KNN(xn, yn, xp, yp, xt, yt, filename, 1)
  xt.clear()
  yt.clear()
print("==========================================================") 

for y in range(1, 16):
  result = 'Positeif'
  filename = 'Test/' + 'Positief/' + 'CTP-' + str(y) + '.jpg'
  Test_Picture_Analyse(filename, xt, yt)
  SVM(xn, yn, xp, yp, xt, yt, filename)
  KNN(xn, yn, xp, yp, xt, yt, filename, 1)
  xt.clear()
  yt.clear()
print("==========================================================")
print()
print("SVM scored : " + str(int(SVM_R) / 30 * 100) + " % ")
print("KNN scored : " + str(int(KNN_R) / 30 * 100) + " % ")
'''




plt.subplot(1, 4, 4)
plt.axis([90, 93, 7.5, 10])
plt.title("Distribution")
plt.scatter(xn, yn)
plt.scatter(xp, yp)


plt.show()
