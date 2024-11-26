import time
import threading
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
if __name__ == "__main__":
    filenames = ["file 1.txt","file 2.txt", "file 3.txt", "file 4.txt"]
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_elapsed = time.time() - start_time
    print(f"{linear_elapsed} (линейный)")
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_elapsed = time.time() - start_time
    print(f"{multiprocessing_elapsed}(многопроцессный)")
