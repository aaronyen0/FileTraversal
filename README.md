# FileTraversal
Traversal from a given path. Output the path structure.

## Demo

- Simple Case
    ```python
    path = r'./data'
    obj = FileTraversal()
    obj.simple_traversal(path, 0)

    """ Result

    +- <data>
    |   +- <folder1>
    |   |   +- minesweeper_debug_log.txt
    |   +- <folder2>
    |   |   +- <folder2_1>
    |   |   |   +- PY1.py
    |   |   |   +- PY2.py
    |   |   +- <folder2_2>
    |   +- LOG1.log
    |   +- LOG2.log
    |   +- TXT1.txt
    |   +- TXT2.txt
    |   +- TXT3.txt
    """

    ```


- Detail Info Case
    ```python
    path = r'./data'
    obj = FileTraversal()
    obj.execute_detail_traversal(path)

    """ Result

    +- <data> [CNT = 12, SIZE = 4.24 KB]
    |   +- LOG1.log [SIZE = 0.02 KB]
    |   +- LOG2.log [SIZE = 0.12 KB]
    |   +- TXT1.txt [SIZE = 0.00 KB]
    |   +- TXT2.txt [SIZE = 0.00 KB]
    |   +- TXT3.txt [SIZE = 0.00 KB]
    |   +- <folder1> [CNT = 1, SIZE = 0.86 KB]
    |   |   +- minesweeper_debug_log.txt [SIZE = 0.86 KB]
    |   +- <folder2> [CNT = 4, SIZE = 3.24 KB]
    |   |   +- <folder2_1> [CNT = 2, SIZE = 3.24 KB]
    |   |   |   +- PY1.py [SIZE = 0.02 KB]
    |   |   |   +- PY2.py [SIZE = 3.23 KB]
    |   |   +- <folder2_2> [CNT = 0, SIZE = 0.00 KB]
    """

    ```


- Condition Case
    ```python
    path = r'./data'
    
    file_pattern1 = '.+\.py'
    file_pattern2 = '.+\.log'
    file_pattern_list = [file_pattern1, file_pattern2]

    obj = FileTraversal()
    obj.compile_pass_file_list(file_pattern_list)

    obj.execute_detail_traversal(path)

    """ Result

    +- <data> [CNT = 8, SIZE = 3.39 KB]
    |   +- LOG1.log [SIZE = 0.02 KB]
    |   +- LOG2.log [SIZE = 0.12 KB]
    |   +- <folder1> [CNT = 0, SIZE = 0.00 KB]
    |   +- <folder2> [CNT = 4, SIZE = 3.24 KB]
    |   |   +- <folder2_1> [CNT = 2, SIZE = 3.24 KB]
    |   |   |   +- PY1.py [SIZE = 0.02 KB]
    |   |   |   +- PY2.py [SIZE = 3.23 KB]
    |   |   +- <folder2_2> [CNT = 0, SIZE = 0.00 KB]
    ```
