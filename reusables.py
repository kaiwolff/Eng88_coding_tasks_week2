def input_float(): #makes sure that the input is a float
    #Will either return the input as a float or the phrase "exit"
    while True:
        var = input(f"Please enter a float. Type 'exit' to exit: ")
        if "exit" in var.lower():
            return "exit"
        else:
            try:
                return float(var)
            except:
                print("input not recognised")
                continue


def input_float_range(min_val, max_val): #makes sure that the input is a float within a set range
    #Will either return the input as a float or the phrase "exit"
    while True:
        var = input(f"Please enter a float between {min_val} and {max_val}. Type 'exit' to exit: ")
        if "exit" in var.lower():
            return "exit"
        else:
            try:
                float(var)
            except:
                print("input not recognised")
                continue

        if float(var) <= max_val and float(var) >=min_val:
            return float(var)
        else:
            print(f"Input must be between {min_val} and {max_val}. Please try again")
            continue

