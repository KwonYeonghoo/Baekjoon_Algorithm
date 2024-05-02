word = input()
arr = ['0'] * 26
for ascii in range(97,123):
    alphabet = chr(ascii)
    arr[ascii-97] = str(word.find(alphabet))
print(' '.join(arr))