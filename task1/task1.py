import sys


def circular_array(n, m):
    circular_array = list(range(1, n + 1))
    path = []
    end_index = 0
    start_index = 0

    while True:
        path.append(circular_array[end_index])
        end_index = (end_index + m - 1) % n
        if end_index == start_index:
            break

    return ''.join(map(str, path))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Используйте: python path/to/task1.py <n> <m>')
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])
    result = circular_array(n, m)
    print(result)
