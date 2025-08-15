# Seaborn Theory

Seaborn is a Python data visualization library based on matplotlib.

## Key Features:
- Statistical plots
- Built-in themes
- Integration with pandas DataFrames
  
# Key Parameters :
1. data:
The dataset to be visualized, typically a Pandas DataFrame.

2. x / y:
The variable(s) to plot on the x-axis or y-axis.

3. bins:
Number of bins (bar groups) to divide the data into.

4. binwidth:
The width of each bin. Overrides bins if specified.

5. binrange:
A tuple specifying the range of bins (e.g., (min, max)).

6. hue:
Variable to group data by color.

7. multiple:
How to display multiple distributions:

> 'layer' (default)
> 'stack'
> 'dodge'
> 'fill'
> 
9. stat:
Determines the bar height:

> 'count' (default)
> 'frequency'
> 'density'
> 'probability'
10. kde:
If True, overlays a Kernel Density Estimate (KDE) curve.

11. color:
Specifies the color of the bars.

12. alpha:
Transparency level of the bars (0 = fully transparent, 1 = fully opaque).

13. element:
Style of bars:

>'bars' (default)
>'step'
>'poly'

14. fill:
If True, fills the bars or steps.

15. discrete:
If True, treats the data as discrete rather than continuous.

16. log_scale:
If True, applies a logarithmic scale to the axes.