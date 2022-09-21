def rle_encode(data_before):
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not data_before: 
        return '' 
    for char in data_before: 
        if char != prev_char: 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
                count += 1 
    else: 
        encoding += str(count) + prev_char 
        return encoding

data_before = open('before.txt', 'r')
data_before = list(data_before)
print(data_before)
encoding1 = []
for i in range(len(data_before)):
    encoding1.append(rle_encode(data_before[i]))
print(encoding1)
data_after = open('after.txt', 'w')
for i in range(len(encoding1)):
    data_after.write(encoding1[i])

