#list
terms = ['computer', 'ram', 'binary', 'io', 'network', 'ethernet',
         'java', 'yeet', 'printer', 'hexadecimal', 'megabyte',
         'kilobyte', 'bit', 'code', 'python', 'logic', 'algorithm',
         'heuristic', 'fortnite', 'tik tok', 'octal', 'usb',
         'hdmi', 'server', 'ip', 'mountain dew', 'dell' , 'linux',
         'ubuntu', 'windows', 'mac', 'zip', 'compression', 'jpeg', 
         'gif', 'png', 'unicode', 'ascii', 'rom', 'memory', 'mouse',
         'hard drive',  'peripheral', 'rgb', 'byte', 'dvi', 'html',
         'technology', 'idle', 'holy grail', 'operating system',
         'ide', 'javascript', 'css', 'text editor']


# write functions here

def num_letters(word_list):
    ''' return the total number of characters in terms '''
    
    count = 0

    for word in word_list:
        count += len(word)

    return count
    

def first_letter_b(word_list):
    ''' return the number of terms with b as the first letter '''

    count = 0

    for word in word_list:
        if word[0] == 'b':
            count += 1

    return count

def has_e_fourth(word_list):
    ''' return the number of terms with e as the fourth letter '''

    count = 0

    for word in word_list:
        if len(word) > 3 and word[3] == 'e':
            count += 1

    return count

def five_letter_word(word_list):
    count = 0

    for word in word_list:
        if len(word) == 5:
            count += 1

    return count

def avg_length(word_list):
    total = 0

    for word in word_list:
        total += len(word)

    return total/len(word_list)

def longest_word_length(word_list):
    count = ""

    for word in word_list:
        if len(word) > len(count):
            count = word

    return len(count)

def longest_word(word_list):
    count = ""

    for word in word_list:
        if len(word) > len(count):
            count = word

    return count


def last_letter_s(word_list):
    count = 0

    for word in word_list:
        if word[-1] == "s":
            count += 1 

    return count

def total_e(word_list):
    count = 0

    for word in word_list:
        for w in word:
            if w == "e":
                count += 1

    return count

def total_letters(word_list):
    count = 0

    for word in word_list:
        for w in word:
            if w != " ":
                count += 1

    return count

# test functions here

print( num_letters(terms) )
print( first_letter_b(terms) )
print( has_e_fourth(terms) )
print( five_letter_word(terms) )
print( avg_length(terms) )
print( longest_word_length(terms) )
print( longest_word(terms) )
print( last_letter_s(terms) )
print( total_e(terms) )
print( total_letters(terms) )

