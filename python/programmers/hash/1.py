def solution(participant, completion):
    answer = ''
    
    hash_table = {}
    for i in completion:
        if i not in hash_table:
            hash_table[i] = 1
        else:
            hash_table[i] += 1
        
    for i in  participant:
        if i not in hash_table:
            return i
        else:
            if hash_table[i] >= 1:
                hash_table[i]-=1
            else:
                return i