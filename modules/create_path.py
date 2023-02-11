import os
def create_path(name_image):
    path_file = os.path.abspath(__file__)
    # print(path_file)
    path_file = path_file.split("\\")
    for i in range(2):
        del path_file[-1]
    path_file = "/".join(path_file)
    path_file = os.path.join(path_file, name_image)
    return path_file
    