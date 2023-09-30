def missing(inp_string):
    alpha='abcdefghijklmnopqrstuvwxyz'
    missing=[letter for letter in alpha if letter not in inp_string]
    return missing

inp_string='abcdefghijklmnoqstuvwxyz'
print(missing(inp_string))
