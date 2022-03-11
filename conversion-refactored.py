

def get_user_choice():
    user_choice_as_int = input("""
    please select one of the following:
    1. Teaspoon to metric
    2. Tablespoon to metric
    3. Fluid ounces to metric
    4. Pint to metric
    5. Display list
    6. Help
    7. Close\n""")
    return user_choice_as_int


def convert_value(message, convert_to):
    not_valid = True
    while not_valid:
        try:
            inputted_data = input(message)
            if convert_to == "int":
                converted_value = int(value)
            elif convert_to == "float":
                converted_value = float(value)
                not_valid = False
            return converted_value
        except:
            print("the value entererd is invalid, try again")


def get_amount_of_type():
    output = input("enter the number of what you want to convert:")
    return output


def get_converted_value(value, ratio):
    return value*ratio


def get_append_data(type_of_conversion, value, amount_of_type):
    return f"{amount_of_type} {type_of_conversion}(s) converted to {value}ml"


def display_array(array):
    return "\n".join(array)


def display_help():
    print("""
          This program will allow you to covert imperial to metric measurments.

          To use this, you can select what you would like to convert from, then you
          enter the amount of what you want to convert. To view your conversions, you need
          to select 5 in the menu""")


def main():
    array_of_conversions = []
    while_control = True
    while while_control:
        user_choice = get_user_choice()
        user_choice_as_int = convert_value(user_choice, "int")
        if user_choice_as_int >= 1 and user_choice_as_int <= 4:
            amount_of_type = get_amount_of_type()
            amount_of_type_as_float = convert_value(amount_of_type, "float")
            if user_choice_as_int == 1:
                type_of_conversion = "teaspoon"
                conversion_ratio = 5.92
            elif user_choice_as_int == 2:
                type_of_conversion = "tablespoon"
                conversion_ratio = 17.76
            elif user_choice_as_int == 3:
                type_of_conversion = "fluid ounce"
                conversion_ratio = 28.4
            elif user_choice_as_int == 4:
                type_of_conversion = "pint"
                conversion_ratio = 568
            converted_amount = get_converted_value(
                amount_of_type_as_float, conversion_ratio)
            data_to_append = get_append_data(
                type_of_conversion, converted_amount, amount_of_type)
            print(f"\n\n {data_to_append}")
            array_of_conversions.append(data_to_append)

        elif user_choice_as_int == 5:
            display_array(array_of_conversions)
        elif user_choice_as_int == 6:
            print(display_help())
        elif user_choice_as_int == 7:
            while_control = False


if __name__ == "__main__":
    main()
