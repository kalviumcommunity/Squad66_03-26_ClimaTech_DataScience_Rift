# Milestone 6: Standardizing Data Formats

## Overview
This milestone teaches you to ensure consistent formatting across your dataset. Standardizing column names, data types, and value formats prevents errors and enables seamless analysis.

## Key Concepts Covered

### 1. Standardizing Column Names
```python
# Strip whitespace
df.columns = df.columns.str.strip()

# Lowercase all columns
df.columns = df.columns.str.lower()

# Replace spaces with underscores
df.columns = df.columns.str.replace(' ', '_')

# Combined standardization
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Rename specific columns
df.rename(columns={'Old Name': 'new_name', 'Another': 'another'}, inplace=True)
```

### 2. Standardizing Text Data
```python
# Lowercase all text
df['column'] = df['column'].str.lower()

# Uppercase
df['column'] = df['column'].str.upper()

# Remove leading/trailing whitespace
df['column'] = df['column'].str.strip()

# Remove extra spaces within text
df['column'] = df['column'].str.replace(r'\s+', ' ', regex=True)

# Consistent casing (title case)
df['column'] = df['column'].str.title()
```

### 3. Standardizing Numeric Data
```python
# Remove currency symbols
df['column'] = df['column'].str.replace('$', '').astype(float)

# Remove commas in large numbers
df['column'] = df['column'].str.replace(',', '').astype(float)

# Ensure float type
df['column'] = df['column'].astype(float)

# Round to consistent decimals
df['column'] = df['column'].round(2)
```

### 4. Standardizing Date Formats
```python
# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Specify format
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# Consistent date string format
df['date_str'] = df['date'].dt.strftime('%Y-%m-%d')
```

### 5. Standardizing Categorical Values
```python
# Map old values to new
df['column'] = df['column'].map({
    'Y': 'Yes',
    'N': 'No',
    'M': 'Male',
    'F': 'Female'
})

# Replace multiple similar values
df['column'] = df['column'].replace(['yes', 'Yes', 'YES'], 'Yes')

# Fill with standard value if missing
df['column'].fillna('Unknown')
```

## Common Standardization Scenarios
| Issue | Solution | Example |
|-------|----------|---------|
| Column names with spaces | Use underscores | "First Name" → "first_name" |
| Mixed case text | Lowercase or standardize | "John", "JOHN" → "john" |
| Extra whitespace | Strip whitespace | "  value  " → "value" |
| Currency formatting | Remove symbols, convert to float | "$1,000.50" → 1000.50 |
| Date inconsistency | Convert to datetime | "01/15/2024" → 2024-01-15 |
| Categorical inconsistency | Map to standard values | "Yes", "Y", "1" → "Yes" |

## Common Use Cases
- Preparing data from multiple sources
- Cleaning survey data with inconsistent entries
- Standardizing across different departments
- Preparing for database import
- Ensuring reproducibility

## Best Practices
✓ Create a standardization plan before editing
✓ Apply changes to copies first, verify, then overwrite
✓ Document all transformations
✓ Use consistent naming conventions (snake_case recommended)
✓ Preserve original data as backup
✓ Test transformations on sample before applying to full dataset

## Mistakes to Avoid
❌ Making case-based assumptions (John vs john)
❌ Not handling leading/trailing whitespace
❌ Inconsistent date formats in same column
❌ Mixing currencies or units
❌ Losing information during format conversion
❌ Not documenting transformations

## Skills Mastered
- Standardizing column names
- Cleaning and standardizing text data
- Converting and formatting numeric data
- Handling dates consistently
- Mapping categorical values to standards
- Creating reproducible data standardization pipelines
