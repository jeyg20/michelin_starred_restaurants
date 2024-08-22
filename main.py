import read_csv
import chart

if __name__ == '__main__':
  data = read_csv.read_file('./michelin_restaurants.csv')
  country, number = chart.num_of_restaurants(data)
  chart.pie_chart(country, number)