import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data = {
    "State": ["Maharashtra", "Rajasthan", "Uttar Pradesh", "Gujarat", "Delhi", "Madhya Pradesh", "Tamil Nadu"],
    "Confirmed": [21506, 12720, 12328, 14721, 13738, 12715, 12526],
    "Active": [19142, 11539, 11632, 13750, 12510, 12046, 11186],
    "Recovered": [11879, 11116, 1654, 1735, 1167, 1524, 11312],
    "Deceased": [485, 65, 42, 236, 1061, 145, 28]
}

# Create DataFrame 
df = pd.DataFrame(data)

# (a) Horizontal bar chart for state-wise confirmed cases
plt.figure(figsize=(10, 6))
plt.barh(df['State'], df['Confirmed'], color='skyblue')
plt.xlabel('Confirmed Cases')
plt.title('State-wise Confirmed Cases')
plt.gca().invert_yaxis()  # Invert y-axis to have highest value on top
plt.show()

# (b) Bar chart for state-wise active and recovered cases
plt.figure(figsize=(10, 6))
plt.bar(df['State'], df['Active'], color='red', label='Active')
plt.bar(df['State'], df['Recovered'], color='green', label='Recovered', bottom=df['Active'])
plt.xlabel('Stae')
plt.ylabel('Cases')
plt.title('State-wise Active and Recovered Cases')
plt.xticks(rotation=45)  # Rotate x-labels for better visibility
plt.legend()
plt.show()

# (c) Pie charts for active, recovered, and deceased cases for Delhi and Uttar Pradesh
states_of_interest = ['Delhi', 'Uttar Pradesh']
for state in states_of_interest:
    state_data = df[df['State'] == state]
    labels = ['Active', 'Recovered', 'Deceased']
    sizes = [state_data['Active'].values[0], state_data['Recovered'].values[0], state_data['Deceased'].values[0]]
    colors = ['red', 'green', 'grey']
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title(f'{state} - Active, Recovered, and Deceased Cases')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
