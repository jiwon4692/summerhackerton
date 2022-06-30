user_input = input('100글자 이내 소문자 문자열 1개 입력 : ')
check = [-1]*26 

for i in range(len(user_input)):
    index = ord(user_input[i])
    if check[index] == -1:
        check[index] = i
        
print(*check)