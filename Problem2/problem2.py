import os

#the find_files function
def find_files(suffix, path):
    global file_list
    file_list=list()
    return find_in_subdir(suffix, path)
#recursive function which returns the set of
def find_in_subdir(suffix, path):
    #base case which appends the path into the list if suffix matches
    if path.endswith(suffix):
        file_list.append(path)
        return
    #if path is directory then we need to look inside it
    if os.path.isdir(path):
        for element in os.listdir(path):
            net_path=os.path.join(path, element)
            find_in_subdir(suffix, net_path)
    return file_list


#Given Testcase
path = os.path.join(os.getcwd(),"testdir")#root
suffix = ".c"#suffix we are looking for
print(find_files(suffix, path))

#Testcase2
path = os.path.join(os.getcwd(),"problems")#root
suffix = ".py"#suffix we are looking for
print(find_files(suffix, path))
