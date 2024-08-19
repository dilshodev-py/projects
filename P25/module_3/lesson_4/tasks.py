import multiprocessing
import time

# emails = [f"EMAIL{i}" for i in range(1, 1_000_001)]

def emails():
    for i in range(1, 1000001):
        yield f"Email{i}"
split_numbers = [i for i in range(0, 1_000_000, 8000)]

start = time.time()


def send_emails(receiver_email):
    time.sleep(3)
    print(f"Success {receiver_email}    |   ")


def process_split(num):
    import threading
    threads = []
    for i in list(emails())[num:num + 8000]:
        t = threading.Thread(target=send_emails, args=(i,))
        t.start()
        threads.append(t)
    for i in threads:
        i.join()


if __name__ == '__main__':
    with multiprocessing.Pool(1000) as p:
        p.map(process_split, split_numbers)
    print(time.time() - start)
