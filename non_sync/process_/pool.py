from multiprocessing import Pool, cpu_count

import time


def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    print(" Process %s Finished." % work_data[0])


def pool_handler():
    work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])
    p = Pool(cpu_count())
    p.map(work_log, work)


if __name__ == '__main__':
    pool_handler()
