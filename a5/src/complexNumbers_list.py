import random as r

def new_complex_number(real, imaginary: int):
    return [real, imaginary]


def get_real(complex_number):
    return complex_number[0]


def get_imaginary(complex_number):
    return complex_number[1]


def to_str(complex_number):
    """
    Return the complex number's representation as a string
    :param complex_number: The complex number
    :return: A string; for complex number  (1,2),
    return "z =  1 + 2i"
    """
    if get_real(complex_number) != 0 and get_imaginary(complex_number) != 0:
        if get_imaginary(complex_number) > 0:
            return "z = " + str(complex_number[0]) + " + " + str(complex_number[1]) + "i"
        elif get_imaginary(complex_number) < 0:
            negative_imaginary = str(complex_number[1])
            negative_imaginary = negative_imaginary[:0] + negative_imaginary[1:]
            return "z = " + str(complex_number[0]) + " - " + negative_imaginary + "i"
    elif get_real(complex_number) == 0:
        return "z = " + str(complex_number[1]) + "i"
    elif get_imaginary(complex_number) == 0:
        return "z = " + str(complex_number[0])

def make_random_complex_number(count: int):
    """
    Create count random complex numbers
    :param count: number of elements to be created
    :return: The list of newly created complex numbers
    """
    assert count < 40 ** 2

    complex_number_list = []

    while count > 0:
        real = r.randint(-100, 100)
        imaginary = r.randint(-100, 100)
        complex_number_list.append(new_complex_number(real, imaginary))
        count -= 1
    return complex_number_list


def add_complex_number(complex_number_list: list, complex_number):
    """
    Adds the new_complex number to the list of complex numbers
    :param complex_number_list: List of complex numbers maintained by the program
    :param complex_number: The new complex number to add
    :return: 0 on success, 1 if complex number with given center already exists
    """
    if complex_number in complex_number_list:
        return 1
    complex_number_list.append(complex_number)
    return 0


def delete_complex_number(complex_number_list: list, complex_number):
    """
    Deletes a complex number from the list of complex numbers
    :param complex_number_list: List of complex numbers maintained by the program
    :param complex_number: The complex number to delete
    :return: 0 on success, 1 if the complex number does not exist
    """
    if complex_number not in complex_number_list:
        return 1
    complex_number_list.remove(complex_number)
    return 0


def read_complex_number():
    """
    Reads a complex number from the console; Real and imaginary parts must
    be integers (keep reading until true)
    :return: The new complex number.
    """
    while True:
        print()

        real = input("Enter the real part: ")
        if not real.lstrip('-').isdigit():
            print("The real part must be an integer.")
            continue
        real = int(real)

        imaginary = input("Enter the imaginary part: ")
        if not imaginary.lstrip('-').isdigit():
            print("The imaginary part must be an integer:")
            continue
        imaginary = int(imaginary)

        return new_complex_number(real, imaginary)


def show_complex_number_list(complex_number_list):
    sorted_list = sorted(complex_number_list, key=lambda c: get_real(c), reverse=True)
    # return "Current list of complex numbers:\n" + "\n".join(map(to_str, sorted_list))
    return "Current list of complex numbers:\n" + "\n".join(map(to_str, complex_number_list))