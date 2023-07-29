#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        value = a / b
    except ZeroDivisionError:
        print("Inside result: {}".format("None"))
    else:
        print("Inside result: {}".format(value))
    finally:
        return value if 'output' in locals() else None

