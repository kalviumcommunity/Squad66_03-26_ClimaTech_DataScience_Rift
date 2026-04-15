# Milestone 3: Detecting Missing Values

## Overview
This milestone teaches you to identify and understand missing data in your datasets. Missing values can distort analysis, so detecting them first is critical for data quality assessment.

## Key Concepts Covered

### 1. Understanding Missing Data
- **NaN**: Not a Number - pandas representation of missing values
- **Null values**: Generic term for missing, absent, or undefined data
- **Sources**: Data entry errors, sensor failures, non-responses, incomplete records
- **Impact**: Skew calculations, reduce sample size, introduce bias

### 2. Detecting Missing Values
```python
# Check for NaN values
df.isnull()  # Boolean DataFrame (True where NaN)
df.isna()  # Same as isnull() (newer naming)
pd.isna(df['column'])  # For specific column

# Count missing
df.isnull().sum()  # Count per column
df.isnull().sum().sum()  # Total missing
df.isna().sum()  # Same as above

# Check specifics
df[df['column'].isnull()]  # Show rows with missing values
df[df['column'].notna()]  # Show rows WITHOUT missing values
```

### 3. Understanding Missing Data Patterns
```python
# Percentage missing per column
(df.isnull().sum() / len(df)) * 100

# Rows with any missing values
df[df.isnull().any(axis=1)]

# Complete rows only
df.dropna()

# Show which columns have missing
df.isnull().any()  # True/False per column
df.columns[df.isnull().any()]  # Names of columns with any NaN
```

### 4. Missing Data Mechanisms
- **MCAR**: Missing Completely At Random (no pattern)
- **MAR**: Missing At Random (missing related to other variables)
- **MNAR**: Missing Not At Random (missing systematically)

### 5. Analysis Without Fixing
```python
# Summarize missingness
missing_summary = pd.DataFrame({
    'Column': df.columns,
    'Missing Count': df.isnull().sum(),
    'Missing Percent': (df.isnull().sum() / len(df)) * 100
})
```

## Common Use Cases
- Data quality assessment before cleaning
- Identifying problematic columns
- Understanding data availability
- Deciding inclusion/exclusion criteria
- Planning data imputation strategy

## Best Practices
✓ Always check for missing values first
✓ Quantify missing data (count and percentage)
✓ Document where missing values originated
✓ Avoid dropping data without understanding impact
✓ Report missing data in final analysis

## Mistakes to Avoid
❌ Ignoring missing values (hoping they don't matter)
❌ Automatically removing rows with ANY missing value
❌ Using `dropna()` without knowing the consequences
❌ Not distinguishing between missing mechanisms
❌ Confusing NaN with 0 or empty strings

## Skills Mastered
- Detecting NaN values using `.isnull()` and `.isna()`
- Counting missing values per column and total
- Finding rows with missing data
- Calculating missing percentages
- Understanding different missing data patterns
- Assessing data quality from missingness perspective
