from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import time


start_time = time.time()
# res = urlopen("https://www.kaggle.com/tunguz/covid19-genomes/download")
# zipfile = ZipFile(BytesIO(res.read()))

file = open('test.zip', 'rb')
zipfile = ZipFile(BytesIO(file.read()))
print(zipfile.namelist())

for line in zipfile.open(zipfile.namelist()[0]).readlines():
    pass
    # print(line.decode('utf-8'))

print('Execution time:', time.time() - start_time)
