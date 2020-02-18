import concurrent.futures
import time

start = time.perf_counter()


def count_sum_thread():
    print('Thread is started.')
    my_sum = sum(map(int, range(1000)))
    return 'Thread was finished.'


def count_sum_process():
    print('Thread is started.')
    my_sum = sum(map(int, range(1000)))
    return 'Thread was finished.'


# -------------------------------------------------------------------------------

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(count_sum_thread) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)\n')

# -------------------------------------------------------------------------------

p_start = time.perf_counter()


with concurrent.futures.ProcessPoolExecutor() as executor:
    results = [executor.submit(count_sum_process) for _ in range(10)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())


p_finish = time.perf_counter()

print(f'Finished in {round(p_finish-p_start, 2)} second(s)')