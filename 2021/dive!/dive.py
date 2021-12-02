import re

class dive():

    def __init__(self) -> None:
        
        # get data
        f = open('sub_data.txt', 'r')
        self.raw_data = f.readlines()


    def multHorDep(self) -> int:

        horizontal_ctr = 0
        depth_ctr = 0

        for x in range(0, len(self.raw_data)):
            numb = int(re.findall("[0-9]+", self.raw_data[x])[0])
            if self.raw_data[x][0] == "f":
                horizontal_ctr += numb
            elif self.raw_data[x][0] == "d":
                depth_ctr += numb
            else:
                depth_ctr -= numb

        return horizontal_ctr * depth_ctr


    def useOfAim(self) -> int:

        horizontal_aim_ctr = 0
        depth_aim_ctr = 0
        aim = 0

        for x in range(0, len(self.raw_data)):
            numb = int(re.findall("[0-9]+", self.raw_data[x])[0])
            if self.raw_data[x][0] == "f":
                horizontal_aim_ctr += numb
                depth_aim_ctr += aim * numb
            elif self.raw_data[x][0] == "d":
                aim += numb
            else:
                aim -= numb

        return horizontal_aim_ctr * depth_aim_ctr


if __name__ == "__main__":
    sol = dive()
    print("mult. task: ", sol.multHorDep())
    print("mult_aim. task: ", sol.useOfAim())