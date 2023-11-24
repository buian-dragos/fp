#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print statements. Functions here
# communicate via function parameters, the return statement and raising of exceptions. 
#
import random as r
import copy

def create_apartments():
    #type_keys = ("water", "heating", "electricity", "gas", "other")
    apartments = {"apartment": [], "type": []}
    for i in range(10):
        apartments["apartment"].append(i+1)
        amount={"water": r.randint(0,1000), "heating": r.randint(0,1000), "electricity": r.randint(0,1000), "gas": r.randint(0,1000), "other": r.randint(0,1000)}
        apartments["type"].append(amount)
    return apartments

def find_index(apartments,number):
    for i in range(len(apartments["apartment"])):
        if int(number) == apartments["apartment"][i]:
            return i

def total_expense(apartments,index):
    return apartments["type"][index]["water"] + apartments["type"][index]["heating"] + apartments["type"][index]["electricity"] + apartments["type"][index]["gas"] + apartments["type"][index]["other"]

#(A) Add new transaction
def add_transaction(apartments,undo_list,number,type,amount):
    if apartments["type"][0].get(type) == None or int(number) not in apartments["apartment"] or not amount.isdigit():
        raise ValueError("Invalid input")
    copie = copy.deepcopy(apartments)
    undo_list.append(copie)
    index = find_index(apartments,number)
    if type == "water":
        apartments["type"][index]["water"] += int(amount)
    elif type == "heating":
        apartments["type"][index]["heating"] += int(amount)
    elif type == "electricity":
        apartments["type"][index]["electricity"] += int(amount)
    elif type == "gas":
        apartments["type"][index]["gas"] += int(amount)
    elif type == "other":
        apartments["type"][index]["other"] += int(amount)
    return apartments, undo_list


#(B) Modify expenses

def remove_apartment(apartments,undo_list,start,end):
    if int(start) not in apartments["apartment"] or (int(end) != 0 and (int(end) not in apartments["apartment"])):
        raise ValueError("Invalid input")
    copie = copy.deepcopy(apartments)
    undo_list.append(copie)
    if end!=0:
        start_index = find_index(apartments,start)
        end_index = find_index(apartments,end)
        for index in range (start_index,end_index+1):
            apartments["type"][index]["water"] = 0
            apartments["type"][index]["heating"] = 0
            apartments["type"][index]["electricity"] = 0
            apartments["type"][index]["gas"] = 0
            apartments["type"][index]["other"] = 0
    else:
        index = find_index(apartments,start)
        apartments["type"][index]["water"] = 0
        apartments["type"][index]["heating"] = 0
        apartments["type"][index]["electricity"] = 0
        apartments["type"][index]["gas"] = 0
        apartments["type"][index]["other"] = 0
    return apartments, undo_list


def remove_type(apartments,undo_list,type):
    if apartments["type"][0].get(type) == None:
        raise ValueError("Invalid input")
    copie = copy.deepcopy(apartments)
    undo_list.append(copie)
    for i in apartments["apartment"]:
        index = find_index(apartments,i)
        if type == "water":
            apartments["type"][index]["water"] = 0
        elif type == "heating":
            apartments["type"][index]["heating"] = 0
        elif type == "electricity":
            apartments["type"][index]["electricity"] = 0
        elif type == "gas":
            apartments["type"][index]["gas"] = 0
        elif type == "other":
            apartments["type"][index]["other"] = 0
    return apartments, undo_list

def remove_unsafe(apartments,type):
    for i in apartments["apartment"]:
        index = find_index(apartments,i)
        if type == "water":
            apartments["type"][index]["water"] = 0
        elif type == "heating":
            apartments["type"][index]["heating"] = 0
        elif type == "electricity":
            apartments["type"][index]["electricity"] = 0
        elif type == "gas":
            apartments["type"][index]["gas"] = 0
        elif type == "other":
            apartments["type"][index]["other"] = 0
    return apartments
