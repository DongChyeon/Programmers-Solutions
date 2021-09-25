ef solution(s):
    if len(s) == 1:
        return 1
    
    answer = len(s)
    
    # 문자를 몇 개 단위로 자를지 나타내는 변수
    count = 1
    while count < len(s):
        string = []
        start, end = 0, count
        while start < len(s) - 1:
            string.append(s[start:end])
            start, end = start + count, end + count
        if start < len(s):
            string.append(s[start:])
        # 다음에 자를 개수 단위를 늘림
        count += 1
        
        idx = 0
        while idx < len(string) - 1:
            target = idx + 1
            s_count = 1
            # 원본 문자열과 비교 문자열이 같다면 비교 문자열 삭제
            while target < len(string) and string[idx] == string[target]:
                s_count += 1
                del string[target]
            # 원본 문자열 앞에 원본 문자열의 원래 개수를 적어줌
            if s_count > 1:
                string.insert(idx, s_count)
                idx += 2
            else:
                idx += 1
        
        # 압축을 했을 때 글자수가 제일 적은 것이 답이 됨
        answer = min(answer, len(''.join(map(str, string))))
    
    return answer
