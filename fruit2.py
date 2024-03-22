import matplotlib.pyplot as plt

# Fruit data
fruits = ['Avocados', 'Oranges', 'Bananas', 'Kiwifruit', 'Mangoes', 'Grapes']
quantities = [36, 41, 19, 28, 30, 16]

# Fruit colors
colors = ['green', 'orange', 'yellow', 'brown', 'orange', 'purple']

# Plot the bar chart
plt.bar(range(len(fruits)), quantities, color=colors)

# Set the labels for x-axis
plt.xticks(range(len(fruits)), fruits)

# Set labels for x and y axes
plt.xlabel('Fruits')
plt.ylabel('Quantities')

# Set the title of the plot
plt.title('Fruit Preference Bar Chart')

# Set the origin to (0, 0)
plt.xlim(left=-0.5)  # Shift the left limit to -0.5
plt.ylim(bottom=0)   # Set the bottom limit to 0

# Show the plot
plt.show()
