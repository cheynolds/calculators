def square_root(number):

    sqrt = number / 2
    kelevin = 0
    
    while (sqrt != kelevin):
        print(str(sqrt))
        kelevin = sqrt;
        sqrt = (number/kelevin + kelevin) / 2
        
    return sqrt
