class BHeap:
    def __init__(self, a):  # 생성자
        self.a = a  # a[0] 사용 안함
        self.N = len(a) - 1  # 힙의 항목 수

    def create_heap(self):  # 초기 힙 만들기
        for i in range(self.N // 2, 0, -1):
            self.downheap(i)

    def insert(self, key_value):  # 삽입 연산
        self.N += 1
        self.a.append(key_value)  # 새로운 키(항목)를 맨 끝에 저장
        self.upheap(self.N)  # 위로 올라가며 힙속성 회복시키기 위해

    def delete_min(self):  # 최솟값 삭제
        if self.N == 0:  # underflow 경우
            print('힙이 비어 있음')
            return None
        minimum = self.a[1]  # a[1]의 최솟값을 minimum에 저장하여 리턴
        self.a[1], self.a[-1] = self.a[-1], self.a[1]  # 힙의 마지막 항목과 교환
        del self.a[-1]  # 힙의 마지막 항목 삭제
        self.N -= 1
        self.downheap(1)  # 힙속성을 회복시키기 위해
        return minimum

    def downheap(self, i):  # 힙 내려가며 힙속성 회복
        while 2 * i <= self.N:  # i의 왼쪽자식이 힙에 있으면
            k = 2 * i  # k는 왼쪽자식의 인덱스
            if k < self.N and self.a[k][0] > self.a[k + 1][0]:  # 왼쪽과 오른쪽자식의 승자를 결정하여 k가 승자의 인덱스가됨
                k += 1
            if self.a[i][0] < self.a[k][0]:
                break  # 현재 노드가 자식 승자보다 작으면, 루프를 중단하고
            self.a[i], self.a[k] = self.a[k], self.a[i]  # 현재 노드가 자식 승자보다 크면 현재 노드와 자식 승자와 교환
            i = k  # 자식 승자가 현재 노드가 되어 다시 반복하기 위해

    def upheap(self, j):  # 힙 올라가며 힙속성 회복
        while j > 1 and self.a[j // 2][0] > self.a[j][0]:  # 현재노드가 루트가 아니고 동시에 부모가 크면
            self.a[j], self.a[j // 2] = self.a[j // 2], self.a[j]  # 부모와 현재 노드 교환
            j = j // 2  # 부모가 현재 노드가 되어 다시 반복하기 위해

    def print_heap(self):  # 힙 출력
        for i in range(1, self.N + 1):
            print('[%2d' % self.a[i][0], self.a[i][1], ']', end='')
        print('\n힙 크기 = ', self.N)