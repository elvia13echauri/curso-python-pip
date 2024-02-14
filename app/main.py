import utils 
import read_csv
import charts
import pandas as pd

def run():
  
  

  '''
  #filtro para hacer legible el grfico de pastel
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  #grafica de pastel
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''
  #dataframe
  df = pd.read_csv('data.csv') #funcion en Pandas para leer csv
  df = df[df['Continent'] == 'Africa'] #forma de filtrar datos por contenido en una columna

  #extraccion de datos
  countries = df['Country/Territory'].values #funcion en pandas para optener valores de un diccionario
  percentages = df['World Population Percentage'].values

  charts.generatePieChart(countries, percentages)

  data = read_csv.readCsv('data.csv')
  #grafica de barras
  country = input('Type Country => ')

  result = utils.populationByCountry(data,country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.getPopulation(country)
    charts.generateBarChart(country['Country/Territory'],labels, values)
  

#dualidad de los modulos... dualidad scrip/modulo
#si se ejecuta desde la terminal, se maneje como scrip
if __name__ == '__main__':
  run()