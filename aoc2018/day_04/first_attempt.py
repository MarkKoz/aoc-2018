def main():
    from collections import defaultdict

    with open('input.txt') as f:
        log = f.read().splitlines()
        log.sort(key=lambda e: e[:17])

    guards = defaultdict(list)
    sleepiest_guard = None

    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]

        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            guards[guard] += range(start, minute)
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif len(guards[sleepiest_guard]) < len(guards[guard]):
                sleepiest_guard = guard

            guard = event
    else:
        if len(guards[sleepiest_guard]) < len(guards[guard]):
            sleepiest_guard = guard

    mins_1 = guards[sleepiest_guard]
    max_min_1 = max(mins_1, key=mins_1.count)

    max_min_2 = (None, -1, 0)
    for guard, mins in guards.items():
        if mins:
            max_min = max(mins, key=mins.count)
            count = mins.count(max_min)
            if count > max_min_2[2]:
                max_min_2 = (guard, max_min, count)

    return int(sleepiest_guard) * max_min_1, int(max_min_2[0]) * max_min_2[1]


if __name__ == '__main__':
    print(main())
