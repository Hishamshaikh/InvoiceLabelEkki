import urllib
import csv

open_csv_file = open("C:\\Users\\Hisham Shaikh\\PycharmProjects\\Excel_Splitter_Combiner\\pdf.csv")

csv_data = csv.reader(open_csv_file, delimiter=',')
raw_details = []
fields = next(csv_data, None)

for row in csv_data:
    raw_details.append(dict(zip(fields, row)))

count = 1
for row in raw_details:
    y = row["PDP URL"]
    names = y.split('/')
    file_name = names[len(names) - 1]
    x = './scrapped/%s' % file_name
    urllib.urlretrieve(y, x)
    count += 1
