def new_string(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    else:
        return "Is" + str
print(new_string("large"))


