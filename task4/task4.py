import sys


def main(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        nums = [int(line.strip()) for line in file]
    if not nums:
        return 'Файл пуст'
    nums.sort()
    n = len(nums)
    median = nums[n // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Используйте: python path/to/task1.py path/to/file')
    else:
        print(main(sys.argv[1]))
