# Milestone 1: Inspecting DataFrames - Shape and Data Types

## Overview
This milestone teaches you to understand the structure of your data before any analysis. Learning to inspect DataFrames using `.shape`, `.info()`, `.dtypes`, and `.head()` helps you quickly understand what you're working with.

## Key Concepts Covered

### 1. Understanding DataFrame Structure
- **Shape**: (rows, columns) tuple showing dataset dimensions
- **Rows**: Individual observations or records
- **Columns**: Features or attributes of each observation
- **Data types**: Type of values in each column (int, float, object, datetime, etc.)

### 2. Essential Inspection Methods
```python
# View dimensions
df.shape  # Returns (rows, columns)
df.shape[0]  # Number of rows
df.shape[1]  # Number of columns

# View first/last rows
df.head()  # First 5 rows
df.head(10)  # First 10 rows
df.tail()  # Last 5 rows

# Get detailed info
df.info()  # Column names, types, non-null counts

# Check data types
df.dtypes  # Dictionary of column -> type
df['column'].dtype  # Single column type

# Basic statistics
df.describe()  # Summary stats (count, mean, min, max, etc.)
```

### 3. Data Type Understanding
- **int**: Integer numbers (whole numbers)
- **float**: Decimal numbers
- **object**: Text strings or mixed types
- **datetime**: Date and time values
- **bool**: True/False values

### 4. Memory and Size Considerations
```python
df.memory_usage()  # Memory per column
df.memory_usage().sum()  # Total memory in bytes
```

### 5. Common Inspection Workflows
1. **First look**: `df.shape` → How big is this?
2. **Column names**: `df.columns` → What do I have?
3. **Data types**: `df.dtypes` → Are they correct?
4. **Sample data**: `df.head()` → What does it look like?
5. **Missing values**: `df.isnull().sum()` → Any gaps?

## Common Use Cases
- Verifying data was loaded correctly
- Checking column names and spelling
- Ensuring dates aren't stored as strings
- Identifying incorrect data types
- Understanding data volume before processing

## Best Practices
✓ Always inspect first - before any transformation
✓ Check `df.info()` to spot data type problems early
✓ Use `.describe()` to get quick statistics
✓ Store shape in variables for later reference
✓ Document expected types in analysis notes

## Mistakes to Avoid
❌ Assuming data is correct without checking
❌ Working with wrong data types (dates as strings)
❌ Ignoring memory implications for large datasets
❌ Not checking for unexpected column names
❌ Processing data you don't understand

## Skills Mastered
- Using `.shape` to understand dataset dimensions
- Inspecting data types with `.dtypes` and `.info()`
- Viewing sample data with `.head()` and `.tail()`
- Getting summary statistics with `.describe()`
- Identifying data structure issues early
- Understanding memory implications
