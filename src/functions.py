import csv

def read_csv():
  data_list = []
  path = 'data/employees.csv'
  with open(path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for line in reader:
      data_list.append(line)
  return data_list
