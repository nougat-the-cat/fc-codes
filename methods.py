def unhyphen(string):
    clean = string.replace("-", "").replace(".", "").replace("_", "").replace(" ", "")
    return clean

def swapcase(codes):
    swapped = ""
    for i in range(len(codes)):
        swapped += codes[i].swapcase()
    return swapped

def swap(string, pos1, pos2):
    string = list(string)
    string[pos1], string[pos2] = string[pos2], string[pos1]
    string = ''.join(string)
    return string

def first_letter(string):
    for i in range(len(string)):
        if string[i].isalpha():
            return i

def last_letter(string):
    for i in range(len(string)-1, -1, -1):
        if string[i].isalpha():
            return i

def swap_letters(string):
    pos1 = first_letter(string)
    pos2 = last_letter(string)
    string = swap(string, pos1, pos2)
    return string
 
def del_highest(string):
  char_list = list(string)
  highest_number = -1
  
  for i, c in enumerate(char_list):
    if c.isdigit():
      if int(c) > highest_number:
        highest_number = int(c)
        highest_number_index = i
  
  del char_list[highest_number_index]
  return ''.join(char_list)

def del_lowest(string):
  char_list = list(string)
  lowest_number = float('inf')
  
  for i, c in enumerate(char_list):
    if c.isdigit():
      if int(c) < lowest_number:
        lowest_number = int(c)
        lowest_number_index = i
  
  del char_list[lowest_number_index]  
  return ''.join(char_list)
