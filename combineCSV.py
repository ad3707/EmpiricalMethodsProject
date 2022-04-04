import pandas as pd
import glob

postsPathF19 = 'csv/posts/f19'
postsPathF20 = 'csv/posts/f20'
postsPathF21 = 'csv/posts/f21'
postsPathS21 = 'csv/posts/s21'
postsPathS20 = 'csv/posts/s20'

liF19 = []
liS21 = []
liF20 = []
liS20 = []
liF21 = []


fall19_postsFiles = glob.glob(postsPathF19 + "/*.csv")
spring21_postsFiles = glob.glob(postsPathS21 + "/*.csv")
fall20_postsFiles = glob.glob(postsPathF20 + "/*.csv")
spring20_postsFiles = glob.glob(postsPathS20 + "/*.csv")
fall21_postsFiles = glob.glob(postsPathF21 + "/*.csv")

for filename in fall19_postsFiles:
    dfF19 = pd.read_csv(filename,index_col = None, header = 0)
    liF19.append(dfF19)

for filename in fall20_postsFiles:
    dfF20 = pd.read_csv(filename,index_col = None, header = 0)
    liF20.append(dfF20)

for filename in fall21_postsFiles:
    dfF21 = pd.read_csv(filename,index_col = None, header = 0)
    liF21.append(dfF21)

for filename in spring21_postsFiles:
    dfS21 = pd.read_csv(filename,index_col = None, header = 0)
    liS21.append(dfS21)
for filename in spring20_postsFiles:
    dfS20 = pd.read_csv(filename,index_col = None, header = 0)
    liS20.append(dfS20)
frameFall19 = pd.concat(liF19, axis = 0, ignore_index = True)
frameFall20 = pd.concat(liF20, axis = 0, ignore_index = True)
frameFall21 = pd.concat(liF21, axis = 0, ignore_index = True)
frameSpring21 = pd.concat(liS21, axis = 0, ignore_index = True)
frameSpring20 = pd.concat(liS20, axis = 0, ignore_index = True)

frameFall19.to_csv(f'./combinedCSV/f19_posts.csv', header = True, index = False, columns = list(frameFall19.axes[1]))
frameFall20.to_csv(f'./combinedCSV/f20_posts.csv', header = True, index = False, columns = list(frameFall20.axes[1]))
frameFall21.to_csv(f'./combinedCSV/f21_posts.csv', header = True, index = False, columns = list(frameFall21.axes[1]))
frameSpring21.to_csv(f'./combinedCSV/s21_posts.csv', header = True, index = False, columns = list(frameSpring21.axes[1]))
frameSpring20.to_csv(f'./combinedCSV/s20_posts.csv', header = True, index = False, columns = list(frameSpring20.axes[1]))
