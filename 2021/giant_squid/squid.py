import re, copy

class Squid():


    def __init__(self) -> None:
        
        # extract data
        f = open('squid_data.txt', 'r')
        raw_data = f.readlines()

        self.sequence_data = list(map(int, re.findall("[0-9]+", raw_data[0])))

        # way too complicated way of getting the input rows
        board_data = [raw_data[x] for x in range(2, len(raw_data))]
        for x in range(0, len(board_data)):
            board_data[x] = re.findall("[0-9]+", board_data[x])
            board_data[x] = list(map(int, board_data[x]))
        board_data = [x for x in board_data if x != []]

        # get columns
        for z in range(0, len(board_data), 5):
            for x in range(5):
                tmp_column_list = []
                for y in range(z, z+5):
                    tmp_column_list.append(board_data[y][x])
                board_data.append(tmp_column_list)

        self.work_data = board_data
        self.copy_data = copy.deepcopy(self.work_data)



    def bingo(self) -> int:
        
        # run through sequence data while no nested lists are empty and delete the called elements
        # if one list is empty, take its index and sum up the unmarked elements
        # then multiply this number with the last element pulled from the sequence list

        for x in range(len(self.sequence_data)):
            if [] in self.copy_data:
                return self.sumUp(self.copy_data.index([])) * self.sequence_data[x-1]
            if any(self.sequence_data[x] in elem for elem in self.copy_data):
                self.removeElem(self.sequence_data[x])


    def removeElem(self, elem: int) -> None:
        for x in range(len(self.copy_data)):
            while elem in self.copy_data[x]:
                self.copy_data[x].remove(elem)

    
    # work-around bc i already forgot some details of the question during implementation...
    def sumUp(self, index) -> int:
        # getting the full board indices
        num_in_board = index % 5
        start_of_board = index - num_in_board

        return sum([sum(self.copy_data[x]) for x in range(start_of_board, start_of_board + 5)])


if __name__ == "__main__":
    one = Squid()
    print("output part one: ", one.bingo())
