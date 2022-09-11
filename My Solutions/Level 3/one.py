def solution(n):
    num=int(n)
    num_binary='0'+format(num,'b')
    val=0
    while int(num_binary,2)!=1:
        binary_seg=binary_segment_last(num_binary)
        length=len(binary_seg)
        if binary_seg[0]=='0':
            val=val+length
            num_binary=num_binary[0:-length]
        else:
            val=val+1
            if length==1:
                num_binary=num_binary[0:-1]+'0'
            else:
                num_binary=num_binary[0:-(length+1)]+'1'+'0'*length
        if int(num_binary,2)==3:
            val=val+2
            num_binary='1'
    return val

def binary_segment_last(binary_string):
    for i in range(len(binary_string)-1,-1,-1):
        if binary_string[i]==binary_string[-1]:
            continue
        else:
            return binary_string[i+1:]

print(solution('3'))