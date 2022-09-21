
def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data:
        char = str(char)
        if char.isdigit(): 
            count += char 
        else: 
            decode += char * int(count) 
            count = '' 

    return decode


data_after = open('after.txt', 'r')
data_after = list(data_after)
print(data_after)
decoding = []
for i in range(len(data_after)):
    decoding.append(rle_decode(data_after[i]))

data_before = open('before.txt', 'w')
for i in range(len(decoding)):
    data_before.write(decoding[i])

