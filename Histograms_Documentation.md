# Milestone 9: Visualizing Data Distributions Using Histograms

## Overview
Histograms are fundamental tools for understanding how numeric data is distributed. This milestone teaches you to create, interpret, and use histograms to spot patterns, outliers, and data quality issues.

## Key Concepts Covered

### 1. Understanding Histograms
- **X-axis**: Value ranges (bins/buckets)
- **Y-axis**: Frequency (count of observations in each bin)
- **Bar height**: How many values fall into that range
- **Purpose**: Show WHERE most values cluster

### 2. Creating Histograms
```python
# Using pandas
df['column'].plot(kind='hist', bins=15)
df['column'].hist(bins=20)

# Using matplotlib
plt.hist(df['column'], bins=15, edgecolor='black', alpha=0.7)

# Customization
plt.hist(data, bins=20, color='blue', edgecolor='black', alpha=0.7)
plt.title('Distribution Title')
plt.xlabel('Value Label')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
```

### 3. Choosing Bins
```python
# Bin rules
# Rule 1: sqrt(n) where n = number of observations
import math
bins = int(math.sqrt(len(data)))

# Rule 2: Sturges' rule
bins = int(math.ceil(math.log2(len(data))) + 1)

# Rule 3: Default 10-30 bins (depends on data)
# Too few = coarse, too many = noisy
```

### 4. Distribution Shapes
- **Normal/Bell Curve**: Most data near center, symmetric
- **Right-skewed**: Long tail to the right, most data left
- **Left-skewed**: Long tail to the left, most data right
- **Bimodal**: Two peaks (two distinct groups)
- **Uniform**: Flat histogram (data spread evenly)

### 5. Using Histograms for Analysis
```python
# Spot outliers
plt.hist(data, bins=20)
# Look for isolated bars far from main cluster

# Check normality
plt.hist(data, bins=30)
# Check if roughly bell-shaped

# Compare multiple distributions
for col in ['col1', 'col2', 'col3']:
    plt.hist(df[col], bins=15, alpha=0.5, label=col)
plt.legend()

# Add reference lines
plt.axvline(df['column'].mean(), color='red', linestyle='--', label='Mean')
plt.axvline(df['column'].median(), color='blue', linestyle='--', label='Median')
```

## Distribution Interpretation Guide
| Shape | Indicator | What It Suggests |
|-------|-----------|-----------------|
| Normal | Peak center, symmetric | Data varies randomly around typical value |
| Right-skewed | Long right tail | High outliers pulling average up |
| Left-skewed | Long left tail | Low outliers pulling average down |
| Bimodal | Two peaks | Two distinct groups/subpopulations |
| Uniform | Flat | Data evenly distributed, no typical value |

## Common Use Cases
- Understanding data spread and variability
- Detecting outliers or data quality issues
- Checking if data is normally distributed
- Comparing distributions across groups
- Identifying skewness or multimodal patterns
- Deciding on appropriate statistical methods

## Best Practices
✓ Start with 20 bins, adjust based on clarity
✓ Use edgecolor='black' to separate bars clearly
✓ Add mean/median reference lines for context
✓ Label axes clearly with units
✓ Use transparency (alpha) when overlapping multiple histograms
✓ Always visualize BEFORE doing statistics

## Mistakes to Avoid
❌ Using too few bins (hide patterns) or too many (look noisy)
❌ Using histograms for categorical data (use bar charts)
❌ Ignoring outliers that appear as isolated bars
❌ Assuming similar means = similar distributions (visualize!)
❌ Not checking for bimodal or non-normal patterns
❌ Using histogram without inspecting its shape

## Skills Mastered
- Creating histograms with pandas and matplotlib
- Understanding and choosing appropriate bin sizes
- Interpreting different distribution shapes
- Identifying outliers visually
- Comparing multiple distributions
- Detecting normality and skewness
- Using histograms for exploratory analysis
