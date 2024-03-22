import matplotlib
import tkinter as tk
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Define the data
fruits = ['Avocados', 'Oranges', 'Bananas', 'Kiwi Fruit', 'Mangoes', 'Grapes']
quantities = [36, 41, 19, 28, 30, 16]

# Define the ripe fruit colors
ripe_fruit_colors = {'Avocados': 'green', 'Oranges': 'orange', 'Bananas': 'yellow', 
                     'Kiwi Fruit': 'brown', 'Mangoes': 'orange', 'Grapes': 'purple'}

# Create a bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(fruits, quantities, color=[ripe_fruit_colors[fruit] for fruit in fruits])

# Label the axes and title
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Youth Preference on Fruits in Juja')

# Add labels to the bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()
