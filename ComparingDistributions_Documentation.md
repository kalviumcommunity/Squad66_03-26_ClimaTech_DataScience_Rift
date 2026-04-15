# Milestone 8: Comparing Distributions Across Multiple Columns

## Overview
This milestone teaches you to compare how different columns are distributed. Understanding whether columns have similar patterns, spread, and central tendency helps identify relationships and differences in your data.

## Key Concepts Covered

### 1. Side-by-Side Comparison
```python
# Compare statistics across columns
df[['col1', 'col2', 'col3']].describe()

# Transpose for easier comparison
df[['col1', 'col2', 'col3']].describe().T

# Custom statistics for comparison
df[['col1', 'col2', 'col3']].agg(['mean', 'median', 'std', 'min', 'max'])
```

### 2. Visual Comparison
```python
# Side-by-side histograms
df[['col1', 'col2', 'col3']].plot(kind='hist', bins=20, alpha=0.5)

# Boxplots for distribution comparison
df[['col1', 'col2', 'col3']].plot(kind='box')

# Compare column distributions visually
plt.figure()
for col in ['col1', 'col2', 'col3']:
    df[col].hist(bins=20, alpha=0.5, label=col)
plt.legend()
```

### 3. Statistical Comparison Metrics
```python
# Skewness (asymmetry)
df['column'].skew()  # Positive = right-skewed, Negative = left-skewed

# Kurtosis (tail heaviness)
df['column'].kurtosis()

# Coefficient of Variation (relative spread)
cv = (df['column'].std() / df['column'].mean()) * 100

# Compare across columns
comparison = df[['col1', 'col2']].apply(lambda x: (x.std() / x.mean()) * 100)
```

### 4. Grouping and Comparing
```python
# Compare distributions by group
df.groupby('category_col')[['numeric_col1', 'numeric_col2']].describe()

# Compare within groups
df.groupby('group')['value'].agg(['mean', 'std', 'min', 'max'])

# Multiple grouping
df.groupby(['group1', 'group2'])['value'].mean()
```

### 5. Common Comparison Patterns
```python
# Before/After comparison
before = df[df['date'] < '2024-01-01']['sales'].describe()
after = df[df['date'] >= '2024-01-01']['sales'].describe()

# Region comparison
regions = df.groupby('region')[['revenue', 'cost']].describe()

# Product comparison
products = df.groupby('product')['price'].agg(['mean', 'std', 'count'])
```

## Comparison Interpretation
| Finding | Interpretation | Implication |
|---------|-----------------|-------------|
| Similar means, different stds | Same level, different spread | One more variable/risky |
| Different means, similar stds | Different levels, same consistency | Genuine differences |
| Both very different | Distinct distributions | Fundamentally different |
| Mean >> Median (right-skewed) | High outliers pulling average | Use median for typical value |
| Mean << Median (left-skewed) | Low outliers pulling average | Use median for typical value |

## Common Use Cases
- Comparing performance across regions/stores
- Before vs after analysis
- Product quality across batches
- Customer segments comparison
- Testing effectiveness (control vs treatment)

## Best Practices
✓ Always visualize alongside statistics
✓ Compare mean AND median (tells distribution story)
✓ Look at spread (std dev) not just central tendency
✓ Check sample sizes when comparing
✓ Document which columns are comparable

## Mistakes to Avoid
❌ Comparing columns with different units/scales
❌ Using mean alone without considering spread
❌ Ignoring that similar means can hide different distributions
❌ Forgetting to visualize (numbers alone misleading)
❌ Not checking for statistical significance

## Skills Mastered
- Computing descriptive statistics across multiple columns
- Comparing distributions side-by-side
- Using `.groupby()` for comparative analysis
- Visualizing multiple distributions simultaneously
- Understanding when columns are similar vs different
- Identifying key differences between distributions
