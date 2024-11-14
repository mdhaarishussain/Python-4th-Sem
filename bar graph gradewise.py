import matplotlib.pyplot as plt
grades = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D', 'E']
python_scores = [80, 69, 72, 72, 72, 75, 81, 84]
os_scores = [89, 86, 85, 79, 81, 80, 83, 76]
network_scores = [75, 75, 84, 83, 79, 86, 91, 79]
x = range(len(grades))
width = 0.25
plt.bar(x, python_scores, width, label='Python')
plt.bar([i + width for i in x], os_scores, width, label='OS')
plt.bar([i + 2*width for i in x], network_scores, width, label='Network')
plt.xlabel('Grades')
plt.ylabel('Scores')
plt.title('Grade-wise Result of OS and Network')
plt.xticks([i + width for i in x], grades)
plt.legend()
plt.show()
