# FileTraversal
Traversal a given path. Show the path structure.

## Demo

- Simple Case
    ```python
    path = r'.'
    obj = FileTraversal()
    obj.simple_traversal(path, 0)

    """ Result

    +- <.>
    |   +- <.git>
    |   |   +- COMMIT_EDITMSG
    |   |   +- config
    |   |   +- description
    |   |   +- FETCH_HEAD
    |   |   +- HEAD
    |   |   +- <hooks>
    |   |   |   +- applypatch-msg.sample
    |   |   |   +- commit-msg.sample
    |   |   |   +- fsmonitor-watchman.sample
    |   |   |   +- post-update.sample
    |   |   |   +- pre-applypatch.sample
    |   |   |   +- pre-commit.sample
    |   |   |   +- pre-push.sample
    |   |   |   +- pre-rebase.sample
    |   |   |   +- pre-receive.sample
    |   |   |   +- prepare-commit-msg.sample
    |   |   |   +- update.sample
    |   |   +- index
    |   |   +- <info>
    |   |   |   +- exclude
    |   |   +- <logs>
    |   |   |   +- HEAD
    |   |   |   +- <refs>
    |   |   |   |   +- <heads>
    |   |   |   |   |   +- master
    |   |   |   |   +- <remotes>
    |   |   |   |   |   +- <origin>
    |   |   |   |   |   |   +- HEAD
    |   |   |   |   |   |   +- master
    |   |   +- <objects>
    |   |   |   +- <13>
    |   |   |   |   +- 0c8ee3f248467fed6b39d51fec404d10ead644
    |   |   |   +- <68>
    |   |   |   |   +- 64da59df0aa40740850d07c3448eca7920d8c1
    |   |   |   +- <8d>
    |   |   |   |   +- b69d43905d7b6a34409004620cda327e99ecf7
    |   |   |   +- <info>
    |   |   |   +- <pack>
    |   |   |   |   +- pack-c7bd9a740296193b896fbfc799de029f7a0cccda.idx
    |   |   |   |   +- pack-c7bd9a740296193b896fbfc799de029f7a0cccda.pack
    |   |   +- packed-refs
    |   |   +- <refs>
    |   |   |   +- <heads>
    |   |   |   |   +- master
    |   |   |   +- <remotes>
    |   |   |   |   +- <origin>
    |   |   |   |   |   +- HEAD
    |   |   |   |   |   +- master
    |   |   |   +- <tags>
    |   +- file_traversal.py
    |   +- README.md
    """

    ```


- Detail Info Case
    ```python
    path = r'.'
    obj = FileTraversal()
    obj.execute_detail_traversal(path)

    """ Result

    +- <.> [CNT = 52, SIZE = 35.541015625 KB]
    |   +- <.git> [CNT = 49, SIZE = 26.1171875 KB]
    |   |   +- <refs> [CNT = 7, SIZE = 0.111328125 KB]
    |   |   |   +- <tags> [CNT = 0, SIZE = 0 KB]
    |   |   |   +- <remotes> [CNT = 3, SIZE = 0.0712890625 KB]
    |   |   |   |   +- <origin> [CNT = 2, SIZE = 0.0712890625 KB]
    |   |   |   |   |   +- master [SIZE = 0.0400390625]
    |   |   |   |   |   +- HEAD [SIZE = 0.03125]
    |   |   |   +- <heads> [CNT = 1, SIZE = 0.0400390625 KB]
    |   |   |   |   +- master [SIZE = 0.0400390625]
    |   |   +- <objects> [CNT = 10, SIZE = 5.2587890625 KB]
    |   |   |   +- <pack> [CNT = 2, SIZE = 3.0322265625 KB]
    |   |   |   |   +- pack-c7bd9a740296193b896fbfc799de029f7a0cccda.pack [SIZE = 1.8212890625]
    |   |   |   |   +- pack-c7bd9a740296193b896fbfc799de029f7a0cccda.idx [SIZE = 1.2109375]
    |   |   |   +- <info> [CNT = 0, SIZE = 0 KB]
    |   |   |   +- <8d> [CNT = 1, SIZE = 0.0927734375 KB]
    |   |   |   |   +- b69d43905d7b6a34409004620cda327e99ecf7 [SIZE = 0.0927734375]
    |   |   |   +- <68> [CNT = 1, SIZE = 0.2421875 KB]
    |   |   |   |   +- 64da59df0aa40740850d07c3448eca7920d8c1 [SIZE = 0.2421875]
    |   |   |   +- <13> [CNT = 1, SIZE = 1.8916015625 KB]
    |   |   |   |   +- 0c8ee3f248467fed6b39d51fec404d10ead644 [SIZE = 1.8916015625]
    |   |   +- <logs> [CNT = 8, SIZE = 1.130859375 KB]
    |   |   |   +- <refs> [CNT = 6, SIZE = 0.748046875 KB]
    |   |   |   |   +- <remotes> [CNT = 3, SIZE = 0.365234375 KB]
    |   |   |   |   |   +- <origin> [CNT = 2, SIZE = 0.365234375 KB]
    |   |   |   |   |   |   +- master [SIZE = 0.162109375]
    |   |   |   |   |   |   +- HEAD [SIZE = 0.203125]
    |   |   |   |   +- <heads> [CNT = 1, SIZE = 0.3828125 KB]
    |   |   |   |   |   +- master [SIZE = 0.3828125]
    |   |   |   +- HEAD [SIZE = 0.3828125]
    |   |   +- <info> [CNT = 1, SIZE = 0.234375 KB]
    |   |   |   +- exclude [SIZE = 0.234375]
    |   |   +- <hooks> [CNT = 11, SIZE = 18.40234375 KB]
    |   |   |   +- update.sample [SIZE = 3.525390625]
    |   |   |   +- prepare-commit-msg.sample [SIZE = 1.45703125]
    |   |   |   +- pre-receive.sample [SIZE = 0.53125]
    |   |   |   +- pre-rebase.sample [SIZE = 4.783203125]
    |   |   |   +- pre-push.sample [SIZE = 1.31640625]
    |   |   |   +- pre-commit.sample [SIZE = 1.599609375]
    |   |   |   +- pre-applypatch.sample [SIZE = 0.4140625]
    |   |   |   +- post-update.sample [SIZE = 0.1845703125]
    |   |   |   +- fsmonitor-watchman.sample [SIZE = 3.2490234375]
    |   |   |   +- commit-msg.sample [SIZE = 0.875]
    |   |   |   +- applypatch-msg.sample [SIZE = 0.466796875]
    |   |   +- packed-refs [SIZE = 0.111328125]
    |   |   +- index [SIZE = 0.2119140625]
    |   |   +- HEAD [SIZE = 0.0224609375]
    |   |   +- FETCH_HEAD [SIZE = 0.099609375]
    |   |   +- description [SIZE = 0.0712890625]
    |   |   +- config [SIZE = 0.3232421875]
    |   |   +- COMMIT_EDITMSG [SIZE = 0.1396484375]
    |   +- README.md [SIZE = 1.96875]
    |   +- file_traversal.py [SIZE = 7.455078125]
    """

    ```


