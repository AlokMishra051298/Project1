import os

#the find_files function
def find_files(suffix, path):
    global file_list
    file_list=list()
    return find_in_subdir(suffix, path)
#recursive function which returns the set of
def find_in_subdir(suffix, path):
    #base case which appends the path into the list if suffix matches
    if os.path.isfile(path) and path.endswith(suffix):
        file_list.append(path)
        return
    #if path is directory then we need to look inside it
    if os.path.isdir(path):
        for element in os.listdir(path):
            net_path=os.path.join(path, element)
            find_in_subdir(suffix, net_path)
    return file_list


#Given Testcase
print("-----------------TEST CASE 1-----------------")
print(os.getcwd())
path = os.path.join(os.path.join(os.getcwd(),"Problem2"),"testdir")#root
suffix = ".c"#suffix we are looking for
print(find_files(suffix, path))

#Testcase2
print("-----------------TEST CASE 2-----------------")
path = os.path.join(os.path.join(os.getcwd(),"Problem2"),"problems")#root
suffix = ".py"#suffix we are looking for
print(find_files(suffix, path))

#Testcase3
print("-----------------TEST CASE 3-----------------")
path = os.path.join(os.path.join(os.getcwd(),"Problem2"),"P0")#root
suffix = ".csv"#suffix we are looking for
print(find_files(suffix, path))
