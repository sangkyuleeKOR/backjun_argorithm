# EOFerror활용해서 예외처리
# b=0
# while True:
#     try:
#         a = input()
#         b+=1
#         if len(a)>100:
#             break
#         if b>100:
#             break
#         print(a)
#     except EOFError:
#         break

# 상대오차,절대오차 10^-9까지 허용하는 코드
# a,b = map(int,input().split())
# print('%0.9f'%(a/b))

# 이게 왜 같을까??? 생각해보자

# a,b,c = map(int,input().split())

# print((a+b)%c)
# print((a%c+b%c)%c)
# print((a*b)%c)
# print((a%c*b%c)%c)

# 덧셈...
# a = int(input())
# b = int(input())
# print(a+b)

#설탕배달 -> 상근이는 사탕가게에 N킬로그램을 배달해야 한다
#설탕공장에서 만드는 설탕은 봉지에 담겨져 있다.
#봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
#최대한 적은 수의 봉지를 사용해 배달하여야 한다.
#만약 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.

a = int(input())
total_num = 0
while a>0:
    if a%5 != 0:
        a = a-3
        if a<0:
            total_num=-1
            break
        total_num+=1
    
    elif a%5 ==0:
        a = a-5
        if a<0:
            total_num=-1
            break
        total_num+=1
    elif a%5!=0 and a%3!=0:
        total_num=-1


print(total_num)



