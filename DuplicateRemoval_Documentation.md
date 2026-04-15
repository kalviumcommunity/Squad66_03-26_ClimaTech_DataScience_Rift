# Milestone 5: Removing Duplicate Records

## Overview
This milestone teaches you to identify and remove duplicate records from your dataset. Duplicates can skew analysis, so cleaning them is essential for data integrity.

## Key Concepts Covered

### 1. Understanding Duplicates
- **Exact duplicates**: Identical rows across all columns
- **Partial duplicates**: Same values in some columns but different in others
- **Unintended duplicates**: Data entry errors, import mistakes
- **Intentional duplicates**: Same ID appearing legitimately multiple times

### 2. Detecting Duplicates
```python
# Check for exact duplicates
df.duplicated()  # Boolean Series (True for duplicates)

# Count duplicates
df.duplicated().sum()  # Number of duplicate rows

# Show duplicate rows
df[df.duplicated()]  # Show rows that ARE duplicates
df[df.duplicated(keep=False)]  # Show all duplicates (keep originals too)

# Duplicates based on specific columns
df.duplicated(subset=['column1', 'column2'])
```

### 3. The `keep` Parameter
```python
# keep='first' (default): Mark all but first as duplicate
df.duplicated(keep='first')

# keep='last': Mark all but last as duplicate
df.duplicated(keep='last')

# keep=False: Mark ALL duplicates (including first)
df.duplicated(keep=False)
```

### 4. Removing Duplicates
```python
# Remove all duplicate rows (keep first occurrence)
df.drop_duplicates()  # Same as drop_duplicates(keep='first')

# Keep last occurrence instead
df.drop_duplicates(keep='last')

# Keep all (remove nothing)
df.drop_duplicates(keep=False)

# Remove duplicates based on specific columns
df.drop_duplicates(subset=['CustomerID'])  # Keep first per customer

# Multiple columns
df.drop_duplicates(subset=['First', 'Last'])  # Name combinations
```

### 5. Common Scenarios
```python
# Keep one record per customer (most recent)
df.sort_values('date').drop_duplicates(subset=['CustomerID'], keep='last')

# Remove complete duplicates
df.drop_duplicates()

# Remove duplicates on key columns
df.drop_duplicates(subset=['email'])  # Keep one per email
```

## Decision Framework
| Scenario | Action | Reason |
|----------|--------|--------|
| Exact same row twice | Remove one | Accidental duplication |
| Same customer, different times | Keep both or last? | Depends on analysis goal |
| Same name, different email | Keep both | Different people |
| Same ID, multiple purchases | Keep all | Legitimate transactions |

## Common Use Cases
- Cleaning imported data
- Removing test records
- Consolidating customer records
- De-duplicating email lists
- Preparing data for model training

## Best Practices
✓ Always check for duplicates first
✓ Understand which duplicates are intentional
✓ Use `keep='last'` if timestamps suggest newer is better
✓ Document how many were removed
✓ Preserve original data; create modified copy
✓ Verify removal doesn't harm analysis

## Mistakes to Avoid
❌ Removing all duplicates without understanding implications
❌ Using `drop_duplicates()` on every column (loses intentional duplicates)
❌ Not sorting before keeping 'last'
❌ Confusing `duplicated()` (returns boolean) with `drop_duplicates()` (returns DataFrame)
❌ Not checking subset combinations make business sense
❌ Silently dropping data without documentation

## Skills Mastered
- Detecting duplicates with `.duplicated()`
- Understanding the `keep` parameter
- Counting and displaying duplicate rows
- Removing duplicates with `.drop_duplicates()`
- Removing duplicates on subset of columns
- Preserving legitimate duplicates while removing unintended ones
