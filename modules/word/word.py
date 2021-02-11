if __name__ == '__main__':
    print('This product includes software developed by L. Pham-Trong and this guy rocks.')


class word:
    def __init__(self, value: str, alphabet):
        self.val = [c for c in value]
        self.alph = alphabet
        self.last = alphabet[-1]
        self.first = alphabet[0]
        self.len_alph = len(alphabet)

    def last_that_is_not(self,word, target):
        for idx, c in enumerate(word[::-1]):
            if c != target: return len(word)-1 - idx
        return

    def next(self):
        # We look for the last letter that isn't equal to self.last
        change_loc = self.last_that_is_not(self.val, self.last)
        if change_loc is not None:
            elem = self.val[change_loc]
            new_letter = self.alph[self.alph.index(elem)+1]
            self.val[change_loc] = new_letter
        len_val = len(self.val)
        # In case last that is not isnt the last letter
        change_loc = -1 if change_loc is None else change_loc
        increment = change_loc == -1
        for idx in range(change_loc+1, len_val):
            self.val[idx] = self.alph[0]
        if increment:
            self.val = [self.alph[0] for i in range(len_val+1)]

    def real_next(self):
        for idx, c in enumerate(self.val[::-1]):
            if c == self.last:
                # prototype
                continue

    def __repr__(self):
        return ''.join(self.val)
    __str__ = __repr__
