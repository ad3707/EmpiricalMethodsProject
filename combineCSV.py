import pandas as pd 
import glob 

path = "/csvTest"

li = []
all_files = glob.glob(path + "/*.csv")

for filename in all_files: 
  df = pd.read_csv(filename,index_col = None, header = 0)
  li.append(df)

frame = pd.concat(li, axis = 0, ignore_index = True)