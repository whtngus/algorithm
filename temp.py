from binary_heap import BHeap

b_heap = BHeap([None])
while True:
    command = input("삽입(i), 삭제(d) : ")
    if command == "i":
        memo = input("할일 : ")
        priority = input("우선순위 : ")
        b_heap.insert([int(priority),memo])
    elif command == "d":
        print("제일 우선순위가 높은 일은 \"{}\" 입니다.".format(b_heap.delete_min()[1]))
    else:
        print("메뉴선택 다시 하세요.")
        break
    # 공백 출력
    print()