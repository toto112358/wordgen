def alphabet_gen(alphabet_type):
    if alphabet_type == 'az':
        return [chr(i) for i in range(97, 123)]
    if alphabet_type == 'aZ':
        return alphabet_gen('az') + alphabet_gen('az').upper()
    if alphabet_type == 'AZ':
        return alphabet_gen('az').upper()
    if alphabet_type is None:
        return alphabet_gen('az')
    return [letter for letter in alphabet_type]
