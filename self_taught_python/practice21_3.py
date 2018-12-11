from practice21_2 import Queue
import time
import random
# from ファイル名 import 関数


def simulate_line(till_show,max_time):

    pq = Queue()
    tix_sold = []

    for i in range(100):
        pq.enqueue("person" + str(i))

    t_end = time.time() + till_show
    now = time.time() # epochからの経過時間をfloatで返す
    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0,max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
        return tix_sold

    if __name__ == '__main__':
        sold = simulate_line(5, 10)
        print(sold)
        print(pq)

