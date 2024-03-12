from file_modules import gen_files, gen_files_from_dict, group_rename

my_dict = {'.mkv':3,'.png':1,'.txt': 8, }
gen_files_from_dict(my_dict, 'test_files')
group_rename('test_files', '.txt', '.csv', 'new', (1, 3), 3)
