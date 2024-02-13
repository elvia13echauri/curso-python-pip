#modulo para generar las graficas
import matplotlib.pyplot as plt

#grafica de barras
def generateBarChart(name,labels,values):
  fig,ax = plt.subplots()
  ax.bar(labels,values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

#grafica de pastel
def generatePieChart(labels,values):
  fig,ax = plt.subplots()
  ax.pie(values,labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

#manejo dual desde el run y el shell
if __name__ == '__main__':
  labels = [1,2,3,4,5]
  values = [100,20,300,40,50]
  #generateBarChart(labels,values)
  generatePieCart(labels, values)