import pandas as pd
import statistics
import plotly.figure_factory as ff
import csv
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot([data],["read time for dataset"],show_hist=False)
fig.show()


def random_dataSet(counter):
  dataSet=[]
  for i in range(0,counter):
    randomIndex = random.randint(0,len(data)-1)
    value = data[randomIndex]
    dataSet.append(value)

  mean = statistics.mean(dataSet)
  return mean

meanList = []
for i in range(0,1000):
  setOfMean = random_dataSet(100)
  meanList.append(setOfMean)

standardDiviation = statistics.stdev(meanList)
mean = statistics.mean(meanList)

print("mean-:",mean)
print("standard Diviation-:",standardDiviation)

stdev_start, stdev_end = mean-standardDiviation, mean+standardDiviation
stdev2_start, stdev2_end = mean-(2*standardDiviation), mean+(2*standardDiviation)
stdev3_start, stdev3_end = mean-(3*standardDiviation), mean+(3*standardDiviation)
print("std1-:",stdev_start, stdev_end)
print("std2-:",stdev2_start, stdev2_end)
print("std3-:",stdev3_start, stdev3_end)


samp1 = pd.read_csv("sample1.csv")
sample1 = samp1["reading_time"].tolist()

meanSample1 = statistics.mean(sample1)
print("mean of sample1 -:", meanSample1)

fig = ff.create_distplot([meanList],["read time for sampling dataset"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[stdev_end, stdev_end], y=[0, 0.17], mode="lines", name="stdev1 End"))
fig.add_trace(go.Scatter(x=[stdev2_end, stdev2_end], y=[0, 0.17], mode="lines", name="stdev2 End"))
fig.add_trace(go.Scatter(x=[stdev3_end, stdev3_end], y=[0, 0.17], mode="lines", name="stdev3 End"))
fig.add_trace(go.Scatter(x=[stdev_start, stdev_start], y=[0, 0.17], mode="lines", name="stdev1 start"))
fig.add_trace(go.Scatter(x=[stdev2_start, stdev2_start], y=[0, 0.17], mode="lines", name="stdev2 start"))
fig.add_trace(go.Scatter(x=[stdev3_start, stdev3_start], y=[0, 0.17], mode="lines", name="stdev3 start"))
fig.show()

z_score = (meanSample1-mean)/standardDiviation
print("The z score is-:",z_score)
