def countOnes(left, right):
    def count_in_column(n,col):
        base = int(n/2**col)
        if base == 0: return 0
        if base % 2 == 0:
            return base * (2**col)/2
        else:
            return ((base - 1) * (2 ** col) / 2) + (n % 2 ** col) + 1
    
    def count_ones(n):
        counter = 0
        i = 0
        while count_in_column(n,i) > 0:
            counter += count_in_column(n,i)
            i += 1
        return counter
        
    left_ones = count_ones(left - 1)
    right_ones = count_ones(right)
    return int(right_ones - left_ones)
