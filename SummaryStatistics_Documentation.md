# Milestone 7: Computing Summary Statistics for Columns

## Overview
This milestone teaches you to calculate and interpret summary statistics. These metrics provide quick insights into data characteristics, central tendency, spread, and overall distribution.

## Key Concepts Covered

### 1. Central Tendency Measures
```python
# Mean (average)
df['column'].mean()  # Sum of all values / count

# Median (middle value)
df['column'].median()  # 50th percentile

# Mode (most frequent)
df['column'].mode()  # Returns Series, use [0] to get value

# When to use each:
# Mean: Normal distributions, continuous data
# Median: Skewed data, presence of outliers
# Mode: Categorical data, identifying common values
```

### 2. Spread/Dispersion Measures
```python
# Standard Deviation
df['column'].std()  # Measure of spread (same units as data)

# Variance
df['column'].var()  # Squared standard deviation

# Range
df['column'].max() - df['column'].min()  # Difference between extremes

# Interquartile Range (IQR)
Q3 = df['column'].quantile(0.75)
Q1 = df['column'].quantile(0.25)
IQR = Q3 - Q1  # Middle 50% spread
```

### 3. Percentiles and Quantiles
```python
# Specific percentiles
df['column'].quantile(0.25)  # 25th percentile (Q1)
df['column'].quantile(0.50)  # 50th percentile (median)
df['column'].quantile(0.75)  # 75th percentile (Q3)

# Multiple at once
df['column'].quantile([0.25, 0.50, 0.75])

# Common usage
first_half = df[df['column'] <= df['column'].median()]
top_quarter = df[df['column'] >= df['column'].quantile(0.75)]
```

### 4. All-at-Once Summary
```python
# Comprehensive statistics
df.describe()  # Returns count, mean, std, min, 25%, 50%, 75%, max

# Per column
df['column'].describe()

# Custom percentiles
df.describe(percentiles=[0.05, 0.25, 0.50, 0.75, 0.95])

# For object (string) columns
df.describe(include=['object'])

# All data types
df.describe(include='all')
```

### 5. Aggregate Functions
```python
# Count non-null values
df['column'].count()

# Sum
df['column'].sum()

# Min and Max
df['column'].min()
df['column'].max()

# Multiple aggregations
df['column'].agg(['mean', 'median', 'std', 'min', 'max'])

# Custom aggregation
df['column'].agg(lambda x: x.max() - x.min())  # Range
```

## Interpretation Guide
| Statistic | Interpretation | Use For |
|-----------|-----------------|---------|
| Mean | Average value | Overall level, symmetric data |
| Median | Middle value | Skewed data, robust to outliers |
| Std Dev | Typical spread | Understanding variability |
| Min/Max | Extremes | Identifying ranges, outliers |
| Percentiles | Positional values | Understanding distribution |
| Skewness | Distribution shape | Detecting non-normal data |

## Common Use Cases
- Understanding data range and typical values
- Comparing distributions across groups
- Identifying outliers (<Q1-1.5*IQR or >Q3+1.5*IQR)
- Detecting skewness or non-normal distributions
- Creating data quality reports

## Best Practices
✓ Use mean with caution if outliers present (use median instead)
✓ Combine central tendency with spread measures
✓ Look at `describe()` to spot data quality issues
✓ Use percentiles for distribution understanding
✓ Compare statistics across different groups

## Mistakes to Avoid
❌ Using only mean without considering outliers
❌ Assuming normal distribution without verification
❌ Not checking std deviation (could indicate problem)
❌ Ignoring that statistics hide distribution shape
❌ Using mean on skewed data (use median)

## Skills Mastered
- Computing mean, median, mode
- Calculating spread measures (std, variance, range)
- Understanding percentiles and quantiles
- Using `.describe()` for comprehensive summaries
- Aggregating data multiple ways
- Interpreting statistics in context
