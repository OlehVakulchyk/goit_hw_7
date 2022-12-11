import sys

from main import main


def start():
    path = None

    try:
        path = sys.argv[1]
        print(path)
    except:
        print("Have not argument")

    if path:
        main(path)


if __name__ == '__main__':
    start()
