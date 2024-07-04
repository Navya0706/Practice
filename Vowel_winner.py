#vowel winner
def count_vowels(s): 
    dict={"A":0,"E":0,"I":0,"O":0,"U":0}
    for i in s: 
        if i == "a" or i == "A": 
            dict['A']+=1
        elif i == "e" or i == "E": 
            dict['E']+=1
        elif i == "i" or i == "I": 
            dict['I']+=1
        elif i == "o" or i == "O": 
            dict['O']+=1 
        elif i == "u" or i == "U":
            dict['U']+=1    
    x=max(dict.values()) 
    result=[]
    for i,j in dict.items(): 
        if j==x: 
            result.append(i)
    return result

i_p=[
     ["navya","this is navyaa"],
     ["keerthi","this is keerthi"]]
op={}
for i in i_p:
    op[i[0]]=count_vowels(i[1])
print(op)     
