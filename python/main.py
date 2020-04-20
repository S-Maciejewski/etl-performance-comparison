from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import time
import glob

test_files = glob.glob('../test_data/*.zip')
start_time = time.time()

# res = urlopen("https://www.kaggle.com/tunguz/covid19-genomes/download")
# zipfile = ZipFile(BytesIO(res.read()))

for test_file in test_files:
    file = open(test_file, 'rb')
    zipfile = ZipFile(BytesIO(file.read()))
    for line in zipfile.open(zipfile.namelist()[0]).readlines():
        # Transformation and loading to db
        # print(line.decode('utf-8'))
        pass

print('Execution time:', time.time() - start_time)
