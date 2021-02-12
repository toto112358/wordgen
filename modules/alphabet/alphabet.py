if __name__ == '__main__':
    print('This product includes software developed by L. Pham-Trong and this guy rocks.')
def alphabet_gen(alphabet_type):
    if alphabet_type == 'az':
        return [chr(i) for i in range(97, 123)]
    if alphabet_type == 'aZ':
        return alphabet_gen('az') + alphabet_gen('AZ')
    if alphabet_type == 'AZ':
        return [letter.upper() for letter in alphabet_gen('az')]
    if alphabet_type is None:
        return alphabet_gen('az')
    return [letter for letter in alphabet_type]
