# Milestone 4: Handling Missing Values - Drop and Fill Strategies

## Overview
This milestone teaches you to handle missing values strategically. You'll learn when to drop incomplete records, when to fill missing values, and how to choose the right approach for your analysis.

## Key Concepts Covered

### 1. Two Main Strategies
- **Drop**: Remove rows or columns with missing values
- **Fill**: Impute/estimate missing values with reasonable replacements

### 2. Dropping Missing Data
```python
# Remove rows with any NaN
df.dropna()  # New DataFrame without any NaN

# Remove rows where specific column is NaN
df.dropna(subset=['column_name'])

# Remove columns with ANY missing value
df.dropna(axis=1)  # axis=1 means columns

# Remove rows where ALL values are NaN
df.dropna(how='all')  # Default is 'any'

# Threshold-based dropping
df.dropna(thresh=3)  # Keep rows with at least 3 non-NaN values
```

### 3. Forward and Backward Fill
```python
# Forward fill: Use previous value
df.fillna(method='ffill')  # Propagate value forward

# Backward fill: Use next value
df.fillna(method='bfill')  # Propagate value backward

# Time series example:
df['value'].fillna(method='ffill')  # Fill with previous measurement
```

### 4. Filling with Specific Values
```python
# Fill with constant
df.fillna(0)  # Replace NaN with 0
df['column'].fillna('Unknown')  # Fill with default value

# Fill with statistical measure
df.fillna(df.mean())  # Fill with column mean
df.fillna(df.median())  # Fill with column median
df.fillna(df.mode()[0])  # Fill with column mode

# Fill per column
df.fillna({'col1': 0, 'col2': 'Unknown', 'col3': df['col3'].mean()})
```

### 5. Interpolation (for numeric series)
```python
# Linear interpolation
df['column'].interpolate()  # Connect gaps linearly

# Different methods
df['column'].interpolate(method='linear')
df['column'].interpolate(method='polynomial', order=2)
```

## Decision Framework
| Scenario | Strategy | Reason |
|----------|----------|--------|
| <5% missing | Drop rows | Minimal data loss |
| Systematic missing | Understand pattern first | May indicate data quality issue |
| Time series | Forward fill | Reasonable for sequential data |
| Categorical | Mode or 'Unknown' | Most common value |
| Numeric | Mean/median | Preserves distribution |
| Entire column missing | Drop column | No information to recover |

## Common Use Cases
- Removing incomplete survey responses
- Forward-filling sensor readings over time
- Imputing average values for analysis
- Handling customer data gaps
- Preparing data for modeling

## Best Practices
✓ Understand WHY values are missing first
✓ Document your handling strategy
✓ Preserve original data; create modified copy
✓ Consider impact on analysis before filling
✓ Report how many values were filled
✓ Validate filled values make sense

## Mistakes to Avoid
❌ Blindly dropping rows without understanding impact
❌ Using mean for skewed distributions (use median)
❌ Not documenting what you did
❌ Forward-filling when no temporal relationship exists
❌ Dropping entire columns without checking importance
❌ Filling without considering data type

## Skills Mastered
- Dropping rows and columns with missing values
- Forward and backward fill strategies
- Filling with constants and statistical measures
- Interpolation for numeric series
- Per-column filling strategies
- Understanding appropriate handling is context-dependent
