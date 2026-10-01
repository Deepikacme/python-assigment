numbers=[10, -5, 0, 20, -10, 0, 5]
positive=0
negative=0
zero=0
for i in numbers:
    if i> 0:
        positive+=1
    elif i<0:
        negative+=1
    else:
        zero+= 1
print("Positive:",positive)
print("Negative:",negative)
print("Zero:",zero)