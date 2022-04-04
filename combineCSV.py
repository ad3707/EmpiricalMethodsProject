import pandas as pd
import glob

postsPath = "csv/posts"
#commsPath = " " 

liF19 = []
liS19 = []
liF20 = []
liS20 = []
liF21 = []


fall19_postsFiles = glob.glob(postsPath + "F19/*.csv")
spring19_postsFiles = glob.glob(postsPath + "S19/*.csv")
fall20_postsFiles = glob.glob(postsPath + "F20/*.csv")
spring20_postsFiles = glob.glob(postsPath + "S20/*.csv")
fall21_postsFiles = glob.glob(postsPath + "F21/*.csv")


for filename in fall19_postsFiles:
  dfF19 = pd.read_csv(filename,index_col = None, header = 0)
  liF19.append(df19)
  
for filename in fall20_postsFiles:
  dfF20 = pd.read_csv(filename,index_col = None, header = 0)
  liF20.append(dfF20)
  
for filename in fall21_postsFiles:
  dfF21 = pd.read_csv(filename,index_col = None, header = 0)
  liF21.append(dfF21)
  
for filename in spring19_postsFiles:
  dfS19 = pd.read_csv(filename,index_col = None, header = 0)
  liS19.append(dfS19)
  
 for filename in spring20_postsFiles:
  dfS20 = pd.read_csv(filename,index_col = None, header = 0)
  liS20.append(dfS20)

frameFall19 = pd.concat(liF19, axis = 0, ignore_index = True)
frameFall20 = pd.concat(liF20, axis = 0, ignore_index = True)
frameFall21 = pd.concat(liF21, axis = 0, ignore_index = True)
frameSpring19 = pd.concat(liS19, axis = 0, ignore_index = True)
frameSpring20 = pd.concat(liS20, axis = 0, ignore_index = True)

frameFall19.to_csv(f'./combinedCSV/f19_posts.csv', header = True, index = False, columns = list(frame.axes[1]))
frameFall20.to_csv(f'./combinedCSV/f20_posts.csv', header = True, index = False, columns = list(frame.axes[1]))
frameFall21.to_csv(f'./combinedCSV/f21_posts.csv', header = True, index = False, columns = list(frame.axes[1]))
frameSpring19.to_csv(f'./combinedCSV/s19_posts.csv', header = True, index = False, columns = list(frame.axes[1]))
frameSpring20.to_csv(f'./combinedCSV/s20_posts.csv', header = True, index = False, columns = list(frame.axes[1]))
