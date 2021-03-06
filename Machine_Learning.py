import matplotlib.pyplot as plt



xn, yn = [], []
xp, yp = [], []
xt, yt = [], []


def SVM(xn, yn, xp, yp, xt, yt, filename):
  rc = (yn[1] - yn[0]) / (xn[1] - xn[0])
  rc = -1 / float(rc)

  xsvm = list(range(90, 93))
  ysvm = [(float(rc) * x - 81.7) for x in xsvm]

  y = float(rc) * xt[0] - 81.7

  plt.subplot(1, 4, 4)
  plt.plot(xsvm, ysvm, c='black')

  if float(yt[0]) < float(y):
    result_SVM = 'Positief'
    plt.subplot(1, 4, 3)
    plt.title("SVM : " + str(result_SVM))
    print()
    print("SVM : " + str(filename) + " --> " + str(result_SVM))

  if float(yt[0]) > float(y):
    result_SVM = 'Negatief'
    plt.subplot(1, 4, 3)
    plt.title("SVM : " + str(result_SVM))
    print() 
    print("SVM : " + str(filename) + " --> " + str(result_SVM))


def KNN(xn, yn, xp, yp, xt, yt, filename, parameter):
  D_N, D_P = [], []
  for n in range(10):
    Distance = (((yn[n] - yt[0])**2) - ((xn[n] - xt[0])**2))**0.5
    D_N.append(str(Distance))
  for p in range(11):
    Distance = (((yp[p] - yt[0])**2) - ((xp[p] - xt[0])**2))**0.5
    D_P.append(str(Distance))

  if parameter == 1:
    if min(D_N) < min(D_P):
      plt.subplot(1, 4, 3)
      result_KNN = 'Negatief'
      plt.title("KNN : " + str(result_KNN))
      print("KNN : " + str(filename) + " --> " + str(result_KNN))
    if min(D_P) < min(D_N):
      plt.subplot(1, 4, 3)
      result_KNN = 'Positief'
      plt.title("KNN : " + str(result_KNN))
      print("KNN : " + str(filename) + " --> " + str(result_KNN))

  if parameter == 3:
    Nega, Posi = [], []

    if min(D_N) < min(D_P):
      D_N.remove(str(min(D_N)))
      Nega.append("1")

      if min(D_N) < min(D_P):
        D_N.remove(str(min(D_N)))
        Nega.append('1')
        if min(D_N) < min(D_P):
          D_N.remove(str(min(D_N)))
          Nega.append('1')
        if min(D_P) < min(D_N):
          D_P.remove(str(min(D_P)))
          Posi.append('1')

      if min(D_P) < min(D_N):
        D_P.remove(str(min(D_P)))
        Posi.append('1')
        if min(D_N) < min(D_P):
          D_N.remove(str(min(D_N)))
          Nega.append('1')
        if min(D_P) < min(D_N):
          D_P.remove(str(min(D_P)))
          Posi.append('1')

    if min(D_P) < min(D_N):
      D_P.remove(str(min(D_P)))
      Posi.append('1')

      if min(D_N) < min(D_P):
        D_N.remove(str(min(D_N)))
        Nega.append('1')
        if min(D_N) < min(D_P):
          D_N.remove(str(min(D_N)))
          Nega.append('1')
        if min(D_P) < min(D_N):
          D_P.remove(str(min(D_P)))
          Posi.append('1')

      if min (D_P) < min(D_N):
        D_P.remove(str(min(D_P)))
        Posi.append('1')
        if min(D_N) < min(D_P):
          D_N.remove(str(min(D_N)))
          Nega.append('1')
        if min(D_P) < min(D_N):
          D_P.remove(str(min(D_P)))
          Posi.append('1')

    if len(Posi) > len(Nega):
        print("KNN : " + str(filename) + " --> " + " Positief")
    if len(Nega) > len(Posi):
        print("KNN : " + str(filename) + " --> " + " Negatief")
