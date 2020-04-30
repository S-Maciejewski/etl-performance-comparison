from datetime import date, timedelta
from urllib.request import urlopen
from io import BytesIO, StringIO
from zipfile import ZipFile
from multiprocessing import Pool, cpu_count
from functools import partial
import pandas as pd
import pysftp
import time

start = time.time()

zip_file = ZipFile('./randomized_data_00.zip', 'r')
print('Getting zipfile took %f s' % (time.time() - start))

zip_file.extractall('./unzipped_data')

print('Saving unzipped file took %f s' % (time.time() - start))

csv_file = open('./unzipped_data/randomized_data_00.csv', 'r')
filtered_file = open('./prefiltered_data/randomized_data_00_prefiltered.csv', 'w+')

header = csv_file.readline()

def nm_filter(file):
    for line in file:
        if line[0:3] == '"N"' or line[0:3] == '"M"':
            yield line

filtered = nm_filter(csv_file)

filtered_file.write(header)
for line in filtered:
    filtered_file.write(line)

print('saving filtered file file took %f s' % (time.time() - start))