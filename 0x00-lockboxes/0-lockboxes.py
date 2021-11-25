#!/usr/bin/python3
""" Lockboxes Algorithm Problem """


def canUnlockAll(boxes):
""" determines whether an array of boxes holding keys can all be opened """

    # list comprehension to a dictionary for access
    box_dict = {box_i:box for box_i, box in enumerate(boxes)}
    
    unique_keys = {}
    # track # of visited boxes
    visited = {}

    # current stack (FILO) of keys
    key_stack = []

    # unique boxes opened
    i = 0

    # while the list of keys is not empty, unlock subsequent boxes

    box_to_search = 0

    # while loop constrained by when running total is equal to box_dict length
    while i < len(box_dict) - 1:
        # iterate through potential keys in the box
        for key in box_dict[box_to_search]:
            # check if key exists in box dictionary
            if box_dict.get(key, None) is not None:
                if unique_keys.get(key, None) is None:
                    # collecting keys to the stack
                    key_stack.append(key)
                    unique_keys[key] = True
        # mark box as searched
        visited[box_to_search] = True
        i += 1

        if key_stack:
            next_box = key_stack.pop()
        else:
            return False
        if visited.get(next_box, None) is None:
            box_to_search = next_box

    return True
