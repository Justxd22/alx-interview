#!/usr/bin/python3
"""Collect and print stats."""


import sys


if __name__ == '__main__':

    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}
    x = 0
    f = 0

    def print_stats(stats: dict, file_size: int) -> None:
        """Collect and print stats."""
        print("File size: {:d}".format(file_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            x += 1
            data = line.split()
            try:
                code = data[-2]
                if code in stats:
                    stats[code] += 1
            except BaseException:
                pass
            try:
                f += int(data[-1])
            except BaseException:
                pass
            if x == 10:
                x = 0
                print_stats(stats, f)
        print_stats(stats, f)
    except KeyboardInterrupt:
        print_stats(stats, f)
        raise
