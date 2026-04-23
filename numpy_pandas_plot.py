
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

subjects = ["Math", "Physics", "Chemistry", "Biology"]
marks = np.array([85, 78, 92, 88])

df = pd.DataFrame({
    "Subject": subjects,
    "Marks": marks
})

print(df)

plt.plot(subjects, marks, marker='o')
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
