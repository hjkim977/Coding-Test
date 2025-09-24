def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num = arr1[i]|arr2[i]
        binary = bin(num)[2:]
        if len(binary)<n:
            binary = '0'* (n - len(binary))+binary
        word = ''
        for b in binary:
            if b=='1':
                word+='#'
            else:
                word+=' '
        answer.append(word)
    return answer