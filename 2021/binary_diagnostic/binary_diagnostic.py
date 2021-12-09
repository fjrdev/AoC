class BinaryDiagnostic():
  
  def __init__(self) -> None:
  
    f = open('bin_data.txt', 'r')
    raw_data = f.readlines()

    self.work_data = []
    for x in range(len(raw_data)):
      self.work_data.append(raw_data[x][:len(raw_data[x])-1])


  def getMostCommonElem(self, index_list) -> str:
    one = zero = 0

    for x in range(0, len(index_list)):
      if index_list[x] == "0":
        zero += 1
      else:
        one += 1

    if one < zero:
      return "0"
    return "1"  

  # Algorithm for first task
  def multGamEps(self) -> int:
    gamma = ""

    for x in range(0, 12):
      tmp_list = [] 
      for y in range(0, len(self.work_data)):
        tmp_list.append(self.work_data[y][x])
      gamma += self.getMostCommonElem(tmp_list)
    
    epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])
    return int(gamma, 2) * int(epsilon, 2)

  # Algorithm for second task
  def shrinkList(self, mc: bool) -> str:
    wd_list = self.work_data

    for x in range(0, 12):
      tmp_list = []
      if len(wd_list) == 1: break
      
      for y in range(0, len(wd_list)):
        tmp_list.append(wd_list[y][x])
      cn = self.getMostCommonElem(tmp_list)

      if mc == True:
        wd_list = [elem for elem in wd_list if elem[x] == cn]
      else: 
        wd_list = [elem for elem in wd_list if elem[x] != cn]

    return wd_list[0]


  def lifeSupportRating(self) -> int:

    # get oxygen generator rating
    ogr = self.shrinkList(True)

    # get CO2 scrubber rating
    csr = self.shrinkList(False)

    return int(ogr, 2) * int(csr, 2)

      
if __name__ == "__main__":
  bd = BinaryDiagnostic()
  print("first task: ", bd.multGamEps())
  print("second task: ", bd.lifeSupportRating())