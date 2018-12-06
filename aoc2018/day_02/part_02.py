def main():
    with open('input.txt') as f:
        ids = f.read().splitlines()
        ids.sort()

    for i in range(len(ids) - 1):
        cur = ids[i]
        nex = ids[i + 1]
        diff = 0
        diff_idx = 0

        for j in range(len(cur)):
            if diff > 1:
                break
            if cur[j] != nex[j]:
                diff += 1
                diff_idx = j
        else:
            if diff == 1:
                return cur[:diff_idx] + cur[diff_idx + 1:]


if __name__ == '__main__':
    print(main())
