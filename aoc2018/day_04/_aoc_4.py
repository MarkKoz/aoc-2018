def get_log():
    with open('input.txt') as f:
        log = f.read().splitlines()
        log.sort(key=lambda e: e[:17])
        return log

def max_idx_getitem(log):
    from collections import defaultdict

    guards = defaultdict(lambda: [0, [0] * 59])
    sleepiest_guard = None

    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]

        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            end = minute
            guards[guard][0] += end - start
            mins = guards[guard][1]

            for i in range(start, end):
                mins[i] += 1
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif guards[sleepiest_guard][0] < guards[guard][0]:
                sleepiest_guard = guard

            guard = event

    mins, ranges = guards[sleepiest_guard]
    return min(range(len(ranges)), key=ranges.__getitem__)
    # print(f'ID: {sleepiest_guard}\nMinutes: {mins}\nMax: {max_min}')

def max_idx_enumerate_lambda(log):
    from collections import defaultdict

    guards = defaultdict(lambda: [0, [0] * 59])
    sleepiest_guard = None

    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]

        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            end = minute
            guards[guard][0] += end - start
            mins = guards[guard][1]

            for i in range(start, end):
                mins[i] += 1
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif guards[sleepiest_guard][0] < guards[guard][0]:
                sleepiest_guard = guard

            guard = event

    mins, ranges = guards[sleepiest_guard]
    return min(enumerate(ranges), key=lambda x: x[1])[0]
    # print(f'ID: {sleepiest_guard}\nMinutes: {mins}\nMax: {max_min}')

def max_count(log):
    from collections import defaultdict

    guards = defaultdict(lambda: [0, []])
    sleepiest_guard = None

    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]

        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            end = minute
            guards[guard][0] += end - start
            guards[guard][1] += range(start, end)
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif guards[sleepiest_guard][0] < guards[guard][0]:
                sleepiest_guard = guard

            guard = event

    mins, ranges = guards[sleepiest_guard]
    return max(ranges, key=ranges.count)
    # print(f'ID: {sleepiest_guard}\nMinutes: {mins}\nMax: {max_min}')

def max_count(log):
    from collections import defaultdict

    guards = defaultdict(lambda: [0, []])
    sleepiest_guard = None

    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]

        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            end = minute
            guards[guard][0] += end - start
            guards[guard][1].append(range(start, end))
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif guards[sleepiest_guard][0] < guards[guard][0]:
                sleepiest_guard = guard

            guard = event

    mins, ranges = guards[sleepiest_guard]
    for i in range(60):
        m = max(ranges)
    # return max(ranges, key=ranges.count)

def final(log):
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
    # max_min_2 = (None, -1, 0)
    # for guard, mins in guards.items():
    #     if mins:
    #         max_min = max(mins, key=mins.count)
    #         count = mins.count(max_min)
    #         if count > max_min_2[2]:
    #             max_min_2 = (guard, max_min, count)

def final_2(log):
    from collections import defaultdict
    with open('input.txt') as f:
        log = f.read().splitlines()
        log.sort(key=lambda e: e[:17])
    guards = defaultdict(lambda: [0, [0] * 59])
    sleepiest_guard = None
    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]
        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            guards[guard][0] += minute - start
            for i in range(start, minute):
                guards[guard][1][i] += 1
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif guards[sleepiest_guard][0] < guards[guard][0]:
                sleepiest_guard = guard
            guard = event
    else:
        if guards[sleepiest_guard][0] < guards[guard][0]:
            sleepiest_guard = guard
    total, mins_1 = guards[sleepiest_guard]
    max_min_1 = max(range(len(mins_1)), key=mins_1.__getitem__)
    # max_min_2 = (None, -1, 0)
    # for guard, mins in guards.items():
    #     if mins:
    #         max_min = max(mins, key=mins.count)
    #         count = mins.count(max_min)
    #         if count > max_min_2[2]:
    #             max_min_2 = (guard, max_min, count)

def final_3(log):
    from collections import defaultdict
    with open('input.txt') as f:
        log = f.read().splitlines()
        log.sort(key=lambda e: e[:17])
    guards = defaultdict(lambda: [0, []])
    sleepiest_guard = None
    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]
        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            guards[guard][0] += minute - start
            guards[guard][1].append(range(start, minute))
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif guards[sleepiest_guard][0] < guards[guard][0]:
                sleepiest_guard = guard
            guard = event
    else:
        if guards[sleepiest_guard][0] < guards[guard][0]:
            sleepiest_guard = guard
    total, ranges_1 = guards[sleepiest_guard]
    mins_1 = [0] * 59
    for r in ranges_1:
        for i in r:
            mins_1[i] += 1
    max_min_1 = max(range(len(mins_1)), key=mins_1.__getitem__)
    # max_min_2 = (None, -1, 0)
    # for guard, mins in guards.items():
    #     if mins:
    #         max_min = max(mins, key=mins.count)
    #         count = mins.count(max_min)
    #         if count > max_min_2[2]:
    #             max_min_2 = (guard, max_min, count)

