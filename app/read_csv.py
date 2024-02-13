#modulo para manejar los csv
import csv

#funcion para abrir y leer el csv
def readCsv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header,row)
      country_dict = {key:value for key, value in iterable}
      data.append(country_dict)
    return data

#manejo dual para run y shell
if __name__ == '__main__':
  data = readCsv('./app/data.csv')
  print(data[34])

