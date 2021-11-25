#!/usr/bin/python3
""" Minimum Operations Algorithm Problem """


def minOperations(n: int) -> int:
    """ Calculates minimum number of operations required to create a string """
    """ of input n length """

    if not n or not isinstance(n, int) or n <= 1:
        return 0
    count = 1
    operations_list = []
    while n > 1:
        count += 1
        while (n % count == 0 and n > 1):
            n /= count
            operations_list.append(count)
    return sum(operations_list)
