#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def print_running_name():
    """Prints in what env the function is being called in"""
    if __name__ == "__main__":
        print("Running as a program")
    else:
        print("Running as a module")


def add_five(x):
    """Adds 5 to the supplied number"""
    return x + 5


if __name__ == "__main__":
    print_running_name()
