#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('day', type=int)
    parser.add_argument('--test', action='store_true')
    parser.set_defaults(test=False)
    args = parser.parse_args()

    try:
        mod = __import__(f'days.day{args.day}', fromlist=['solve'])
        input_file = f'test' if args.test else f'input'
        print(f'[#] Computing day {args.day}, test: {args.test}...')
        mod.solve(f'./input/{input_file}{args.day}.txt')
    except ModuleNotFoundError:
        print(f'[-] Solution for day {args.day} not implemented.')

if __name__ == '__main__':
    main()
