import matplotlib.pyplot as plt
import numpy as np

y = np.array([7.18, 19.34, 39.20, 45.8, 52.11, 39.83, 32.51, 25.91])
mylabels = ["Task 1", "Task 2", "Task 3",
            "Task 4", "FTask 5",
            "Task 6", "Task 7",
            "Task 8"]

# Setting up the positions for the bars
x = np.arange(len(y))

# Creating a bar chart
plt.bar(x, y)

# Adding labels and title
plt.xlabel('Tasks')
plt.ylabel('Time Spent (seconds)')
plt.title('Time Spent on Different Tasks')

# Adding custom x-axis labels
plt.xticks(x, mylabels, rotation=45, ha="right")

# Displaying the bar chart
plt.show()
