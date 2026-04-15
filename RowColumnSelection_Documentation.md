# Milestone 2: Selecting Rows and Columns Using iloc and loc

## Overview
This milestone teaches you to select specific data from DataFrames. Mastering `iloc` (integer location) and `loc` (label location) enables you to extract exactly what you need for analysis.

## Key Concepts Covered

### 1. Understanding Indexing
- **Row index**: The row label (0, 1, 2, ... or custom names)
- **Column index**: The column name or position
- **Integer position**: 0-based index regardless of labels
- **Slicing**: Using ranges to select multiple items

### 2. The Two Main Methods
```python
# iloc: Integer-location based selection
df.iloc[0]  # First row
df.iloc[0:5]  # Rows 0-4 (excludes 5)
df.iloc[:, 0]  # All rows, first column
df.iloc[0:5, 1:3]  # Rows 0-4, columns 1-2

# loc: Label-based selection
df.loc['row_label']  # Specific row by name
df.loc[['A', 'B']]  # Multiple rows by label
df.loc[:, 'column_name']  # All rows, specific column
df.loc[0:5, 'start_col':'end_col']  # Rows and columns by label
```

### 3. Selecting Specific Rows
```python
# Single row
df.iloc[0]  # First row as Series
df.iloc[[0]]  # First row as DataFrame (keep 2D)

# Multiple rows
df.iloc[0:10]  # Rows 0-9
df.iloc[[0, 2, 5]]  # Non-consecutive rows

# Last rows
df.iloc[-1]  # Last row
df.iloc[-5:]  # Last 5 rows
```

### 4. Selecting Specific Columns
```python
# Single column (two ways)
df['column_name']  # Returns Series
df[['column_name']]  # Returns DataFrame

# Multiple columns
df[['col1', 'col2', 'col3']]
df.iloc[:, 0:3]  # First 3 columns
df.iloc[:, [0, 2, 4]]  # Non-consecutive columns
```

### 5. Conditional Selection
```python
# Boolean filtering
df[df['age'] > 30]  # Rows where age > 30
df[df['name'] == 'John']  # Rows matching condition
df[(df['age'] > 25) & (df['salary'] < 100000)]  # Multiple conditions
```

## Common Use Cases
- Extracting specific rows for analysis
- Getting subsets of columns for visualization
- Filtering data by conditions
- Creating new DataFrames from selected data
- Splitting data into train/test sets

## Best Practices
✓ Use `.iloc` when you know position numbers
✓ Use `.loc` when you know row/column names
✓ Use `df[['col1', 'col2']]` for quick column selection
✓ Always use double brackets `[[]]` to keep DataFrame structure
✓ Use boolean indexing for conditional filtering

## Mistakes to Avoid
❌ Confusing `.iloc` (position) with `.loc` (label)
❌ Using single brackets for column selection expecting DataFrame
❌ Forgetting second index for 2D selection
❌ Using `.iloc[-1]` expecting last element (it works but confuses many)
❌ Not using double brackets when structure matters

## Skills Mastered
- Integer-location based selection with `.iloc`
- Label-based selection with `.loc`
- Selecting rows and columns independently
- Combined row and column selection
- Boolean/conditional filtering
- Maintaining DataFrame structure vs converting to Series
