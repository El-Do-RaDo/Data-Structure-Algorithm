import stack

def paranthes_checker(symbol_string):
    s = stack.Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.is_empty():
        return 'PERFECTLY BALANCED'
    else:
        return 'NOT PERFECTLY BALANCED'
def matches(open, close):
    opens = "({["
    closes = ")}]"
    return opens.index(open) == closes.index(close)
