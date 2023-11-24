import complexNumbers_list as lst
import complexNumbers_dict as dct
import subsequenceProprietes as sup
import time as t

#
# Write below this comment
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

def menu():
    complex_number_list = lst.make_random_complex_number(10)
    complex_number_dict = dct.make_random_complex_number_dict(10)
    while True:
        print("Choose:")
        print("1. List")
        print("2. Dictionary")
        print("3. Exit")
        repr_choice = int(input())
        if repr_choice == 3:
            print("Quitting")
            return
        elif (repr_choice!=1) and (repr_choice!=2):
            print("Entrance", repr_choice, "not valid.")
            return
        while True:
            print("Choose:")
            print("1. Add complex numbers.")
            print("2. Delete a complex number.")
            print("3. Display the list of complex numbers")
            print("4. Length and elements of a longest subarray of numbers "
                  "where both their real and imaginary parts can be written using the same base 10 digits")
            print("5. The length of the longest alternating subsequence, when considering each number's modulus.\n")
            print("6. Exit")

            choice = int(input())

            if choice == 1:
                if repr_choice==1:
                    while True:
                        complex_number = lst.read_complex_number()
                        exists = lst.add_complex_number(complex_number_list, complex_number)
                        if exists:
                            print("The complex number is already in the list.")
                            print()
                        else:
                            print("Complex number added.")
                            print()
                        print("Do you want to add another number? y/n")
                        continue_choice = input()
                        if continue_choice == 'y':
                            pass
                        elif continue_choice == 'n':
                            print("You will be returned to the menu.\n")
                            t.sleep(1)
                            break
                        else:
                            print("Entrance", continue_choice, "not valid. You will be returned to the menu.\n")
                            t.sleep(1)
                            break
                else:
                    while True:
                        complex_number = lst.read_complex_number()
                        exists = dct.add_complex_number_dict(complex_number_dict, complex_number)
                        if exists:
                            print("The complex number is already in the dictionary.\n")
                        else:
                            print("Complex number added.\n")
                        print("Do you want to add another number? y/n")
                        continue_choice = input()
                        if continue_choice == 'y':
                            pass
                        elif continue_choice == 'n':
                            print("You will be returned to the menu.\n")
                            t.sleep(1)
                            break
                        else:
                            print("Entrance", continue_choice, "not valid. You will be returned to the menu.\n")
                            t.sleep(1)
                            break
            elif choice == 2:
                if repr_choice==1:
                    complex_number = lst.read_complex_number()
                    exists = lst.delete_complex_number(complex_number_list, complex_number)
                    if exists:
                        print("The complex number isn't in the list.")
                        print()
                    else:
                        print("Complex number deleted.")
                        print()
                else:
                    complex_number = lst.read_complex_number()
                    exists = dct.delete_complex_number_dict(complex_number_dict, complex_number)
                    if exists:
                        print("The complex number isn't in the dictionary.\n")
                    else:
                        print("Complex number deleted.\n")
            elif choice == 3:
                if repr_choice==1:
                    print(lst.show_complex_number_list(complex_number_list))
                else:
                    print(dct.show_complex_number_dict(complex_number_dict))
            elif choice == 4:
                if repr_choice==1:
                    complex_subsets = sup.subsets(complex_number_list)
                    longest_subset = sup.longest_subarray(complex_subsets)
                    if len(longest_subset) == 0:
                        print("There is no such subarray.")
                        print()
                    else:
                        print("The length of the longest subarray satisfying the condition is: ", len(longest_subset))
                        print("The elements of the  longest subarray satisfying the condition are: ")
                        print(lst.show_complex_number_list(longest_subset))
                        print()
                else:
                    complex_subsets = sup.subsets(dct.dict_to_list(complex_number_dict))
                    longest_subset = sup.longest_subarray(complex_subsets)
                    if len(longest_subset) == 0:
                        print("There is no such subarray.")
                        print()
                    else:
                        print("The length of the longest subarray satisfying the condition is: ",
                              len(longest_subset))
                        print("The elements of the  longest subarray satisfying the condition are: ")
                        print(lst.show_complex_number_list(longest_subset))
                        print()
            elif choice == 5:
                if repr_choice==1:
                    print("The length of the longest alternating subsequence is:",
                          sup.longest_alternating_list(complex_number_list))
                else:
                    print("The length of the longest alternating subsequence is: ",
                          sup.longest_alternating_dict(complex_number_dict))
            elif choice == 6:
                print("Quitting")
                return
            else:
                print("Entrance", choice, "not valid. Try again")



if __name__ == "__main__":
    menu()