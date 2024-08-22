import csv

def read_file(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    header = next(reader)
    data = []

    for row in reader:
      iterable = zip(header, row)
      restaurants_dict = dict(iterable)
      data.append(restaurants_dict)
      
    return data 