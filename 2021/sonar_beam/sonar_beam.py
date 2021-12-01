class sonar_beam():        

    def algorithm(self, work_list) -> int:

        inc_count = 0
        prev_elem = 0
        for x in range(0, len(work_list)):
            if x > 0:
                if prev_elem < work_list[x]:
                    inc_count += 1
            prev_elem = work_list[x]

        return inc_count

    def getWorkData(self):

        f = open('sonar_data.txt', 'r')
        raw_data = f.readlines()

        # iterate through data to get rid of \n
        for x in range(0, len(raw_data)):
            # deletes last char of the list of strings
            raw_data[x] = raw_data[x][:len(raw_data[x])-1]

        # count the elements where the previous element is lower
        work_list = list(map(int, raw_data))
        return work_list

    def first_task(self) -> int:

        work_list = self.getWorkData()
        return self.algorithm(work_list)


    def second_task(self) -> int:

        work_list = self.getWorkData()

        # create new list with the sums of the three measurement window
        sum_list = []

        # iterate through data list with 3 element window
        for x in range(0, len(work_list)):
            if x+2 > len(work_list)-1:
                break
            sum_list.append(work_list[x] + work_list[x+1] + work_list[x+2])

        return self.algorithm(sum_list)


if __name__ == "__main__":
    test = sonar_beam()
    print("first task: ", test.first_task())
    print("second task: ", test.second_task())