def bm_match(txt: str, pat: str) -> int:
    skip = [None] * 256
    
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1
        
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp
        
    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력 : ')
    s2 = input('패턴을 입력 : ')
    
    idx = bm_match(s1, s2)
    
    if idx == -1:
        print('텍스트 안에 패턴 없음')
    else:
        print(f'{(idx + 1)}번째 문자가 일치함')