def string_clean(s):
    return ''.join([i for i in s if not i.isnumeric()])


print(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"))