def final_4(log):
    from collections import defaultdict
    with open('input.txt') as f:
        log = f.read().splitlines()
        log.sort(key=lambda e: e[:17])
    guards = defaultdict(lambda: [0, []])
    sleepiest_guard = None
    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]
        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            guards[guard][0] += minute - start
            guards[guard][1].append(range(start, minute))
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif guards[sleepiest_guard][0] < guards[guard][0]:
                sleepiest_guard = guard
            guard = event
    else:
        if guards[sleepiest_guard][0] < guards[guard][0]:
            sleepiest_guard = guard
    total, ranges_1 = guards[sleepiest_guard]
    mins_1 = [0] * 59
    max_min_1 = (-1, -1)
    for r in ranges_1:
        for i in r:
            mins_1[i] += 1
            if mins_1[i] > max_min_1[1]:
                max_min_1 = (i, mins_1[i])
    # max_min_2 = (None, -1, 0)
    # for guard, mins in guards.items():
    #     if mins:
    #         max_min = max(mins, key=mins.count)
    #         count = mins.count(max_min)
    #         if count > max_min_2[2]:
    #             max_min_2 = (guard, max_min, count)

def final_5(log):
    from collections import defaultdict
    with open('input.txt') as f:
        log = f.read().splitlines()
        log.sort(key=lambda e: e[:17])
    guards = defaultdict(lambda: [0, [0] * 59])
    sleepiest_guard = None
    sleepiest_guard_2 = (None, None, -1) # guard_id, minute, minute_freq
    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]
        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            guards[guard][0] += minute - start
            for i in range(start, minute):
                guards[guard][1][i] += 1
                if guards[guard][1][i] > sleepiest_guard_2[2]:
                    sleepiest_guard_2 = (guard, i, guards[guard][1][i])
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif guards[sleepiest_guard][0] < guards[guard][0]:
                sleepiest_guard = guard
            guard = event
    else:
        if guards[sleepiest_guard][0] < guards[guard][0]:
            sleepiest_guard = guard
    total, mins_1 = guards[sleepiest_guard]
    max_min_1 = max(range(len(mins_1)), key=mins_1.__getitem__)

def final_6(log):
    from collections import defaultdict
    with open('input.txt') as f:
        log = f.read().splitlines()
        log.sort(key=lambda e: e[:17])
    guards = defaultdict(lambda: [0, [0] * 59])
    sleepiest_guard = None
    sleepiest_guard_2 = [None, None, -1] # guard_id, minute, minute_freq
    for entry in log:
        entry = entry.split()
        minute = int(entry[1][3:5])
        event = entry[3][1:]
        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            guards[guard][0] += minute - start
            for i in range(start, minute):
                guards[guard][1][i] += 1
                if guards[guard][1][i] > sleepiest_guard_2[2]:
                    sleepiest_guard_2[0] = guard
                    sleepiest_guard_2[1] = i
                    sleepiest_guard_2[2] = guards[guard][1][i]
        else:  # started shift
            if sleepiest_guard is None:
                sleepiest_guard = event
            elif guards[sleepiest_guard][0] < guards[guard][0]:
                sleepiest_guard = guard
            guard = event
    else:
        if guards[sleepiest_guard][0] < guards[guard][0]:
            sleepiest_guard = guard
    total, mins_1 = guards[sleepiest_guard]
    max_min_1 = max(range(len(mins_1)), key=mins_1.__getitem__)

def final_7(log):
    from collections import defaultdict

    with open('input.txt') as f:
        log = f.read().splitlines()
        log.sort(key=lambda e: e[:17])

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

        if event.startswith('s'):  # asleep
            start = minute
        elif event.startswith('p'):  # awake
            guards[guard][0] += minute - start
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

    # print(int(sleepiest_guard) * max_min_1)
    # print(int(sleepiest_guard_2[0]) * sleepiest_guard_2[1])

def final_8(log):
    from collections import defaultdict

    with open('input.txt') as f:
        log = f.read().splitlines()
        log.sort(key=lambda e: e[:17])

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
            guards[guard][0] += minute - start
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

    int(sleepiest_guard) * max_min_1
    int(sleepiest_guard_2[0]) * sleepiest_guard_2[1]

def final_9(log):
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
            guards[guard][0] += minute - start
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

    int(sleepiest_guard) * max_min_1
    int(sleepiest_guard_2[0]) * sleepiest_guard_2[1]

def final_10(log):
    from collections import defaultdict

    with open('input.txt') as f:
        log = sorted(f.read().splitlines())

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
            guards[guard][0] += minute - start
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

    int(sleepiest_guard) * max_min_1
    int(sleepiest_guard_2[0]) * sleepiest_guard_2[1]


if __name__ == '__main__':
    import timeit
    # tests = ('max_idx_getitem', 'max_idx_enumerate_lambda', 'max_count')
    # tests = ('final', 'final_2', 'final_3', 'final_4', 'final_5', 'final_6', 'final_7')
    tests = ('final_8', 'final_9', 'final_10')
    for test in tests:
        print(timeit.timeit(f"{test}(log)", setup=f"from __main__ import {test}, get_log; log = get_log()", number=5000))
