# !/usr/bin/env python
# -*- coding: utf-8 -*-

def find_needed_words(some_list):
    items = {}
    for item in some_list:
        new_item = ''.join(sorted(item))
        if new_item not in items:
            items[new_item] = [item]
        else:
            items[new_item].append(item)
    res = sorted(list(map(lambda x: sorted(x), list(items.values()))))
    return res


def main():
    result = find_needed_words(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)


if __name__ == '__main__':
    main()
