import os
#the path
path = os.path.join(os.getcwd(),"testdir")
#the suffix we are looking for
suffix = ".c"
# def find_files(suffix, path):
#     file_list=set()
#     def find_in_subdir(suffix, path):
#         if path.endswith(suffix):
#             file_list.add(path)
#             return
#         if os.path.isdir(path):
#             for element in os.listdir(path):
#                 net_path=os.path.join(path, element)
#                 find_in_subdir(suffix, net_path)
#         return file_list
#     return find_in_subdir(suffix, path)
# print(find_files(suffix, path))

def find_files(suffix, path):
    global file_list
    file_list=set()
    return find_in_subdir(suffix, path)
def find_in_subdir(suffix, path):
    if path.endswith(suffix):
        file_list.add(path)
        return
    if os.path.isdir(path):
        for element in os.listdir(path):
            net_path=os.path.join(path, element)
            find_in_subdir(suffix, net_path)
    return file_list
# def find_in_subdir(suffix, path, file_list):
#     if path.endswith(suffix):
#         return path
#     if os.path.isdir(path):
#         for element in os.listdir(path):
#             net_path=os.path.join(path, element)
#             append=find_in_subdir(suffix, net_path, file_list)
#             print(type(append))
#             if len(append)!=0:
#                 file_list.append(append)
#     return file_list
print(find_files(suffix, path))
