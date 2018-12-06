def main():
    from collections import defaultdict

    with open('input.txt') as f:
        log = f.read().splitlines()
        log.sort()

    # 0th index is a running total of the minutes slept.
    # 1st index is a list counting the number of days the guard was asleep during
    # a given minute (minutes are the list's indices).
    guards = defaultdict(lambda: [0, [0] * 59])

    sleepiest_guard = None  # The ID of the guard with the highest total of minutes slept.
    sleepiest_guard_2 = (None, None, -1)  # guard_id, minute, minute_freq

    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]

        if event[0] == 's':  # asleep
            start = minute
        elif event[0] == 'p':  # awake
            guards[guard][0] += minute - start  # Add to the running total of minutes slept.
            for m in range(start, minute):
                # Increment the number of days the guard was asleep for minute m.
                guards[guard][1][m] += 1

                # Check if this guard holds the record for most days slept for minute m.
                if guards[guard][1][m] > sleepiest_guard_2[2]:
                    sleepiest_guard_2 = (guard, m, guards[guard][1][m])
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif guards[sleepiest_guard][0] < guards[guard][0]:
                sleepiest_guard = guard  # Previous guard is the sleepiest guard.

            guard = event

    # Make sure the last event is taken into account for checking sleepiest guard.
    if guards[sleepiest_guard][0] < guards[guard][0]:
        sleepiest_guard = guard

    mins_1 = guards[sleepiest_guard][1]
    # Get the index (minute) which has the most days slept.
    max_min_1 = max(range(len(mins_1)), key=mins_1.__getitem__)

    return int(sleepiest_guard) * max_min_1, int(sleepiest_guard_2[0]) * sleepiest_guard_2[1]


if __name__ == '__main__':
    print(main())
