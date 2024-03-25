def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        Reversed_string = reverse_string(s[1:]) + s[0]

    return Reversed_string
print(reverse_string("hello"))
