import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import csv
import random

df = pd.read_csv("studentMarks.csv")

data = df["Math_score"].tolist() 

#fig = ff.create_distplot([data],["Math Score"],show_hist = False)
#fig.show()

#Calclate mean and sd of population data
mean = statistics.mean(data)
std_dev = statistics.stdev(data)

#print("Mean is: ",mean)
#print("Sd is: ",std_dev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

standard_deviation = statistics.stdev(mean_list)
sample_mean = statistics.mean(mean_list)

print("Mean of sampling distribution: ",sample_mean)
print("Stdev : ",standard_deviation)

fig = ff.create_distplot([mean_list],["Student Marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0,20] , mode = "lines", name = "MEAN"))
fig.show()