from matplotlib import pyplot as plt

def num_of_restaurants(data):
  resturants_by_location = {}

  for item in data:
    current_location = item['Location']
    if current_location in resturants_by_location:
      resturants_by_location[current_location].append(item)
    else:
      resturants_by_location[current_location] = [item]

  keys = resturants_by_location.keys()
  values = [len(item) for item in resturants_by_location.values()]
  return keys, values

def pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels, autopct='%1.1f%%')
  ax.axis('equal')
  plt.show()