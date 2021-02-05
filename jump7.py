a = 0
while a < 100:
    a = a + 1
    if a%10 == 7 or a%7 == 0:  #7? ????7? ??
        continue
    elif a//10 == 7: #10???7???
        continue
    print(a)
