
def reverse_num(num):
    return reverse_num_helper(num, 0)[0]
def reverse_num_helper(num, powerOfTen=0):
    
    while num >= 1:
        digit = num % 10
        num = num / 10       
        new_number, powerOfTen = reverse_num_helper(num, powerOfTen)        

        new_number += digit * (10**powerOfTen)
        powerOfTen += 1
        return new_number, powerOfTen

    return 0, 0


if __name__ == '__main__':
    print reverse_num(123456789)
