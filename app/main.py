import utils 
import read_csv
import charts


def run():
  data = read_csv.readCsv('data.csv')

  #filtro para hacer legible el grfico de pastel
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  #grafica de pastel
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generatePieChart(countries, percentages)

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