import matplotlib.pyplot as plt
import numpy as np

y = np.array([3.2, 5, 5.4, 3, 10.6, 10.8, 11.8, 5.2])
mylabels = ["Task 1", "Task 2", "Task 3",
            "Task 4", "Task 5",
            "Task 6", "Task 7",
            "Task 8"]

plt.pie(y, labels = mylabels)
plt.title("Percentage of User Clicks On Each task")
plt.show() 


