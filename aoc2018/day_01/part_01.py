def main():
    with open('input.txt') as f:
        freq = 0
        for f in f.read().splitlines():
            freq = eval(f'freq {f}')
        return freq


if __name__ == '__main__':
    print(main())
