from datetime import datetime
from time import sleep


def print_hi(name):
    print(f'Hi, {name}', flush=True)


if __name__ == '__main__':
    for i in range(0, 100):
        print_hi('PyCharm the time is {}'.format(datetime.now()))
        sleep(1)
