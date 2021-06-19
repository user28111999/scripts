import time
import sys

def follow(f):
    f.seek(0, 2)
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


if __name__ == '__main__':
    logfile = open(
        sys.argv[1], "r"
    )
    try:
        loglines = follow(logfile)
        for line in loglines:
            print(line)
    except IndexError:
        print('ERROR! No path specified')
