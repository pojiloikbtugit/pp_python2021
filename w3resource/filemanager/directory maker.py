import os 

directory= input()

parent_dir = 'C:/Users/sezam/Desktop/study/pp2/python ex'

path = os.path.join(parent_dir,directory)

os.mkdir(path)

