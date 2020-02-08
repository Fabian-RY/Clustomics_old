
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import seaborn 

data_numbers = pd.DataFrame(pd.read_csv("input.csv", names=["gen1","gen2"]) )
data_group= pd.DataFrame(pd.read_csv("nombre.csv",names=["grupo"]))

data_numbers=pd.DataFrame([(1,1),(2,2),(3,3)])
data_group=pd.DataFrame([0,1,2],columns=["grupo"])

number_groups=len(set(data_group["grupo"]))

colors=seaborn.color_palette(palette="Set1", n_colors=number_groups)


color=[]
for i in range(len(data_group)):
    color.append(colors[data_group["grupo"][i]])

plt.scatter(x=data_numbers[data_numbers.columns[0]],y=data_numbers[data_numbers.columns[1]],color=color)





