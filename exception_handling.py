def handle_exceptions():
    try:
        # Example 1: SyntaxError
        print("Hello")  # Missing closing parenthesis
    except SyntaxError as e:
        print(f"SyntaxError: {e}")

    try:
        # Example 2: IndentationError
        if True:
            print("Indentation error")
    except IndentationError as e:
        print(f"IndentationError: {e}")

    try:
        # Example 3: NameError
        print(undefined_variable)
    except NameError as e:
        print(f"NameError: {e}")

    try:
        # Example 4: TypeError
        result = 10 + "20"
    except TypeError as e:
        print(f"TypeError: {e}")

    try:
        # Example 5: IndexError
        my_list = [1, 2, 3]
        print(my_list[5])
    except IndexError as e:
        print(f"IndexError: {e}")

    try:
        # Example 6: ValueError
        int("abc")
    except ValueError as e:
        print(f"ValueError: {e}")

    try:
        # Example 7: FileNotFoundError
        with open("nonexistent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

    try:
        # Example 8: ZeroDivisionError
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")

    try:
        # Example 9: KeyError
        my_dict = {"a": 1, "b": 2}
        value = my_dict["c"]
    except KeyError as e:
        print(f"KeyError: {e}")
    else:
        print(f"The value is: {value}")
    finally:
        print("This block will always execute.")

# Call the function to see the error handling in action
handle_exceptions()
