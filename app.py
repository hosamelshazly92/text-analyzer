from string import digits

# import text file open(file, mode)
file = open('demo.txt', 'rt', encoding='utf-8')

# print file name and mode
# print(f'File Name: "{file.name}", File Mode: "{file.mode}"')

# read text
# print(file.read())

# limit by characters
# print(file.read(10))
# specify print position
# file.seek(0)
# print(file.read(10))

# read line
# print(file.readline())

# readlines
# lines = file.readlines()
# for line in lines:
    # print(line, '\n')
    # print(line, end='')

# read line by line
# for line in file:
#     print(line)

# get current position
# print(file.tell())

# check file close
# print(f'Check file close: {file.closed}')
# close file
# file.close()
# check file close
# print(f'Check file close: {file.closed}')

# create text file with context manager and run
# with open('demo2.txt', 'w') as text:
#     text.write('text')

# ------------------------------------------------------------------------ #

text_with_spaces = file.read()
# print(type(text))
# print(f'Text length with spaces:                {len(text_with_spaces)}')

# check for digits
check_digit = any(char.isdigit() for char in text_with_spaces)
# print(f'Text contains digits:                   {check_digit}')
# remove digits, import digits module
remove_digits = str.maketrans('', '', digits)
text_without_digits = text_with_spaces.translate(remove_digits)
# print(f'Text length without digits:             {len(text_without_digits)}')

# check for special characters
# check_letters = any(char.isalpha() for char in text_without_digits)
# print(f'Text contains no special characters:    {check_letters}')
# remove all special characters
# text_without_special_characters = text_without_digits.replace("()", "")
# print(f'Text length without special characters: {len(text_without_special_characters)}')

# remove leading and ending spaces
text_indent = text_without_digits.strip()
# print(f'Text length with indentation:           {len(text_indent)}')

# remove all special characters
# string = ''.join(e for e in string if e.isalnum())

# remove spaces
# string = string.replace(" ", "")

# remove all whitespace characters
# text_letters = "".join(text_indent.split())

print(text_indent)

# letter count
letter = ["ص", "ل", "ر"]
letter_count = 0
for i in letter:
    for j in text_indent:
        if (j == i):
            letter_count += 1
    print(f'Letter "{j}" has number of occurrences:{letter_count}')
    letter_count = 0
