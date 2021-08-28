import string
str_input = input('Input a string:')
str_len = len(str_input)
count_letter=0
count_number=0
for i in range (0,str_len,1):
    if str_input[i].isalpha() ==True:
        count_letter +=1
    if str_input[i].isnumeric() ==True:
        count_number +=1
print (count_letter,count_number)
