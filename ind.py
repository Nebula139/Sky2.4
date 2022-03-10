#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


if __name__ == '__main__':
    a = str(input("Введите строку: "))
    print(reverse(a))
