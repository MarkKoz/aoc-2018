def main():
    import re

    pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    claims = [[[0, []] for _ in range(1000)] for _ in range(1000)]
    area = 0
    good = set()

    with open('input.txt') as f:
        for claim in f:
            id, x, y, w, h = map(int, pattern.match(claim).groups())
            overlaps = False
            for i in range(x, x + w):
                for j in range(y, y + h):
                    if claims[j][i][0] >= 1:
                        if claims[j][i][0] == 1:
                            area += 1

                        overlaps = True
                        for bad_id in claims[j][i][1]:
                            good.discard(bad_id)

                    claims[j][i][0] += 1
                    claims[j][i][1].append(id)

            if not overlaps:
                good.add(id)

        return area, good


if __name__ == '__main__':
    print(main())
