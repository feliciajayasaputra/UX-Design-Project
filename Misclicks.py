import matplotlib.pyplot as plt
import numpy as np

y = np.array([0.4, 0, 2.4, 0, 1.6, 1.8, 3.8, 2.2])
mylabels = ["Task 1", "Task 2", "Task 3",
            "Task 4", "Task 5",
            "Task 6", "Task 7",
            "Task 8"]

plt.pie(y, labels = mylabels)
plt.title("Percentage of user misclicks on each task")
plt.show() 
