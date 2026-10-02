
# def rem(l , word):
#     for item in l:
#         l.remove(word)   in the list this code is remove list of last what have that will have 
#         return l

# l = ["pankaj", "suruja" , "monoja " ,"aj"]
# print(rem(l ,"aj"))

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
            return n 


l = ["Pankaj", "monoja", "suruja", "aj"]

print(rem(l, "aj"))