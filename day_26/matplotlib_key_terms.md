# 📚 Matplotlib Key Terms

## 🎨 The Basics: Figure and Axes

Think of a Figure as the entire canvas or window for your plot. It's the top-level container. The Axes is the actual plotting area inside the Figure where your data points are drawn with an x-axis and y-axis. You can have multiple Axes on a single Figure.

- 🖼️ **Figure**: The whole window or page.
- 📊 **Axes**: The individual plot or graph area.

## 📈 Data and Plotting

- 📍 **Data Point**: A single piece of information, usually represented as a coordinate pair like (x,y).
- 📏 **X-axis & Y-axis**: The horizontal (x-axis) and vertical (y-axis) lines that provide the frame of reference for your data points.
- 📊 **Plot**: The visual representation of your data on the Axes. This could be a line graph, scatter plot, bar chart, etc. The command `plt.plot()` or `ax.plot()` creates it.

## ✨ Customizing the Look

These are arguments you pass to functions like plot() to change how your graph looks.

- 🔵 **Marker**: The symbol used to show a specific data point. Common markers are circles ('o'), squares ('s'), or triangles ('^').
- 📈 **Line Style**: The pattern of the line connecting data points. For example, a solid line ('-'), a dashed line ('--'), or a dotted line (':').
- 🌈 **Color**: Sets the color of your lines and markers. You can use names like 'red' or 'blue'.

```python
# Example of customizing a plot
plt.plot(x_data, y_data, color='green', marker='o', linestyle='--')
```

## 🏷️ Labels and Information

These elements help people understand your plot.

- 📝 **Title**: The main heading for your Axes (the plot).
- 🔤 **Label**: The text used to name the x-axis (xlabel) and y-axis (ylabel). It's also used to identify a specific line in the legend.
- 🗂️ **Legend**: A small box that explains what each line or color on your plot represents. It uses the label you provided for each plot.
- 🔲 **Grid**: A set of faint lines in the background that help you read the values on the plot more easily.

## 💻 Programming Concepts

- 🔧 **Function**: A standalone command that performs an action, like `plt.figure()` or `plt.plot()`. This is part of Matplotlib's simple pyplot interface.
- ⚙️ **Method**: A function that belongs to an object. For example, `ax.set_title()` is a method of the Axes object ax. This is used in the Object-Oriented API.
- 📋 **Parameter**: A variable in a function's definition.
- 🔑 **Keyword Arguments (kwargs)**: When you call a function and specify the parameter name, like `color='red'`. This makes your code more readable.
- 🎯 **Object-Oriented API**: A more powerful and flexible way to create plots. Instead of using global plt functions, you create and control Figure and Axes objects explicitly (e.g., `fig, ax = plt.subplots()`). This is the recommended approach for complex plots.

## 🖥️ Output and Rendering

- 🔍 **DPI (Dots Per Inch)**: This controls the resolution of your saved image. A higher DPI (e.g., dpi=300) results in a sharper, higher-quality image file.
- 🎪 **Backend**: The "engine" that Matplotlib uses to draw the plot. It determines whether the plot is shown in a window on your screen (interactive backend) or saved to a file like a PNG or PDF (non-interactive backend). You usually don't need to worry about this.