def replace(apartments,undo_list,number,type,amount):
    if apartments["type"][0].get(type) == None or int(number) not in apartments["apartment"] or not amount.isdigit():
        raise ValueError("Invalid input")
    copie = copy.deepcopy(apartments)
    undo_list.append(copie)
    index = find_index(apartments, number)
    amount = int(amount)
    if type == "water":
        apartments["type"][index]["water"] = amount
    elif type == "heating":
        apartments["type"][index]["heating"] = amount
    elif type == "electricity":
        apartments["type"][index]["electricity"] = amount
    elif type == "gas":
        apartments["type"][index]["gas"] = amount
    elif type == "other":
        apartments["type"][index]["other"] = amount
    return apartments, undo_list


#(C) Display expenses having different proprieties

def list(apartments):
    string = ""
    for i in apartments["apartment"]:
        string += list_apartment(apartments,i) + '\n'
    return string

def list_apartment(apartments,number):
    if (int(number) not in apartments["apartment"]):
        raise ValueError("Invalid input")
    index = find_index(apartments,number)
    string = "Apartment " + str(number) + '\n'
    if apartments["type"][index]["water"]!=0:
        string += "water: " + str(apartments["type"][index]["water"])
    if apartments["type"][index]["heating"]!=0:
        string += " heating: " + str(apartments["type"][index]["heating"])
    if apartments["type"][index]["electricity"]!=0:
        string += " electricity: " + str(apartments["type"][index]["electricity"])
    if apartments["type"][index]["gas"]!=0:
        string += " gas: " + str(apartments["type"][index]["gas"])
    if apartments["type"][index]["other"]!=0:
        string += " other: " + str(apartments["type"][index]["other"])
    string += '\n' + "total: " + str(total_expense(apartments,index)) + '\n'
    return string
def list_amount(apartments,char,amount):
    if (char != "<" and char != "=" and char != ">") or not amount.isdigit():
        raise ValueError("Invalid input")
    string = ""
    for i in apartments["apartment"]:
        if char=="<":
            if total_expense(apartments,find_index(apartments,i)) < int(amount):
                string += list_apartment(apartments,i) + '\n'
        elif char=="=":
            if total_expense(apartments, find_index(apartments, i)) == int(amount):
                string += list_apartment(apartments, i) + '\n'
        elif char==">":
            if total_expense(apartments, find_index(apartments, i)) > int(amount):
                string += list_apartment(apartments, i) + '\n'
    return string
#(D) Filter

def filter_type(apartments,undo_list,type):
    if apartments["type"][0].get(type) == None:
        raise ValueError("Invalid input")
    copie = copy.deepcopy(apartments)
    undo_list.append(copie)
    if type != "water":
       apartments = remove_unsafe(apartments,"water")
    if type != "heating":
       apartments = remove_unsafe(apartments,"heating")
    if type != "electricity":
       apartments = remove_unsafe(apartments,"electricity")
    if type != "gas":
       apartments = remove_unsafe(apartments,"gas")
    if type != "other":
       apartments = remove_unsafe(apartments,"other")
    return apartments, undo_list

def filter_value(apartments,undo_list,amount):
    copie = copy.deepcopy(apartments)
    undo_list.append(copie)
    amount = int(amount)
    for i in apartments["apartment"]:
        index = find_index(apartments,i)
        if apartments["type"][index]["water"]>=amount:
            apartments["type"][index]["water"] = 0
        if apartments["type"][index]["heating"]>=amount:
            apartments["type"][index]["heating"] = 0
        if apartments["type"][index]["electricity"]>=amount:
            apartments["type"][index]["electricity"] = 0
        if apartments["type"][index]["gas"]>=amount:
            apartments["type"][index]["gas"] = 0
        if apartments["type"][index]["other"]>=amount:
            apartments["type"][index]["other"] = 0
    return apartments, undo_list
#(E) Undo

def undo(apartments,undo_list):
    apartments = undo_list.pop()
    return apartments, undo_list
