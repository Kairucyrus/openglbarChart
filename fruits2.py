import matplotlib
import tkinter as tk
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Defining the data
fruits = ['Avocados', 'Oranges', 'Bananas', 'Kiwi Fruit', 'Mangoes', 'Grapes']
quantities = [36, 41, 19, 28, 30, 16]



#  we here define the ripe fruit colors
ripe_fruit_colors = {'Avocados': 'green', 'Oranges': 'orange', 'Bananas': 'yellow', 
                     'Kiwi Fruit': 'brown', 'Mangoes': 'orange', 'Grapes': 'purple'}
figure = plt.figure(figsize=(10, 6))
ax = figure.add_subplot(111) #we use the add_subplot() to create  the AxesSubplot to later remove the top and right spines

#changing the origin to be at point (5,5), we use the set_xlim() and set_ylim()
ax.set_xlim(5, ax.get_xlim()[1])
ax.set_xlim(5, ax.get_ylim()[1])


bars = plt.bar(fruits, quantities, color=[ripe_fruit_colors[fruit] for fruit in fruits])

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, str(height), ha='center', va='bottom')

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout() # Adjust layout to prevent clipping of labels


ax.spines['right'].set_visible(False) #we remove the right spines using the spines' set_visible() method
ax.spines['top'].set_visible(False) #we remove the top and right spines using the spines' set_visible() method

plt.title('Youth Preference on Fruits Origin(5,5)')
plt.show()