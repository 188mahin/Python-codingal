def word_match(word):
    ctr=0
    lst=[]
    for word in word:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("list of items having the first and last numbers or letters same is ",lst)
    return ctr
count=word_match(["121","345","abba","ere","eye"])
print("the count of numbers matching is ",count)