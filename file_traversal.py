import os, sys
import re

HOME_PATH = '.'
MAC_FOLDER_PATTERN = '\w{2}_\w{2}_\w{2}_\w{2}_\w{2}_\w{2}' # re_match
IP_FOLDER_PATTERN = '\.\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
FILE_PATTERN = '\d{4}-\d{2}-\d{2}\.log\.\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'


class FileTraversal:
    def __init__(self):
        self.depth_str = '|   '
        self.expand_folder_format = '+- <{folder_name}>'
        self.expand_file_format = '+- {file_name}'


    def traversal_path(self, node_name: str, depth: int=0):
        node_name = os.path.normpath(node_name)

        if os.path.exists(node_name):
            current_depth_str = self.depth_str * depth

            current_name = node_name.split('\\')[-1]
            if os.path.isdir(node_name):
                self.writeline_data(current_depth_str + self.expand_folder_format.format(folder_name=current_name))

                full_path_name = node_name
                file_list = os.listdir(node_name)
                for file_name in file_list:
                    self.traversal_path(os.path.join(full_path_name, file_name), depth + 1)
            else:
                self.writeline_data(current_depth_str + self.expand_file_format.format(file_name=current_name))


    def writeline_data(self, string: str):
        print(string)


    def check_folder_name(folder_name: str):


if __name__ == "__main__":

    path = r'..'
    obj = FileTraversal()
    obj.traversal_path(path, 0)

    pass