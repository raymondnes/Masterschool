def create_new_number(num):
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    new_hundreds = hundreds - ones
    new_ones = ones - hundreds
    simplify_hundreds = new_hundreds * 100
    simplify_tens = tens * 10
    simplify_ones = (new_ones * 1)
    new_number = (new_hundreds * 100) + (tens * 10) + (new_ones * 1)
    print(f"({new_hundreds} * 100) + ({tens} * 10) + ({new_ones} * 1) = {simplify_hundreds} + {simplify_tens} + ({simplify_ones}) = {new_number}")

create_new_number(856)