- Condition Case
    ```python
    path = r'.'
    
    file_pattern1 = '.+\.py'
    file_pattern2 = '.+\.md'
    file_pattern3 = '.+\.sample'
    file_pattern_list = [file_pattern1, file_pattern2, file_pattern3]

    obj = FileTraversal()
    obj.compile_pass_file_list(file_pattern_list)

    obj.execute_detail_traversal(path)

    """ Result

    +- <.> [CNT = 32, SIZE = 31.3818359375 KB]
    |   +- <.git> [CNT = 29, SIZE = 18.40234375 KB]
    |   |   +- <refs> [CNT = 4, SIZE = 0 KB]
    |   |   |   +- <tags> [CNT = 0, SIZE = 0 KB]
    |   |   |   +- <remotes> [CNT = 1, SIZE = 0 KB]
    |   |   |   |   +- <origin> [CNT = 0, SIZE = 0 KB]
    |   |   |   +- <heads> [CNT = 0, SIZE = 0 KB]
    |   |   +- <objects> [CNT = 5, SIZE = 0 KB]
    |   |   |   +- <pack> [CNT = 0, SIZE = 0 KB]
    |   |   |   +- <info> [CNT = 0, SIZE = 0 KB]
    |   |   |   +- <8d> [CNT = 0, SIZE = 0 KB]
    |   |   |   +- <68> [CNT = 0, SIZE = 0 KB]
    |   |   |   +- <13> [CNT = 0, SIZE = 0 KB]
    |   |   +- <logs> [CNT = 4, SIZE = 0 KB]
    |   |   |   +- <refs> [CNT = 3, SIZE = 0 KB]
    |   |   |   |   +- <remotes> [CNT = 1, SIZE = 0 KB]
    |   |   |   |   |   +- <origin> [CNT = 0, SIZE = 0 KB]
    |   |   |   |   +- <heads> [CNT = 0, SIZE = 0 KB]
    |   |   +- <info> [CNT = 0, SIZE = 0 KB]
    |   |   +- <hooks> [CNT = 11, SIZE = 18.40234375 KB]
    |   |   |   +- update.sample [SIZE = 3.525390625]
    |   |   |   +- prepare-commit-msg.sample [SIZE = 1.45703125]
    |   |   |   +- pre-receive.sample [SIZE = 0.53125]
    |   |   |   +- pre-rebase.sample [SIZE = 4.783203125]
    |   |   |   +- pre-push.sample [SIZE = 1.31640625]
    |   |   |   +- pre-commit.sample [SIZE = 1.599609375]
    |   |   |   +- pre-applypatch.sample [SIZE = 0.4140625]
    |   |   |   +- post-update.sample [SIZE = 0.1845703125]
    |   |   |   +- fsmonitor-watchman.sample [SIZE = 3.2490234375]
    |   |   |   +- commit-msg.sample [SIZE = 0.875]
    |   |   |   +- applypatch-msg.sample [SIZE = 0.466796875]
    |   +- README.md [SIZE = 5.5244140625]
    |   +- file_traversal.py [SIZE = 7.455078125]
    """

    ```
