def main():
    from collections import Counter

    twice = 0
    thrice = 0

    with open('input.txt') as f:
        for box_id in f.read().splitlines():
            seen_2 = False
            seen_3 = False
            for c in Counter(box_id).values():
                if seen_2 and seen_3:
                    break
                elif not seen_2 and c == 2:
                    twice += 1
                    seen_2 = True
                elif not seen_3 and c == 3:
                    thrice += 1
                    seen_3 = True

    return twice * thrice


if __name__ == '__main__':
    print(main())
