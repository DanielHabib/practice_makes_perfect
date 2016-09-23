'''
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

    AAA ->
   
''' 
letterValue = {
    "A": 1,
    ...:...,
    "Z": 26
}

def excelNumber(string):
    count = 0
    i = 1
    for letter in string[::-1]:
        count += letterValue[letter] * i
        i += 1
    return count

'''
    Proof
      BC: ''   => 0
          'A'  => 1
          'AA' => 27


'''






