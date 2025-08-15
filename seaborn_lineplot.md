# Seaborn Theory

Seaborn is a Python data visualization library based on matplotlib.

## Key Features:
- Statistical plots
- Built-in themes
- Integration with pandas DataFrames

# Key Parameters :
1. Data Parameters
x: Values for the x-axis.
y: Values for the y-axis.
data: Dataset (e.g., Pandas DataFrame) where the variables x and y are defined.

2. Semantic Grouping Parameters
hue: Grouping variable that will produce lines with different colors.
style: Grouping variable that will produce lines with different styles (e.g., dashed, dotted).
size: Grouping variable that will produce lines with different thicknesses.

3. Aesthetic Parameters
palette: Colors to use for the hue variable.
dashes: Boolean or list to control line dashing styles.
markers: Boolean or list to control markers at data points.
legend: Controls the display of the legend ('auto', 'brief', 'full', or False).

4. Statistical Parameters
estimator: Function to aggregate data points (default is mean).
ci: Confidence interval to draw around the estimate (e.g., 95 for 95% CI, or None to suppress it).
n_boot: Number of bootstrap samples for computing confidence intervals.

5. Plot Customization Parameters
sort: Whether to sort data by the x-axis values before plotting (default is True).
err_style: Style of error visualization ('band' or 'bars').
err_kws: Additional keyword arguments for error bars.

6. Axes and Plot Control
ax: Matplotlib Axes object to draw the plot on.
kwargs: Additional keyword arguments passed to the underlying Matplotlib plot() function.
