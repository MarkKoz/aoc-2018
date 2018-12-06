import argparse
import os
import pkgutil
import timeit
from collections import OrderedDict
from typing import Sequence

ORIGINAL_CWD = os.getcwd()

# Make timeit return the value of the function it timed.
timeit.template = """
def inner(_it, _timer{init}):
    {setup}
    _t0 = _timer()
    retval = None
    for _i in _it:
        {stmt}
    _t1 = _timer()
    return _t1 - _t0, retval
"""

def run_benchmark(package: str, module: str, no_executions: int = 1):
    """Benchmark a module from a package and log the results."""
    cwd = os.path.join(os.getcwd(), package)
    time, output = timeit.timeit(
        'retval = main()',
        setup=f'import os; os.chdir({repr(cwd)}); from {package}.{module} import main',
        number=no_executions
    )
    os.chdir(ORIGINAL_CWD)

    try:
        if not isinstance(output, str):
            output = ', '.join(map(str, output))
    except TypeError:
        if output is None:
            output = str(None)

    time_output = f'{time:06f} seconds'
    if no_executions > 1:
        time_output += f' ({time / no_executions:06f} avg)'

    print(f'    {module:<15} | {output:<30} | {time_output}')


def benchmark_modules(modules: Sequence[str], no_executions: int = 1):
    """Benchmark the given modules."""
    print(f'Results for benchmarks with {no_executions} executions:')

    packages = OrderedDict()
    for module in modules:
        package, module = module.rsplit('.', 1)
        packages.setdefault(package, []).append(module)

    for package, modules in packages.items():
        print(package)

        for module in modules:
            run_benchmark(package, module, no_executions)


def benchmark_days(days: Sequence[int] = range(1, 26), no_executions: int = 1):
    """Benchmark all modules for the given days."""
    print(f'Results for benchmarks with {no_executions} executions:')

    for i in days:
        package = f'day_{i:02d}'
        print(package)

        for module in pkgutil.iter_modules([package]):
            if module.name[0] != '_':
                run_benchmark(package, module.name, no_executions)


class CreateRange(argparse.Action):
    """Convert a pair of values to a range."""

    def __call__(self, parser, args, values, option_string=None):
        start, stop = values
        if stop < start:
            raise ValueError('Invalid range: stop must be greater than start')

        setattr(args, self.dest, range(start, stop + 1))


def validate_day(day: str):
    """Convert a day string to an int and validate it is in the range [1, 25]."""
    day = int(day)
    if day not in range(1, 26):
        raise argparse.ArgumentTypeError(f'{day} is not in the range [1, 25]')

    return day


def main():
    parser = argparse.ArgumentParser(prog='Advent of Code 2018 Benchmarker')
    parser.add_argument(
        '-n', '--no-executions',
        type=int,
        default=1,
        help='The number of executions for each benchmark.'
    )

    days_group = parser.add_mutually_exclusive_group()
    days_group.add_argument(
        '-r', '--range',
        nargs=2,
        type=validate_day,
        action=CreateRange,
        default=range(1, 26),
        help='The start and stop (both inclusive) for the range of days to benchmark.'
    )
    days_group.add_argument(
        '-d', '--days',
        nargs='+',
        type=validate_day,
        default=None,
        help='A list of days to benchmark.'
    )
    days_group.add_argument(
        '-m', '--modules',
        nargs='+',
        help='The names of the modules to benchmark.'
    )

    args = parser.parse_args()
    if args.modules:
        benchmark_modules(args.modules, args.no_executions)
    else:
        days = args.days or args.range
        benchmark_days(days, args.no_executions)


if __name__ == '__main__':
    main()