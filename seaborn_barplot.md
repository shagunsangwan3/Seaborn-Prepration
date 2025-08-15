# Seaborn Theory

Seaborn is a Python data visualization library based on matplotlib.

## Key Features:
- Statistical plots
- Built-in themes
- Integration with pandas DataFrames

# Key Parameters : 
1. Data and Axes Parameters
x: Categorical variable for the x-axis.
y: Numerical variable for the y-axis.
data: DataFrame or dataset containing the variables.
hue: Grouping variable to create subcategories within bars.

1. Statistical Parameters
estimator: Function to calculate the central tendency (default is np.mean).
ci: Confidence interval size for error bars (default is 95). Use None to hide error bars.
n_boot: Number of bootstrap iterations for computing confidence intervals.

1. Appearance Parameters
palette: Color palette for the bars.
orient: Orientation of the plot ('v' for vertical, 'h' for horizontal).
saturation: Intensity of bar colors (default is 0.75).

1. Advanced Parameters
order: Custom order for categorical levels on the x-axis.
hue_order: Custom order for levels of the hue variable.
dodge: Whether to separate bars for different hue levels (default is True).
width: Width of the bars (default is 0.8).
errcolor: Color of the error bars.
capsize: Width of the caps on error bars.

1. Axes and Plot Customization
ax: Matplotlib Axes object to draw the plot on.
kwargs: Additional keyword arguments passed to matplotlib.axes.Axes.bar.