#Finding the cases of the given string in the format(upper case,lower case)
def cases(str):
    upper_case=0
    lower_case=0
    for i in str:
        if(i.isupper()):
            upper_case+=1
        else:
            lower_case+=1
    return upper_case,lower_case
str=input("Enter a word or sentence: ")
print(cases(str))

