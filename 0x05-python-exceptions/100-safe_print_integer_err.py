#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError, NameError) as ex:
        sys.stderr.write("Exception:" + str(ex) + "\n")
        return False
