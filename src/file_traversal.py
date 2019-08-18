import os, sys
import re
from enum import Enum


class FileInfo:
    FILE_SIZE = 'file_size'
    FILE_CNT = 'file_cnt'

    @classmethod
    def gen_info(cls, file_size: int, file_cnt: int):
        res_info = {}
        res_info[FileInfo.FILE_SIZE] = file_size
        res_info[FileInfo.FILE_CNT] = file_cnt
        return res_info


class FileTraversal:
    """
    Attributes:
        depth_str(str): the duplicate string dependents on the depth
        expand_folder_format(str): the output string format for a folder
        expand_file_format(str): the output string format for a file
        pass_folder_name(list): the re-expression list for pass folder_name
        pass_file_name(list): the re-expression list for pass file_name
    """
    def __init__(self):
        """
        Initialize module
        """
        self.depth_str = '|   '
        self.expand_folder_format = '+- <{folder_name}>'
        self.expand_file_format = '+- {file_name}'
        self.pass_folder_re_list = []
        self.pass_file_re_list = []
        self.detail_folder_format = '+- <{folder_name}> [CNT = {file_cnt:d}, SIZE = {file_size:.2f} KB]'
        self.detail_file_format = '+- {file_name} [SIZE = {file_size:.2f} KB]'


    def simple_traversal(self, node_name: str, depth: int=0):
        """
        traversal in a given path and output the path structure

        Args:
            node_name(str): the current file/folder name
            depth(int): the relative depth to root
        """

        node_name = os.path.normpath(node_name)

        if os.path.exists(node_name):
            current_depth_str = self.depth_str * depth

            current_name = os.path.basename(node_name)
            if os.path.isdir(node_name):
                self.writeline_data(current_depth_str + self.expand_folder_format.format(folder_name=current_name))

                full_path_name = node_name
                file_list = os.listdir(node_name)
                for file_name in file_list:
                    self.simple_traversal(os.path.join(full_path_name, file_name), depth + 1)
            else:
                self.writeline_data(current_depth_str + self.expand_file_format.format(file_name=current_name))


    def execute_detail_traversal(self, root_name: str):
        node_list = []
        self.detail_traversal(node_list=node_list, node_name=root_name, depth=0)
        node_list.reverse()
        for line in node_list:
            print(line)


    def detail_traversal(self, node_list: list, node_name: str, depth: int=0):
        """
        traversal in a given path and output the path structure

        Args:
            node_list(list of str): store information of the path structure
            node_name(str): the current file/folder name
            depth(int): the relative depth to root

        Return:
            file_info(dict): {'file_num': count, 'file_size': KB}
        """

        file_size = 0
        file_cnt = 0
        node_name = os.path.normpath(node_name)
        if not os.path.exists(node_name):
            return FileInfo.gen_info(file_size, file_cnt)

        current_depth_str = self.depth_str * depth
        current_name = os.path.basename(node_name)
        if os.path.isdir(node_name):
            if self.check_folder_name(current_name):
                file_list = self.sorted_listdir(node_name)
                for file_name in file_list:
                    tmp_info = self.detail_traversal(node_list, os.path.join(node_name, file_name), depth + 1)
                    file_size += tmp_info[FileInfo.FILE_SIZE]
                    file_cnt += tmp_info[FileInfo.FILE_CNT]

                res_str = current_depth_str + \
                          self.detail_folder_format.format( \
                          folder_name=current_name, file_size=file_size, file_cnt=file_cnt)
                node_list.append(res_str)
                file_cnt += 1
        else:
            if self.check_file_name(current_name):
                stat_info = os.stat(node_name)
                file_size += stat_info.st_size / 1024
                file_cnt += 1
                res_str = current_depth_str + \
                        self.detail_file_format.format( \
                        file_name=current_name, file_size=file_size)
                node_list.append(res_str)
            
        return FileInfo.gen_info(file_size, file_cnt)


    def writeline_data(self, string: str):
        print(string)


    def sorted_listdir(self, node_name: str):
        """
        sort the current path, and put folders in fornt of files
        """
        
        sorted_files = []
        sorted_folders = []
        if os.path.exists(node_name) and os.path.isdir(node_name):
            file_list = os.listdir(node_name)
            for crt_name in file_list:
                full_path = os.path.join(node_name, crt_name)
                if os.path.isdir(full_path):
                    sorted_folders.append(crt_name)
                else:
                    sorted_files.append(crt_name)
        res_list = sorted_files + sorted_folders
        res_list.reverse()
        return res_list


    def compile_pass_folder_list(self, folder_name_patterns: list):
        self.pass_folder_re_list = []
        for pattern in folder_name_patterns:
            self.pass_folder_re_list.append(re.compile(pattern))


    def check_folder_name(self, folder_name: str):
        """
        Args:
            folder_name(str): the folder_name we want to check

        Returns:
            True/False: folder_name is in re-list: True, o.w.: False
        """
        if isinstance(self.pass_folder_re_list, list):
            if len(self.pass_folder_re_list) == 0:
                return True

            for re_obj in self.pass_folder_re_list:
                mathc_info = re_obj.match(folder_name)
                if mathc_info is not None:
                    return True
            return False
        else:
            return True


    def compile_pass_file_list(self, file_name_patterns: list):
        self.pass_file_re_list = []
        for pattern in file_name_patterns:
            self.pass_file_re_list.append(re.compile(pattern))

    
    def check_file_name(self, file_name: str):
        """
        Args:
            file_name(str): the file_name we want to check

        Returns:
            True/False: file_name is in re-list: True, o.w.: False
        """
        if isinstance(self.pass_file_re_list, list):
            if len(self.pass_file_re_list) == 0:
                return True

            for re_obj in self.pass_file_re_list:
                mathc_info = re_obj.match(file_name)
                if mathc_info is not None:
                    return True
            return False
        else:
            return True



def test_simple_traversal():
    path = r'./data'
    obj = FileTraversal()
    obj.simple_traversal(path, 0)


def test_detail_traversal():
    path = r'./data'
    obj = FileTraversal()
    obj.execute_detail_traversal(path)


def test_condition_detail_traversal():
    path = r'./data'
    
    file_pattern1 = '.+\.py'
    file_pattern2 = '.+\.log'
    file_pattern_list = [file_pattern1, file_pattern2]

    obj = FileTraversal()
    obj.compile_pass_file_list(file_pattern_list)

    obj.execute_detail_traversal(path)


if __name__ == "__main__":
    #test_condition_detail_traversal()
    #test_detail_traversal()
    test_simple_traversal()

