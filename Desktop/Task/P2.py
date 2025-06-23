#1st Program
# def str(s):
#     sub_str = s.split('0')
#     print(sub_str)
#     while '' in sub_str:
#         sub_str.remove('')
#     return {
#         'first_name': sub_str[0],
#         'last_name': sub_str[1],
#         'id': sub_str[2]
#     }

# print(str("Robert000Smith000123"))


#2nd Program
# s1 = "eueiieo"
# s2 = "iieoedue"

# for i in s2:
#     if s2.count(i) > s1.count(i):
#         print(i)
#         break

#3rd Program
# def shadow(s1, s2):
#     w1 = s1.split()
#     w2 = s2.split()

#     if len(w1) != len(w2):
#         return False

#     for i in range(len(w1)):
#         if len(w1[i]) != len(w2[i]):
#             return False
#         for j in w1[i]:
#             if j in w2[i]:
#                 return False

#     return True
# print(shadow("they are round", "fold two times")) 
# print(shadow("his friends", "our company"))


#4th Program
# def dup_letters(s):
#     words = s.split()
#     print(words)
#     for word in words:
#         for letter in word:
#             if word.count(letter) > 1:
#                 return True
#     return False
# print(dup_letters("Vamsi"))  
# print(dup_letters("Krishnaa")) 

#5th Program
# def str_to_hex(s):
#     result = ""
#     for i in s:
#         hex = format(ord(i), '02x')  
#         result+= hex+" "
    
#     return result.strip()

# print(str_to_hex("Hello"))
# print(str_to_hex("ABC123"))


#6th Program
# import datetime
# def friday(month, year):
#     date = datetime.date(year, month, 13)
#     if date.weekday() == 4:
#         return True
#     else:
#         return False
# print(friday(5, 2025))  
# print(friday(6, 2025)) 

#7th Program
# def block_win(p1, p2):
#     winning_combinations = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
#     for combo in winning_combinations:
#         if p1 in combo and p2 in combo:
#             for p in combo:
#                 if p != p1 and p != p2:
#                     return p
#     return None

# print(block_win(0, 1))
# print(block_win(2, 4)) 
# print(block_win(3, 6))  
# print(block_win(1, 5)) 
# print(block_win(7, 0))


def morse_code(text):
    # Morse code dictionary (includes letters, digits, and common punctuation)
    morse_dict = {
        'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
        'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
        'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
        'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
        '!': '-.-.--', ':': '---...', '"': '.-..-.', '(': '-.--.',
        ')': '-.--.-', '&': '.-...', ';': '-.-.-.', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '_': '..--.-', '/': '-..-.',
        '@': '.--.-.', '$': '...-..-'
    }

    text = text.upper()
    result = []
    for char in text:
        if char == ' ':
            result.append('/')  
        elif char in morse_dict:
            result.append(morse_dict[char])
        else:
            result.append('?')

    return ' '.join(result)

print(morse_code("Hello, World!"))









