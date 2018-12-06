def main():
    import re

    pattern = re.compile(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)')
    claims = [[0] * 1000 for _ in range(1000)]
    area = 0

    with open('input.txt') as f:
        for claim in f:
            x, y, w, h = map(int, pattern.match(claim).groups())
            for i in range(x, x + w):
                for j in range(y, y + h):
                    if claims[j][i] == 1:
                        area += 1
                    claims[j][i] += 1

    return area


if __name__ == '__main__':
    print(main())
