import multiprocessing
import time
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline().strip()
            all_data.append(line)
            if not  line:
                break

filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
# started_1 = datetime.now()
# for i in filenames:
#      read_info(i)
#
# stopped_1 = datetime.now()
# time_func = stopped_1 - started_1
# print(f'Время работы линейного подхода: {time_func}')

if __name__ == '__main__':
    started_2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    stopped_2 = datetime.now()
    time_multiprocess = stopped_2 - started_2
    print(f'Время работы многопроцессного подхода: {time_multiprocess}')

# Время работы линейного подхода: 0:00:07.046163
# Время работы многопроцессного подхода: 0:00:02.946290