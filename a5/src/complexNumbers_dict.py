import random as r
import complexNumbers_list as lst


def make_random_complex_number_dict(count: int):
    assert count < 40 ** 2

    complex_number_dict = {"Real": [], "Imaginary": []}

    while count > 0:
        real = r.randint(-100, 100)
        imaginary = r.randint(-100, 100)
        complex_number_dict["Real"].append(real)
        complex_number_dict["Imaginary"].append(imaginary)
        count -= 1
    return complex_number_dict


def add_complex_number_dict(complex_number_dict: dict, complex_number):
    for i in range(len(complex_number_dict["Real"])):
        if lst.get_real(complex_number) == complex_number_dict["Real"][i] and lst.get_imaginary(complex_number) == \
                complex_number_dict["Imaginary"][i]:
            return 1
    complex_number_dict["Real"].append(lst.get_real(complex_number))
    complex_number_dict["Imaginary"].append(lst.get_imaginary(complex_number))
    return 0


def delete_complex_number_dict(complex_number_dict: dict, complex_number):
    flag = 0
    length = len(complex_number_dict["Real"])
    for i in range(length):
        if lst.get_real(complex_number) == complex_number_dict["Real"][i] and lst.get_imaginary(complex_number) == \
                complex_number_dict["Imaginary"][i]:
            flag += 1
            complex_number_dict["Real"].pop(i)
            complex_number_dict["Imaginary"].pop(i)
            return 0
    if flag == 0:
        return 1


def show_complex_number_dict(complex_number_dict: dict):
    complex_number_list_dict = []
    length = len(complex_number_dict["Imaginary"])
    for i in range(length):
        complex_number_list_dict.append(lst.new_complex_number(complex_number_dict["Real"][i],
                                                           complex_number_dict["Imaginary"][i]))
    sorted_list = sorted(complex_number_list_dict, key=lambda c: lst.get_real(c), reverse=True)
   # return "Current dictionary of complex numbers:\n" + "\n".join(map(to_str, sorted_list))
    return "Current dictionary of complex numbers:\n" + "\n".join(map(lst.to_str, complex_number_list_dict))

def dict_to_list(complex_number_dict: dict):
    complex_number_list = []
    length = len(complex_number_dict["Real"])
    for i in range(length):
        real = complex_number_dict["Real"][i]
        imaginary = complex_number_dict["Imaginary"][i]
        complex_number_list.append(lst.new_complex_number(real, imaginary))
    return complex_number_list