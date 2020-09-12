import os



# """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
def get_file_names(dir_path, output_file):
  dir_list = os.listdir(dir_path)
  with open(output_file, 'w') as file_object:
    for line in dir_list:
      file_object.write(line + "\n")

get_file_names('./', 'file-names.txt')

#  """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
def get_all_file_names(path,output_file):
  file_list = []
  for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
      file_list.append(os.path.join(root, name))
    for name in dirs:
      file_list.append(os.path.join(root, name))
  with open(output_file, 'w') as file_object:
    for line in file_list:
      file_object.write(line + '\n')

get_all_file_names('./../../', 'files-and-subfolders.txt')


# """takes a list of filenames and print the first line of each"""

def print_line_one(file_list):
    for file in file_list:
        with open(file,'r') as file_object:
            print("First line in: " + file + "\n" + file_object.readlines()[0])
lst_files = ['./file-names.txt','./input-file.txt']
print_line_one(lst_files);

#"""takes a list of filenames and print each line that contains an email (just look for @)"""
def print_emails(file_names):
    for file in file_names:
      with open(file,'r') as file_object:
        for line in file_object.readlines():
          if '@' in line:
            print(line)


email_list = ['./email-list01.txt','./email-list02.txt']
print_emails(email_list)

#    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
def write_headlines(md_files, output_file):
    output_list = []
    for file in md_files:
      with open(file, 'r') as file_object:
           for line in file_object.readlines():
              if line[0] == '#':
                  output_list.append(line);
      with open(output_file, 'w') as file_object:
           for line in output_list:
              file_object.write(line)
   

md_list = ['./md-files/file-one.md','./md-files/file-two.md']



def fifth_function(lst, output_file):
    lines_to_output = []
    for file in lst:
        with open(file,'r') as file_object:
            for line in file_object.readlines():
                if line[0] == "#":
                    lines_to_output.append(line);
        with open(output_file, 'w') as file_object:
            for line in lines_to_output:
                file_object.write(line)


write_headlines(md_list, './headlines-output.txt')