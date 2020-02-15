
def main():
    lines = input()
    n = int(lines)
    nums = []

    for i in range(n):
        v = input()
        nums.append(int(v))

    nums.sort()

    for i in range(n):
        print(nums[i])


main()