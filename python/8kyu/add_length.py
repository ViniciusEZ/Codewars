def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split(' ')]

print(add_length("apple ban"))