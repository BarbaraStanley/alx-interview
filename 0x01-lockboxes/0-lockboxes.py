#!/usr/bin/python3

"""
A method that determines if all n number of locked boxes numbered sequentially
from 0 to n - 1 can be opened
"""


def canUnlockAll(boxes):
    unlocked = {0}
    # the first box is always unlocked
    locked = set(boxes[0])

    while len(locked) > 0:
        keys = locked.pop()
        # the set arranges the keys in sequence
        # so the keys will be the first one in locked
        # print(keys)

        if keys not in unlocked:
            unlocked.add(keys)
            locked.update(boxes[keys])
            # print(locked)

    logic = len(unlocked) == len(boxes)
    return logic
