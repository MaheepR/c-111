import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import csv
import random

#df = pd.read_csv("data1.csv")

#data = df["Math_score"].tolist() 



df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()

mean = statistics.mean(data)
st_dv = statistics.stdev(data)

first_std_dev_start,first_std_dev_end = mean - st_dv , mean + st_dv
second_std_dev_start,second_std_dev_end = mean - (2*st_dv) , mean + (2*st_dv)
third_std_dev_start,third_std_dev_end = mean - (3*st_dv) , mean + (3*st_dv)

print("std1", first_std_dev_start,first_std_dev_end)
print("std2", second_std_dev_start,second_std_dev_end)
print("std3", third_std_dev_start,third_std_dev_end)

#mean_of_sample1 = statistics.mean(data)

#print("Mean of sample1 :",mean_of_sample1)

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


#fig = ff.create_distplot([mean_list],["Student Marks"],show_hist = False)
#fig.add_trace(go.Scatter(x = [mean,mean],y =[0,0.17], mode = "lines", name ="MEAN"))
#fig.add_trace(go.Scatter(x = [mean_of_sample1,mean_of_sample1],y =[0,0.17], mode = "lines", name ="MEAN OF SAMPLE"))
#fig.add_trace(go.Scatter(x = [first_std_dev_end,first_std_dev_end], y = [0,0.17],mode = "lines", name = "Standard Deviation1 end"))
#fig.show()

 
#mean_of_sample2 = statistics.mean(data)
#print("Mean of sample2 :",mean_of_sample2)
#fig = ff.create_distplot([mean_list],["Student Marks"],show_hist = False)
#fig.add_trace(go.Scatter(x = [mean,mean],y =[0,0.17], mode = "lines", name ="MEAN"))
#fig.add_trace(go.Scatter(x = [mean_of_sample2,mean_of_sample2],y =[0,0.17], mode = "lines", name ="MEAN OF SAMPLE2"))
#fig.add_trace(go.Scatter(x = [first_std_dev_end,first_std_dev_end], y = [0,0.17],mode = "lines", name = "Standard Deviation1 end"))
#fig.add_trace(go.Scatter(x = [second_std_dev_end,second_std_dev_end], y = [0,0.17],mode = "lines", name = "Standard Deviation2 end"))
#fig.show()

mean_of_sample3 = statistics.mean(data)
print("Mean of sample3 :",mean_of_sample3)
fig = ff.create_distplot([mean_list],["Student Marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y =[0,0.17], mode = "lines", name ="MEAN"))
fig.add_trace(go.Scatter(x = [mean_of_sample3,mean_of_sample3],y =[0,0.17], mode = "lines", name ="MEAN OF SAMPLE3"))
fig.add_trace(go.Scatter(x = [first_std_dev_end,first_std_dev_end], y = [0,0.17],mode = "lines", name = "Standard Deviation1 end"))
fig.add_trace(go.Scatter(x = [second_std_dev_end,second_std_dev_end], y = [0,0.17],mode = "lines", name = "Standard Deviation2 end"))
fig.add_trace(go.Scatter(x = [third_std_dev_end,third_std_dev_end], y = [0,0.17],mode = "lines", name = "Standard Deviation3 end"))
fig.show()

#fig = ff.create_distplot([mean_list],["Student Marks"],show_hist = False)
#fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17] , mode = "lines", name = "MEAN"))
#fig.add_trace(go.Scatter(x = [first_std_dev_start,first_std_dev_start], y = [0,0.17],mode = "lines", name = "Standard Deviation1 start"))
#fig.add_trace(go.Scatter(x = [first_std_dev_end,first_std_dev_end], y = [0,0.17],mode = "lines", name = "Standard Deviation1 end"))
#fig.add_trace(go.Scatter(x = [second_std_dev_start,second_std_dev_start], y = [0,0.17],mode = "lines", name = "Standard Seviation2 start"))
#fig.add_trace(go.Scatter(x = [second_std_dev_end,second_std_dev_end], y = [0,0.17],mode = "lines", name = "Standard Deviation2 end"))
#fig.add_trace(go.Scatter(x = [third_std_dev_start,third_std_dev_start], y = [0,0.17],mode = "lines", name = "Standard Seviation3 start"))
#fig.add_trace(go.Scatter(x = [third_std_dev_end,third_std_dev_end], y = [0,0.17],mode = "lines", name = "Standard Deviation3 end"))
#fig.show()