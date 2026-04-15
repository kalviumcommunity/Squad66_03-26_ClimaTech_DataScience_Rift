# Milestone 13: Detecting Outliers Using Visual Inspection and Simple Rules

## Overview
Outliers are data points that differ significantly from the majority. This milestone teaches you to detect outliers using visual tools and statistical rules, interpret them carefully, and make informed decisions about how to handle them.

## Key Concepts Covered

### 1. Understanding Outliers
- **Definition**: Data points significantly different from the rest of the distribution
- **Impact**: Can skew statistics, compress visualizations, distort analyses
- **Types**:
  - **Valid outliers**: Legitimate extreme observations (e.g., CEO salary)
  - **Data errors**: Impossible or incorrect values (e.g., age = -5)
  - **Measurement errors**: Sensor malfunction or collection issues

### 2. Visual Inspection Methods
```python
# Method 1: Boxplot inspection
plt.boxplot(df['column'])  # Look for isolated points beyond whiskers

# Method 2: Histogram inspection
plt.hist(df['column'], bins=20)  # Look for separated bars

# Method 3: Scatter plot inspection
plt.scatter(df['X'], df['Y'])  # Look for isolated or extreme clusters
```

### 3. Statistical Detection Rules
```python
# IQR Method (Interquartile Range)
Q1 = df['column'].quantile(0.25)
Q3 = df['column'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['column'] < lower_bound) | (df['column'] > upper_bound)]

# Threshold Method (Domain Knowledge)
outliers = df[(df['Age'] < 18) | (df['Age'] > 100)]

# Standard Deviation Method
mean = df['column'].mean()
std = df['column'].std()
outliers = df[(df['column'] > mean + 2*std) | (df['column'] < mean - 2*std)]
```

### 4. Outlier Interpretation Framework
**Step 1: Detection** (Visual + Rule) ✓
**Step 2: Investigation** (Ask questions)
- Is this value physically possible?
- Does it align with domain expectations?
- Are there related context clues?
- When/how was it collected?

**Step 3: Classification**
- **VALID** → Keep and note in analysis
- **ERROR** → Fix or remove after tracing source
- **UNCERTAIN** → Document and flag for review

**Step 4: Documentation**
- What was the outlier?
- Why was it classified as such?
- What decision was made?
- Why that decision?

### 5. Common Scenarios
- **CEO salary** in employee dataset = VALID (legitimate role difference)
- **Temperature = -500°C** = ERROR (physically impossible)
- **Response time = 10 seconds** when typical = 0.5s = INVESTIGATE (could be real outage)
- **Single $1M house** with rest $50K = VALID (could be luxury property)

## Detection Method Comparison
| Method | Best For | Pros | Cons |
|--------|----------|------|------|
| IQR | Any distribution | Robust, resistant | Lagging on extreme outliers |
| Threshold | Known bounds | Simple, domain-based | Requires prior knowledge |
| Std Dev | Normal distributions | Standard statistical | Affected by extreme values |
| Visual | Quick screening | Intuitive, fast | Subjective, less precise |

## Common Use Cases
- Financial fraud detection
- Sensor malfunction identification
- Data quality assurance
- Extreme value analysis
- Performance analysis across groups

## Best Practices
✓ Use visual inspection first (fast, intuitive)
✓ Confirm with multiple detection methods
✓ Consider domain context always
✓ Investigate before deciding to keep/remove
✓ Document all outlier decisions
✓ Never remove outliers blindly

## Mistakes to Avoid
❌ Not visualizing before applying rules
❌ Automatically removing all outliers
❌ Using only one detection method
❌ Ignoring domain context
❌ Treating all outliers as bad/errors
❌ Hiding outlier decisions from analysis

## Skills Mastered
- Visual detection using boxplots, histograms, scatter plots
- IQR statistical rule implementation
- Threshold-based detection
- Standard deviation outlier flagging
- Multi-method outlier confirmation
- Investigation and interpretation framework
- Professional documentation of outlier decisions
