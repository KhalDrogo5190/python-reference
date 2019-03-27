#File IO
with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()

#functions
def num_words():
    count = 0
    for word in words:
        count+=1
    return count

def five_letter():
    count = 0
    for word in words:
        if len(word)==5:
            count+=1
    return count 

def longer_seven():
    count = 0
    for word in words:
        if len(word)>7:
            count+=1
    return count

def total_letters():
    count = 0
    for word in words:
        for w in word:
            count += 1
    return count

def no_e():
    count = 0
    for word in words:
        if 'e' not in word:
            count+=1
    return count

def first_last():
    count = 0
    for word in words:
        if word[0] == word[-1]:
            count+=1
    return count

def three_a():
    count = 0
    for word in words:
        count_a = 0
        for w in word:
            if w == 'a':
                count_a += 1
        if count_a == 3:
            count += 1
    return count

def q_no_u():
    count = 0
    for word in words:
        for i in range(len(word)):
            if word[i] == 'q':
                if len(word[i:]) >= 2 and word[i+1] != 'u':
                    count += 1
                    break
                elif len(word[i:]) < 2 :
                    count += 1
                    break 
                
    return count
    
#output
print(num_words())
print(five_letter())
print(longer_seven())
print(total_letters())
print(no_e())
print(first_last())
print(three_a())
print(q_no_u())
