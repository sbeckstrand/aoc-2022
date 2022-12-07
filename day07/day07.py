input = open("input.txt", "r")
commands = input.read().splitlines()
input.close()

# Class for tracking File object types
class SystemFile:
    def __init__(self, parent, name, size):
        self.name = name
        self.size = size
        self.parent= parent

# Class for tracking Directory object types
class Dir:
    def __init__(self, parent, name):
        self.name = name
        self.size = 0
        self.parent = parent
        self.children = []
        self.files = []

    # Function to check if a child directory already exists, if so, retrieve it
    def get_child(self, name):
        result_child = None
        for child in self.children:
            if child.name == name:
                result_child = child
        
        return result_child
    
    # Function to check if a file already exists, if so, retrieve it
    def get_file(self, name):
        result_file = None
        for file in self.files:
            if file.name == name:
                result_file = file

        return result_file

# Recursive function to set size of directories based on child directories 
# and to calculate size of directories under the specified max size
def calc_size(dir, record_size, max_size):
    updated_record_size = record_size
    if len(dir.children) > 0:
        for child in dir.children:
            size_update, record_update = calc_size(child, record_size, max_size)
            updated_record_size += record_update
            dir.size += size_update 
        
    for file_obj in dir.files:
        dir.size += file_obj.size

    if dir.size < max_size:
        updated_record_size += dir.size

    return dir.size, updated_record_size

# Recursive function to find the smallest file that can be deleted 
# and meet the requirement for the amount of space needed to free up
def del_smallest_needed(dir, del_size):
    smallest_needed = dir
    if len(dir.children) > 0:
        for child in dir.children:
            smallest_in_path = del_smallest_needed(child, del_size)
            size_diff = smallest_in_path.size - del_size
            if size_diff > 0 and size_diff < smallest_needed.size - del_size:
                smallest_needed = smallest_in_path
                
    return smallest_needed
    
# Takes a series of command line input and builds the tree of directories and files. 
def build_dir_map(commands, max_size=100000, del_files=False):
    root_dir = None
    curr_dir = None

    for line in commands: 
            
        if line.startswith("$ cd"):
            
            directory = line.split("$ cd ")[1]
            
            if directory == "/":
                if root_dir == None:
                    root_dir = Dir(None, "/")
                    curr_dir = root_dir
            elif directory == "..":
                curr_dir = curr_dir.parent
            else:
                child_dir = curr_dir.get_child(directory)
                if child_dir == None:
                    child_dir = Dir(curr_dir, directory)
                    curr_dir.children.append(child_dir)
                curr_dir = child_dir
            
        # If command starts with dir, create the directory under current directory if it doesnt already exist
        elif line.startswith("dir"):
            dir_name = line.split(" ")[1]
            if curr_dir.get_child(dir_name) == None:
                child = Dir(curr_dir, dir_name)
                curr_dir.children.append(child)

        # Check if a file, if so, create it under current directory if it doesnt already exist. 
        elif line[0].isdigit():
            file_props = line.split(" ")
            file_name, file_size = file_props[1], int(file_props[0])
            if curr_dir.get_file(file_props[1]) == None:
                new_file = SystemFile(curr_dir, file_name, file_size)
                curr_dir.files.append(new_file)

    _, record_size = calc_size(root_dir, 0, max_size)

    if del_files:
        needed_space = 30000000 - (70000000 - root_dir.size)
        return del_smallest_needed(root_dir, needed_space).size
    else:
        return record_size

print(build_dir_map(commands))
print(build_dir_map(commands, del_files=True))