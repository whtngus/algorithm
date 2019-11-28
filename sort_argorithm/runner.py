from sort import Sort
class Runner():
    def __init__(self):
        self.sort_collection = Sort()

    def sort(self, runner,sort_history,top):
        for i, (memo, history) in enumerate(sort_history(runner)):
            print("{} {}".format(memo, i + 1), end=" : ")
            for runner_info in history:
                print("{}\t".format(runner_info[1]), end="\t")
            print()
        self._result_print(runner, top)

    def run(self,sort_name, runner, top=3):
        # start history print
        runner_len = len(runner)
        self._start_history(runner)
        # sort setting
        print("=========================================")
        sort_history = self.sort_collection.get_sort(sort_name, runner_len)
        print("{} sort start".format(sort_name))
        if sort_name == "merge":
            result = self.sort_collection._merge_sort(runner)
            self._result_print(result, top)
            return
        elif sort_name == "quick":
            self.sort_collection._quick_sort(runner, 0, runner_len - 1)
            self._result_print(runner, top)
            return
        elif sort_name == None:
            return
        self.sort(runner, sort_history, top)
        print("=========================================")

    def _result_print(self, result, top):
        for i in range(top):
            print("{} 등 : {}번 {}".format(i + 1, result[i][0], self._s_to_time(result[i][1])))

    def _start_history(self, runner):
        # sort history print
        print("정렬 전", end=" : ")
        for runner_info in runner:
            print("{}".format(runner_info[1]), end="\t")
        print()

    def _s_to_time(self, second):
        h = second // 3600
        second -= h * 3600
        m = second // 60
        s = second % 60
        return "{}시간 {}분 {}초".format(h, m, s)

'''
input
8
8110
8132
8076
7939
7955
7840
7523
8041

7523   7840   7939   7955   8041   8076   8110   8132 

8
7930
7523
8192
7498
7347
8090
7983
8041

'''
if __name__ == "__main__":
    number = input("마라토너 수를 입력하시오 : ")
    marathon_runner = []
    print("마라토너의 기록을 초단위로 입력 : ")
    for i in range(int(number)):
        marathon_runner.append([i + 1, int(input())])
    runner = Runner()
    runner.run("select",marathon_runner[:])
    runner.run("insert",marathon_runner[:])
    runner.run("shell",marathon_runner[:])
    runner.run("bubble",marathon_runner[:])
    runner.run("heap",marathon_runner[:])
    runner.run("merge", marathon_runner[:])
    runner.run("quick", marathon_runner[:])
