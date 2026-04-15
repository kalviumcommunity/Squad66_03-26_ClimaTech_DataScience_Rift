# Milestone 11: Visualizing Trends Over Time Using Line Plots

## Overview
Line plots are essential for analyzing how data changes over time. This milestone teaches you to create time-series visualizations, identify trends, spot anomalies, and interpret temporal patterns in your data.

## Key Concepts Covered

### 1. Understanding Time-Based Data
- **Time is a dimension**: Order matters critically
- **Regular vs irregular intervals**: Daily, monthly, or event-based timestamps
- **Time series characteristics**:
  - **Trend**: Long-term upward/downward movement
  - **Seasonality**: Repeating patterns (weekly, monthly, yearly)
  - **Noise**: Random fluctuations
  - **Anomalies**: Unusual spikes or drops

### 2. Creating Line Plots
```python
# Basic line plot
df.plot(x='Date', y='Value')

# With markers and styling
plt.plot(df['Date'], df['Value'], marker='o', linewidth=2)

# Multiple time series
plt.plot(df['Date'], df['Sales'], label='Sales')
plt.plot(df['Date'], df['Revenue'], label='Revenue')
plt.legend()

# Area fill under line
ax.fill_between(df['Date'], df['Value'], alpha=0.2)
```

### 3. Identifying Trends
- **Upward trend**: Line goes UP (growth, improvement, increasing demand)
- **Downward trend**: Line goes DOWN (decline, deterioration, loss)
- **Stable/Flat trend**: Line stays LEVEL (steady state, no change)
- **Cyclical pattern**: Repeating ups and downs (seasonality)

### 4. Spotting Anomalies
- **Spikes**: Sudden sharp increases
- **Drops**: Sudden sharp decreases
- **Plateaus**: Unexpected flat periods
- **Volatility**: Rapid fluctuations
- Questions to ask: Is this real? Data error? Special event?

### 5. Time Series Analysis Steps
1. **Sort by time** (CRITICAL: Always sort first!)
2. **Create line plot** to visualize progression
3. **Identify patterns** (trend, seasonality, noise)
4. **Spot anomalies** (spikes, drops, unusual changes)
5. **Compare quarters/periods** to see progress

## Common Use Cases
- Stock price movements over months/years
- Website traffic over time
- Sales revenue by month
- Customer acquisition growth
- System performance metrics over hours/days
- Temperature changes throughout the year

## Best Practices
✓ Always sort data by time before plotting
✓ Label x-axis as Date/Time clearly
✓ Use clear y-axis labeling with units
✓ Add grid lines for easier reading
✓ Combine with other metrics to understand context
✓ Distinguish long-term trends from short-term noise

## Mistakes to Avoid
❌ Not sorting by time (line will cross itself)
❌ Reacting to noise instead of trend
❌ Missing seasonal patterns
❌ Drawing conclusions from too little data
❌ Confusing correlation with causation when anomalies appear

## Skills Mastered
- Creating time-based visualizations
- Sorting data chronologically
- Identifying upward, downward, and stable trends
- Recognizing seasonality and cyclical patterns
- Detecting and investigating anomalies
- Comparing multiple time series
- Understanding context of temporal changes
