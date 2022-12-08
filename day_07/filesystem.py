from pprint import pprint

class File:

    def __init__(self, path, size):
        self.path = path
        self.size = size

    def get_size(self):
        return self.size

    def __repr__(self):
        return f'File[{self.path}, {self.size}]'


class Directory:
    
    def __init__(self, path, children, filesystem):
        self.path = path
        self.children = children
        self.filesystem = filesystem

    def get_size(self):

        if len(self.children) == 0:
            return 0

        size = 0
        for child_name in self.children:
            child_path = self.path + (child_name, )
            child = filesystem[child_path]
            size += child.get_size()
            
        return size

    def __repr__(self):
        return f'Directory[{self.path}, {self.get_size()}]'


if __name__ == '__main__':

    current_dir = ['/', ]
    current_children = []
    filesystem = dict()

    with open('data/input.txt') as f:
        for line in f:            
            line = line.strip()

            if line.startswith('$ '):
                command_s = line[2:]

                if len(current_children) > 0:
                    dir_path = tuple(current_dir)
                    filesystem[dir_path] = Directory(dir_path, current_children, filesystem)
                
                if command_s.startswith('cd'):
                    current_children = []

                    target = command_s.split('cd ')[-1]
                    
                    if target == '/':
                        current_dir = ['/', ]
                    elif target == '..':
                        current_dir = current_dir[:-1]
                    else:
                        current_dir.append(target)
                    
            else:
                prefix, name = line.split(' ')
                if prefix != 'dir':
                    file_size = int(prefix)
                    file_path = tuple(current_dir) + (name, )
                    filesystem[file_path] = File(file_path, file_size)

                current_children.append(name)

    dir_path = tuple(current_dir)
    filesystem[dir_path] = Directory(dir_path, current_children, filesystem)


    AVAILABLE = 70_000_000 - filesystem[('/', )].get_size()
    NEEDED = 30_000_000

    result = 0
    candidates = []
    for k, v in filesystem.items():
        if type(v) == Directory:
            s = v.get_size()
            if s <= 100_000:
                result += s

            if AVAILABLE + s >= NEEDED:
                candidates.append(s)

    print(result, min(candidates))
