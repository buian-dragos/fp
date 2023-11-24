import complexNumbers_list as lst
import complexNumbers_dict as dct

def getFreq(number1, number2):
    number1 = abs(number1)
    number2 = abs(number2)
    if number2 != 0:
        digits = len(str(number2))
    else:
        digits = 0
    number = number1 * (10 ** digits) + number2
    freq = [0] * 10
    while number > 0:
        freq[number % 10] = 1
        number = number // 10
    return freq


def subsets(complex_list):
    sets = []
    for i in range(2 ** len(complex_list)):
        subset = []
        for j in range(len(complex_list)):
            if i & (1 << j) > 0:
                subset.append(complex_list[j])
        sets.append(subset)
    return sets


def freqFlag(freq1, freq2):
    for i in range(10):
        if freq1 == freq2:
            return True
    return False


def longest_subarray(complex_subsets):
    index = 0
    length_max = 1
    flag = 1
    for i in range(1, len(complex_subsets)):
        if len(complex_subsets[i]) > length_max:
            for j in range(len(complex_subsets[i]) - 1):
                freq_a = getFreq(lst.get_real(complex_subsets[i][j]), lst.get_imaginary(complex_subsets[i][j]))
                freq_b = getFreq(lst.get_real(complex_subsets[i][j+1]), lst.get_imaginary(complex_subsets[i][j+1]))
                if not freqFlag(freq_a, freq_b):
                    flag = 0
                    break
            if flag == 1:
                index = i
                length_max = len(complex_subsets[i])
            flag = 1
    return complex_subsets[index]

def longest_alternating_list(complex_number_list):
    modulus_list = []
    for i in range(len(complex_number_list)):
        modulus_list.append(lst.get_real(complex_number_list[i])**2+lst.get_imaginary(complex_number_list[i])**2)
    inc = 1
    dec = 1
    for i in range(1, len(modulus_list)):
        if modulus_list[i] > modulus_list[i - 1]:
            inc = dec + 1
        elif modulus_list[i] < modulus_list[i-1]:
            dec = inc + 1
    print(modulus_list)
    return max(inc, dec)

def longest_alternating_dict(complex_number_dict):
    modulus_list = []
    for i in range(len(complex_number_dict["Real"])):
        modulus_list.append(complex_number_dict["Real"][i]**2+complex_number_dict["Imaginary"][i]**2)
    print(modulus_list)
    inc = 1
    dec = 1
    for i in range(1, len(modulus_list)):
        if modulus_list[i] > modulus_list[i - 1]:
            inc = dec + 1
        elif modulus_list[i] < modulus_list[i-1]:
            dec = inc + 1
    return max(inc, dec)