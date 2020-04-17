import urllib
import csv
import os
import urllib.request

open_csv_file = open("C:\\Users\\Hisham Shaikh\\PycharmProjects\\Ekwinder_splitter\\pdf.csv")
csv_data = csv.reader(open_csv_file, delimiter=',')
raw_details = []
headers = next(csv_data, None)

for row in csv_data:
   raw_details.append(dict(zip(headers, row)))

count = 1
for row in raw_details:
    y = row["PDP URL"]
    names = y.split('/')
    file_name = names[len(names)-1]
    x = 'C:\\Users\\Hisham Shaikh\\PycharmProjects\\Ekwinder_splitter\\scrapped\\%s' % file_name
    urllib.request.urlretrieve(y, x)
    count += 1

print('Successful')
