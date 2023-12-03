import statistics
import matplotlib.pyplot as plt
import numpy as np

# Calculate the standard deviation from a sample of data
#print("Standard Deviation Task 1: " + statistics.stdev([0, 0, 0, 2, 0]))
x1 = statistics.stdev([0, 0, 0, 2, 0])
#print("Standard Deviation Task 2: " + statistics.stdev([0, 0, 0, 0, 0]))
x2 = statistics.stdev([0, 0, 0, 0, 0])
#print("Standard Deviation Task 3: " + statistics.stdev([0, 0, 0, 8, 4]))
x3 = statistics.stdev([0, 0, 0, 8, 4])
#print("Standard Deviation Task 4: " + statistics.stdev([0, 0, 0, 0, 0]))
x4 = statistics.stdev([0, 0, 0, 0, 0])
#print("Standard Deviation Task 5: " + statistics.stdev([2, 1, 0, 2, 3]))
x5 = statistics.stdev([2, 1, 0, 2, 3])
#print("Standard Deviation Task 6: " + statistics.stdev([0, 2, 0, 4, 3]))
x6 = statistics.stdev([0, 2, 0, 4, 3])
#print("Standard Deviation Task 7: " + statistics.stdev([5, 4, 2, 6, 2]))
x7 = statistics.stdev([5, 4, 2, 6, 2])
#print("Standard Deviation Task 8: " + statistics.stdev([0, 0, 0, 5, 6]))
x8 = statistics.stdev([0, 0, 0, 5, 6])


# User average misclicks for 7 tasks
user_avg_misclicks = np.array([0.4, 0, 2.4, 0, 1.6, 1.8, 3.8, 2.2])

# Corresponding standard deviations for each task
std_dev_misclicks = np.array([x1, x2, x3, x4, x5, x6, x7, x8])

# Task labels
task_labels = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5", "Task 6", "Task 7", "Task 8"]

# Plotting the bar chart with error bars
plt.bar(task_labels, user_avg_misclicks, yerr=std_dev_misclicks, capsize=5, color='skyblue', alpha=0.7)

# Adding labels and title
plt.xlabel('Tasks')
plt.ylabel('Average Misclicks')
plt.title('Average Misclicks with Standard Deviation for Different Tasks')

# Show the plot
plt.show()



