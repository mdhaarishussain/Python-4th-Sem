import numpy as np
import matplotlib.pyplot as plt
games = np.array(['Cricket', 'Football', 'Hockey', 'Tennis'])
India_scores = np.array([60, 50, 20, 10])
other_scores = np.array([30, 50, 25, 10])
x = np.arange(len(games))
width = 0.35
plt.bar(x - width/2, India_scores, width, label='India', color='blue')
plt.bar(x + width/2, other_scores, width, label='Other', color='orange')
plt.xlabel('Games')
plt.ylabel('Scores')
plt.title('Scores by Game and Country')
plt.xticks(x, games)
plt.legend()
plt.show()


















