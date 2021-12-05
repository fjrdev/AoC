class sonar_beam():

    def __init__(self) -> None:

        f = open('sonar_data.txt', 'r')
        raw_data = f.readlines()

        # get rid of \n
        for x in range(0, len(raw_data)):
            # deletes last char
            raw_data[x] = raw_data[x][:len(raw_data[x])-1]

        self.work_list = list(map(int, raw_data))    


    def algorithm(self, work_list) -> int:

        inc_count = prev_elem = 0
        for x in range(0, len(work_list)):
            if x > 0:
                if prev_elem < work_list[x]:
                    inc_count += 1
            prev_elem = work_list[x]

        return inc_count


    def first_task(self) -> int:
        return self.algorithm(self.work_list)


    def second_task(self) -> int:
        sum_list = []

        # iterate through data list with 3 element window
        for x in range(0, len(self.work_list)):
            if x+2 > len(self.work_list)-1:
                break
            sum_list.append(self.work_list[x] + self.work_list[x+1] + self.work_list[x+2])

        return self.algorithm(sum_list)


if __name__ == "__main__":
    test = sonar_beam()
    print("first task: ", test.first_task())
    print("second task: ", test.second_task())