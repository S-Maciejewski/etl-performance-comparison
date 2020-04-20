from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import time
import glob

dtcc_us_urls = [
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_01.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_02.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_03.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_04.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_05.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_06.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_07.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_08.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_09.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_10.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_11.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_12.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_13.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_14.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_15.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_16.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_17.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_18.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_19.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_20.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_21.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_22.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_23.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_24.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_25.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_26.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_27.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_28.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_29.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_30.zip',
    'https://kgc0418-tdw-data-0.s3.amazonaws.com/slices/CUMULATIVE_COMMODITIES_2020_03_31.zip'
]
test_files = glob.glob('../test_data/*.zip')
# file = open(test_file, 'rb')
# zipfile = ZipFile(BytesIO(file.read()))


start_time = time.time()


for url in dtcc_us_urls:
    res = urlopen(url)
    zipfile = ZipFile(BytesIO(res.read()))
    for line in zipfile.open(zipfile.namelist()[0]).readlines():
        # Transformation and loading to db
        # print(line.decode('utf-8'))
        pass

print('Execution time:', time.time() - start_time)
