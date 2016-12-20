def checkio(n, m):
    diff = 0
    bin_m, bin_n = bin(m)[2:], bin(n)[2:]
    expected_len = max(len(bin_m), len(bin_n))
    bin_m = '0'*(expected_len-len(bin_m))+bin_m
    bin_n = '0'*(expected_len-len(bin_n))+bin_n
    for i in range(expected_len):
        if bin_m[i] != bin_n[i]:
            diff += 1
    return diff

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
