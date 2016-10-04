def reverseWords(string):
    string = string[::-1]
    i = 0
    j = 0
    newString = ''
    for char in string:
        if char == ' ' or j == len(string) - 1: # len(string) - 1 = 6
            newString += string[i: j][::-1]
            if j != len(string) - 1:
                newString += ' '
            i = j + 1
        j += 1
    return newString

if __name__ == '__main__':
    print(reverseWords('hello'))
    print(reverseWords('foo bar'))
    print(reverseWords('fiz baz'))
