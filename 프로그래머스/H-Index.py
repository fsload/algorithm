def solution(citations):
    #h번이상 인용이 h개 이상 나머지가 h 번 이하

    h_index = 0
    citations = sorted(citations, reverse=True)
    for index, item in enumerate(citations):
        if index + 1 >= len(citations) - (index + 1) and item >= index + 1:
            h_index = index+1
    return h_index
