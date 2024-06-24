#리스트를 정렬하여 중앙위치를 반환하는 함수
def sort_and_get_mid(list, start, end):
    list[start : end + 1] = sorted(list[start : end + 1]) #리스트를 정렬
    return (start + end) // 2 # 작은 리스트의 중앙값(m)

# 피벗을 고르는 함수
def choose_pivot(list, start, end):
    if end - start < 5: # M 을 구하는 경우
        return sort_and_get_mid(list, start, end) # 각 그룹의 중앙값(m)의 중앙값(M) 위치 반환

    cur = start # 각 그룹의 중앙값(m)을 모을 위치
    for i in range(start, end+1, 5):
        mid_loc = sort_and_get_mid(list, i, min(i+4, end)) # 전체 원소들을 5개씩 원소를 가진 5/n개의 그룹으로 나눔
        list[cur], list[mid_loc] = list[mid_loc], list[cur] # 각 그룹의 중앙값들을 리스트의 앞부분에 모음
        cur+=1 # 다음 각 그룹의 중앙값(m) 위치
    return LinearSelect(list, start, cur - 1, (start + (cur - 1)) // 2) # 재귀적으로 중앙값(M)을 구함

#피벗의 위치를 이용하여 피벗을 올바른 자리에 위치시키는 함수
def partition(list, start, end, pivot_pos):
    list[end], list[pivot_pos] = list[pivot_pos], list[end] # 피벗을 리스트의 끝으로 이동시킴
    pivot = list[end] # 끝으로 이동한 피벗의 값
    row = start # 피벗보다 작은 수를 위치시킬 인덱스

    for i in range(start, end + 1): # 리스트 순회
        if list[i] < pivot: # 피벗보다 작을 경우
            list[row],list[i] = list[i], list[row] # 피벗보다 작은 수를 위치시킴
            row += 1 # 다음 피벗보다 작은 수가 위치할 인덱스
    list[row], list[end] = list[end], list[row] # 피벗을 올바른 위치에 위치시킴
    return row # 피벗의 위치를 반환

def LinearSelect(list, start, end, k):
    if start == end: # 값이 1개일 거나 원하는 값을 못찾은 경우
        return list[start] # 그 값을 반환
    pivot_pos = choose_pivot(list, start, end) # 피벗의 위치를 구함
    partition_ = partition(list, start, end, pivot_pos) # 피벗의 올바른 위치를 구함

    if partition_ == k: # 원하는 위치와 피벗 위치가 일치한다면
        return partition_
    elif partition_ > k: # 피벗이 원하는 위치보다 크다면
        return LinearSelect(list, start, partition_-1, k)
    elif partition_ < k: # 피벗이 원하는 위치보다 작다면
        return LinearSelect(list, partition_+1, end, k)

def main():
    list1 = [31, 8, 48, 73, 11, 3, 20, 29, 65, 15]
    num = int(input("몇 번째 숫자를 찾을건가요?"))

    res = LinearSelect(list1, 0, len(list1) -1, num)

    print(f"{num} 번째 숫자는 {list1[num]} 입니다.")

if __name__ == '__main__':
    main()
