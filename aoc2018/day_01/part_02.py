def main():
    with open('input.txt') as f:
        freqs = f.read().splitlines()
        freq = 0
        seen = set([0])
        while True:
            for f in freqs:
                freq = eval(f'freq {f}')
                if freq in seen:
                    break
                seen.add(freq)
            else:
                continue
            break

        return freq


if __name__ == '__main__':
    print(main())
