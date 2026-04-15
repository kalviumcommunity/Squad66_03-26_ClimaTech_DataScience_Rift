# Milestone 12: Exploring Relationships Between Variables Using Scatter Plots

## Overview
Scatter plots reveal how two numeric variables relate to each other. This milestone teaches you to create scatter plots, interpret correlation direction and strength, identify clusters and outliers, and use scatter plots to guide deeper analysis.

## Key Concepts Covered

### 1. Understanding Scatter Plots
- **Each point** = One observation with two values
- **X-axis** = First variable
- **Y-axis** = Second variable
- **Position** = Reflects the values of both variables
- **Pattern** = Shows the relationship between variables

### 2. Creating Scatter Plots
```python
# Basic scatter plot
plt.scatter(df['Variable1'], df['Variable2'])

# With styling
plt.scatter(df['X'], df['Y'], s=100, alpha=0.6, color='blue')

# Multiple series
plt.scatter(df[df['Group']=='A']['X'], df[df['Group']=='A']['Y'], label='Group A')
plt.scatter(df[df['Group']=='B']['X'], df[df['Group']=='B']['Y'], label='Group B')
plt.legend()

# Add trend line
z = np.polyfit(df['X'], df['Y'], 1)
p = np.poly1d(z)
plt.plot(df['X'], p(df['X']), "r--", alpha=0.8)
```

### 3. Interpreting Relationships
- **Positive correlation**: Points trend UP from left to right (one increases, so does the other)
- **Negative correlation**: Points trend DOWN from left to right (one increases, other decreases)
- **No correlation**: Points scattered randomly with no clear pattern
- **Linear relationship**: Points follow roughly a straight line
- **Non-linear relationship**: Points follow a curved or complex pattern

### 4. Identifying Clusters and Outliers
- **Clusters**: Groups of points close together (distinct segments)
- **Outliers**: Points far from the main pattern (isolated or unusual)
- **Separation**: Clear distance between groups suggests distinct subpopulations
- **Extreme points**: Unusually high/low combinations

### 5. Reading Scatter Plot Patterns
```python
# Correlation strength interpretation
# r ≈ 1: Strong positive relationship
# r ≈ 0.5: Moderate positive relationship
# r ≈ 0: No clear relationship
# r ≈ -0.5: Moderate negative relationship
# r ≈ -1: Strong negative relationship
```

## Common Use Cases
- Student study hours vs test scores
- Product price vs sales volume
- Temperature vs ice cream sales
- Employee experience vs salary
- Website traffic vs conversion rate
- Ad spend vs revenue generated

## Best Practices
✓ Use scatter plots to explore relationships early
✓ Combine with correlation coefficients (but visualize first!)
✓ Look for linear AND non-linear patterns
✓ Investigate clusters and isolated points
✓ Don't infer causation from scatter plots alone
✓ Use multiple scatter plots to understand complex relationships

## Mistakes to Avoid
❌ Confusing scatter plots with line plots (scatter shows relationship, not sequence)
❌ Assuming scatter plot correlation = causation
❌ Using scatter plots for categorical variables
❌ Ignoring outliers that might reveal important insights
❌ Over-interpreting weak patterns in small samples
❌ Missing non-linear relationships (look beyond straight lines!)

## Skills Mastered
- Creating scatter plots for two-variable analysis
- Interpreting positive, negative, and no correlation
- Identifying linear and non-linear patterns
- Spotting clusters and segments in data
- Recognizing and investigating outliers
- Using scatter plots to guide exploratory analysis
- Understanding when causation claims are justified
