'''
b=0
while True:
    try:
        a = input()
        b+=1
        if len(a)>100:
            break
        if b>100:
            break
        if a==' ':
            break
        print(a)
    except EOFError:
        break
''' # EOFerror활용해서 예외처리



