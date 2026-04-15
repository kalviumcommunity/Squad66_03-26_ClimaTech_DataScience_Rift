# Milestone 10: Visualizing Distributions Using Boxplots

## Overview
Boxplots are one of the most powerful visualization tools for understanding data distributions at a glance. This milestone teaches you to create boxplots, interpret their components, and use them for comparing distributions across multiple variables.

## Key Concepts Covered

### 1. Understanding Boxplots
- **5-number summary**: Minimum, Q1 (25%), Median (50%), Q3 (75%), Maximum
- **Box**: Contains the middle 50% of data (IQR)
- **Whiskers**: Extend to min/max (or 1.5*IQR)
- **Outliers**: Shown as individual points beyond whiskers
- **Median line**: The horizontal line inside the box

### 2. Creating Boxplots
```python
# Basic boxplot
df.boxplot(column='Daily Sales')

# Multiple columns comparison
df.boxplot()

# With matplotlib customization
fig, ax = plt.subplots()
df.boxplot(ax=ax)
ax.set_title("Distribution Comparison")
```

### 3. Interpreting Boxplots
- **Tall box** = High variability, data spread out
- **Short box** = Low variability, consistent data
- **Median position** in box = Symmetric (centered) or skewed (off-center)
- **Points beyond whiskers** = Outliers (rare or unusual values)
- **Box position** = Overall level of the variable

### 4. Comparing Multiple Distributions
- Side-by-side boxplots show differences between groups
- Easy to spot which column has highest/lowest values
- Easy to spot which column has more variability
- Enables quick comparison without complex statistics

### 5. Identifying Outliers
```python
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['column'] < lower_bound) | (df['column'] > upper_bound)]
```

## Common Use Cases
- Store performance comparison (side-by-side sales distributions)
- Quality control across production lines
- Student grades by subject
- Customer metrics across regions
- Test scores across groups

## Best Practices
✓ Always label axes clearly
✓ Use multiple boxplots to compare distributions
✓ Investigate outliers before removing them
✓ Combine with other visualizations (histograms, scatter plots)
✓ Document any data transformations or filtering

## Mistakes to Avoid
❌ Treating all outliers as errors (investigate first!)
❌ Confusing box height with data quality
❌ Ignoring the median line position
❌ Using boxplots for categorical data
❌ Over-interpreting small samples

## Skills Mastered
- Creating single and multiple boxplots
- Interpreting box components
- Detecting outliers mathematically
- Comparing distributions visually
- Making data-driven decisions about extreme values
