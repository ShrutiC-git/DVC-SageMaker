import os
import wget

url = "https://shrutideveloper.s3.amazonaws.com/Iris.csv"
data = wget.download(url)

with open(data) as f:
    with open("Iris.data", 'w') as f2:
        for line in f:
            f2.write(line)

os.remove(data)


