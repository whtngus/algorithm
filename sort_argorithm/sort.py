class Sort():

    def get_sort(self,sort_name,runner_len):
        self.runner_len = runner_len
        sort_history = None
        if sort_name == "select":
            sort_history = self._select_sort
        elif sort_name == "shell":
            sort_history = self._shell_sort
        elif sort_name == "insert":
            sort_history = self._insert_sort
        elif sort_name == "bubble":
            sort_history = self._bubble_sort
        elif sort_name == "heap":
            sort_history = self._heap_sort
        elif sort_name == "merge":
            sort_history = self._merge_sort
        elif sort_name == "quick":
            sort_history = self._quick_sort
        return sort_history

    def _quick_sort(self, runner, start, end):
        if start > end:
            return
        pivot = self._quick_partition(runner, start, end)
        print("pivot-{}  : {}".format(pivot, runner))
        self._quick_sort(runner, start, pivot - 1)
        self._quick_sort(runner, pivot + 1, end)

    def _quick_partition(self, runner, start, end):
        target = runner[start][1]
        target_index = start

        def compare(start, stop, is_big,move):
            while (start < stop) == is_big and (target > runner[start][1]) == is_big:
                start += move
            return start

        start += 1
        while True:
            start = compare(start, end, True,1)
            end = compare(end, start, False,-1)
            if start >= end:
                break
            runner[start], runner[end] = runner[end], runner[start]
            start += 1
            end -= 1
        runner[target_index], runner[end] = runner[end], runner[target_index]
        return end

    def _merge_sort(self, runner):
        def merge_sort(left, right):
            sort = []
            left_len = len(left)
            right_len = len(right)
            left_index = 0
            right_index = 0
            while True:
                if left_index < left_len and right_index < right_len:
                    if left[left_index][1] > right[right_index][1]:
                        sort.append(right[right_index])
                        right_index += 1
                    else:
                        sort.append(left[left_index])
                        left_index += 1
                elif left_index < left_len:
                    sort.append(left[left_index])
                    left_index += 1
                elif right_index < right_len:
                    sort.append(right[right_index])
                    right_index += 1
                else:
                    break
            return sort

        if len(runner) <= 1:
            return runner
        runner_split = len(runner) // 2
        left = runner[:runner_split]
        right = runner[runner_split:]
        left = self._merge_sort(left)
        right = self._merge_sort(right)
        result = merge_sort(left, right)
        print("{}와{}합침 : {}".format(left, right, result))
        return result

    def _heap_sort(self, runner):
        def check(index):
            change_index = index * 2
            if limit > change_index + 1 and runner[change_index + 1][1] > runner[change_index][1]:
                change_index += 1
            if runner[index][1] < runner[change_index][1]:
                runner[index], runner[change_index] = runner[change_index], runner[index]
                if change_index * 2 < limit:
                    check(change_index)

        runner.insert(0, 0)
        # 힙 정렬 하기
        for memo in self._init_heap(runner):
            yield memo, runner[1:]
        runner_len = self.runner_len
        # 큰값 하나씩 뒤로
        for limit in range(runner_len, 1, -1):
            runner[1], runner[limit] = runner[limit], runner[1]
            if 2 < limit:
                check(1)
            yield "heap sort", runner[1:]
        del runner[0]

    def _init_heap(self, runner):
        def check(index):
            change_index = index * 2
            if runner_len > change_index and runner[change_index + 1][1] > runner[change_index][1]:
                change_index += 1
            if runner[index][1] < runner[change_index][1]:
                runner[index], runner[change_index] = runner[change_index], runner[index]
                if runner_len >= change_index * 2:
                    check(change_index)

        runner_len = self.runner_len - 1
        for index in range(len(runner) // 2, 0, -1):
            check(index)
            yield "정렬중"

    def _shell_sort(self, runner):
        runner_len = self.runner_len
        gap = runner_len
        while gap != 1:
            gap = int(gap / 2)
            # gap = gap + 1 if gap % 2 == 0 else gap
            for i in range(gap):
                gap_list = runner[i:runner_len:gap]
                # 한번만 실행됨
                for insert_sort in self._insert_sort(gap_list, False):
                    runner[i:runner_len:gap] = insert_sort
            yield "gap={} ".format(gap), runner

    def _bubble_sort(self, runner):
        runner_len = self.runner_len
        for change_index in range(runner_len - 1):
            for index in range(runner_len - change_index - 1):
                if runner[index][1] > runner[index + 1][1]:
                    runner[index], runner[index + 1] = runner[index + 1], runner[index]
            yield "Step", runner

    def _select_sort(self, runner):
        runner_len = self.runner_len
        for change_index in range(runner_len - 1):
            local_min_index = change_index
            local_min_time = runner[change_index][1]
            for index in range(change_index, runner_len):
                if runner[index][1] < local_min_time:
                    local_min_index = index
                    local_min_time = runner[index][1]
            runner[change_index], runner[local_min_index] = runner[local_min_index], runner[change_index]
            yield "Step", runner

    def _insert_sort(self, runner, history=True):
        runner_len = len(runner)
        for change_index in range(1, runner_len):
            for index in range(change_index, 0, -1):
                if runner[index][1] > runner[index - 1][1]:
                    break
                runner[index], runner[index - 1] = runner[index - 1], runner[index]
            if history:
                yield "Step", runner
        if not history:
            yield runner