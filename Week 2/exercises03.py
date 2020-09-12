import webget as webget

file = 'read_from_file_ex.txt'


def print_file_conent(file):
  with open(file) as file_object:
    contents = file_object.read()

    print(contents)

print_file_conent(file)

#def write_list_to_file(output_file, lst) that can take a list or tuple and write each element to a new line in file
#create a helper function that gets an arbitrary number of strings instead of a list

outputFile = 'output_file_ex03.txt'
wordList = ['Derka','Derk','Derpsen','Papi']

def write_list_to_file(output_file, lst):
  with open(output_file, 'w') as file_object:
    for i in range(len(lst)):
      file_object.write(lst[i] + '\n')


write_list_to_file(outputFile, wordList)

#def read_file(input_file) that take a csv file and read each row into a list



def read_file(input_file):
    with open(input_file) as f_obj:
        content = f_obj.readlines()
        file_list = []
        
    for line in content:
        file_list.append(line.strip().split(','))
        
    print(file_list)

read_file('sample_csv.csv')