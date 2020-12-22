import stack

def base_converter(number, base):
    digits = "0123456789ABCDEF"

    rem_stack = stack.Stack()

    while number > 0 :
        rem = number % base
        rem_stack.push(rem)
        number = number // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string
