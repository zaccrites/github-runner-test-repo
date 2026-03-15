
import sys


def fact(n: int) -> int:
    if n <= 1:
        return 1
    return n * fact(n - 1)


def main() -> int:
    result = fact(len(sys.argv))
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
