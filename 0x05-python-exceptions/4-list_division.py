#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    l = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            l.append(res)
        except TypeError:
            res = 0
            l.append(res)
            print("wrong type")
        except ZeroDivisionError:
            res = 0
            l.append(res)
            print("division by 0")
        except IndexError:
            res = 0
            l.append(res)
            print("out of range")
        finally:
            pass
    return l
