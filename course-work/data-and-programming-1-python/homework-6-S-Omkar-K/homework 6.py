# PPHA 30535
# Spring 2022
# Homework 6

# Sai Omkar Kandukuri

# Sai Omkar Kandukuri
# S-Omkar-K

# Due date: Sunday May 15th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_plot.png", "q2_plot.png", etc. If a question calls
# for more than one plot, name them "q1a_plot", "q1b_plot", etc.

#NOTE: If no specific library is called for by the question, then you may freely
# use Matplotlib, Pandas, Seaborn, or a combination to answer the question.

# Question 1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis labels are legible.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]


path = 'C:/Users/saiom/OneDrive/Documents/GitHub/homework-6-S-Omkar-K/'

fig, ax = plt.subplots()
ax.scatter(x, y1)
ax.plot(x,y2,color = 'Red')
ax.legend(["Random Value Plot", "Sine Value Plot"], loc ="lower right")
ax.set_xlabel('Dates')
ax.set_ylabel('Y Values')
fig.savefig(path + "q1_plot.png")
#fig.show()
#fig.clear()




# Question 2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.

x = np.arange(0,10)
y = np.arange(0,10)
fig,ax = plt.subplots()
ax.plot(x, y, label='Blue')
ax.spines['top'].set_visible(True)
#ax.spines['top'].set_color('0.5')
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.set_facecolor('xkcd:white')
ax.plot(x, y[::-1], 'r-', label = 'Red')
plt.xticks(np.arange(x.min(),x.max(),2))
plt.yticks(np.arange(y.min(), y.max(), 2))
ax.legend(loc = 'center left')
ax.set_title(' X marks the spot')
ax.patch.set_edgecolor('black')  
ax.patch.set_linewidth('1') 
fig.savefig(path + "q2_plot.png")
#fig.show()
#fig.clear()


# Question 3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.


data = pd.read_csv("C:/Users/saiom/OneDrive/Documents/GitHub/homework-6-S-Omkar-K/mpg.csv")



fig,ax = plt.subplots()
ax.plot(data['displacement'], data['mpg']) #label = 'Displacement'
ax.set_xlabel('Displacement')
ax.set_ylabel('Mpg')
ax.set_title('Displacement against Mpg')
#ax.legend(loc='upper right')
fig.savefig(path + "q3a_plot.png")
#fig.show()
#fig.clear()

#The hypothesis given is true as we see a downward sloping trend, i.e the miles per gallon decreasing with displacement increasing


fig,ax = plt.subplots()
ax.plot(data['horsepower'], data['mpg']) #label = 'Horsepower'
ax.set_xlabel('Horsepower')
ax.set_ylabel('Mpg')
#ax.legend(loc='upper right')
ax.set_title("Horsepower against Mpg")
fig.savefig(path + "q3b_plot.png")
#fig.show()
#fig.clear()
#The hypothesis given is true as we see a downward sloping trend, i.e the miles per gallon decreasing with Horsepower increasing



fig,ax = plt.subplots()
ax.plot(data['weight'], data['mpg']) #label = 'Weight'
ax.set_xlabel('Weight')
ax.set_ylabel('Mpg')
#ax.legent(loc = 'upper right')
ax.set_title('Weight against Mpg')
fig.savefig(path + "q3c_plot.png")
#fig.show()
#fig.clear()
#The hypothesis given is true as we see a downward sloping trend, i.e the miles per gallon decreasing with Weight increasing




# Question 4: Continuing from question 3, create a scatter plot with mpg
# on the y-axis and cylinders on the x-axis.  Explain what is wrong with this
# plot with a one-line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.

data.columns

fig,ax = plt.subplots()
ax.scatter(data['cylinders'],data['mpg'])
ax.set_xlabel('Cylinders')
ax.set_ylabel('Mpg')
ax.set_title("Cylinders against Mpg - Scatter")
fig.savefig(path + "q4a_plot.png")

#The scatter plot is not the right depiction to represent the accurate relation, as the distribution/properties of the Mpg data cannot be obtained to compare across various groupings of the Cylinder data 

import seaborn as sns
fig,ax = plt.subplots()
sns.boxplot(x = 'cylinders', y = 'mpg', data = data).set(title = 'Mpg against Cylinders'
                                                    ,xlabel = 'Cylinders', ylabel = 'Mpg')

fig.savefig(path + "q4b_plot.png")


# Question 5: Continuing from question 3, create a two-by-two grid of
# subplots, where each one has mpg on the y-axis and one of displacement,
# horsepower, weight, and acceleration on the x-axis.  To clean up this 
# plot, remove the y-axis labels on the right two plots - the scale will 
# already be aligned because the mpg values are the same.

  

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2,ncols = 2, sharey='row', figsize = (6.4,6.4))
fig.suptitle(' Mpg against displacement, weight, horsepower, acceleration')
ax1.plot(data['displacement'], data['mpg'])
ax1.set_xlabel('Displacement')
#ax1.set_xlabel('Mpg')
ax2.plot(data['weight'], data['mpg'], 'tab:orange')
ax2.set_xlabel('Weight')
ax3.plot(data['horsepower'], data['mpg'], 'tab:green')
ax3.set_xlabel('Horsepower')
#ax1.set_xlabel('Mpg')
ax4.plot(data['acceleration'], data['mpg'], 'tab:red')
ax4.set_xlabel('Acceleration')
fig.supylabel('Mpg')
fig.savefig(path + "q5_plot.png")
#fig.legend


# Question 6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot.

#data = sns.load_dataset('data')
fig, ax = plt.subplots()
plot6 = sns.boxplot(x = 'origin', 
                    y = 'mpg', 
                    showmeans = 'True', 
                    meanline = 'True', 
                    whiskerprops={'visible': True},
                    medianprops={'visible': True},
                    zorder=10,
                    showfliers=True,
                    showbox=True,
                    showcaps=True,
                    data = data)
fig.savefig(path + "q6_plot.png")
#The green dashed line shows mean properties. Median properties are the solid black lines in the boxes
#The average mpg is the least for usa and highest for japan. The same goes with median as well.
#The highest mpg in absolute values is in Japan and the least mpg in absolute values is in usa



#Method 2
#data = sns.load_dataset('data')
#scatplot = sns.scatterplot(x="origin", y="mpg", data=data)
#sns.boxplot(x = 'origin', 
#                    y = 'mpg', 
#                    showmeans = 'True', 
#                    meanline = 'True', 
#                    whiskerprops={'visible': False},
#                    medianprops={'visible': False},
#                    zorder=10,
#                    showfliers=True,
#                    showbox=False,
#                    showcaps=False,
#                    data = data,
#                    ax = scatplot)

# Question 7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.

#data = sns.load_dataset('data')
fig, ax = plt.subplots()
plot7 = sns.scatterplot(x="displacement",
                    y="mpg",
                    hue="origin",
                    data=data).set(
                        xlabel = 'Displacement',
                        ylabel = 'Mpg',
                        title = 'Mpg versus displacement')
fig.savefig(path + "q7_plot.png")