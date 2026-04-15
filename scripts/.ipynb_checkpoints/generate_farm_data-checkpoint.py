import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

np.random.seed(42)
print("Generating Agricultural Climate Dataset (1050 rows)...")

start_date = datetime(2021, 1, 1)
dates = [start_date + timedelta(days=x) for x in range(210)]  # 210 days x 5 crops x 1 region
crops = ['Wheat', 'Corn', 'Soybeans', 'Rice', 'Barley']

data = []
for date in dates:
    for crop in crops:
        day_of_year = date.timetuple().tm_yday
        seasonal_temp = 20 + 15 * np.sin(2 * np.pi * day_of_year / 365)
        seasonal_rain = 50 + 30 * np.sin(2 * np.pi * (day_of_year - 90) / 365)
        
        temperature = seasonal_temp + np.random.normal(0, 5)
        rainfall = max(0, seasonal_rain + np.random.normal(0, 15))
        
        base_yield = {'Wheat': 4000, 'Corn': 9000, 'Soybeans': 2500, 'Rice': 6000, 'Barley': 3500}
        weather_factor = (temperature - 20) * 10 + rainfall * 2
        yield_kg_per_hectare = base_yield[crop] + weather_factor + np.random.normal(0, 200)
        yield_kg_per_hectare = max(100, yield_kg_per_hectare)
        
        base_price = {'Wheat': 250, 'Corn': 200, 'Soybeans': 400, 'Rice': 350, 'Barley': 220}
        price = base_price[crop] * (1 - yield_kg_per_hectare / 10000) + np.random.normal(0, 20)
        price = max(50, price)
        
        base_demand = {'Wheat': 50000, 'Corn': 80000, 'Soybeans': 30000, 'Rice': 60000, 'Barley': 25000}
        demand = base_demand[crop] * (1 + 0.3 * np.sin(2 * np.pi * day_of_year / 365)) + np.random.normal(0, 2000)
        demand = max(1000, demand)
        
        data.append({'Date': date, 'Crop': crop, 'Temp': temperature, 'Rain': rainfall, 
                     'Yield': yield_kg_per_hectare, 'Price': price, 'Demand': demand})

print(f"✓ Generated {len(data)} data points\n")

# ANALYSIS
temps = [d['Temp'] for d in data]
prices = [d['Price'] for d in data]
yields = [d['Yield'] for d in data]
demands = [d['Demand'] for d in data]

print("=" * 60)
print("AGRICULTURE & CLIMATE RISK ANALYSIS")
print("=" * 60)
print(f"\n📊 DATASET: {len(data)} observations across {len(set([d['Crop'] for d in data]))} crops")
print(f"🌡️  Temperature Range: {min(temps):.1f}°C to {max(temps):.1f}°C")
print(f"🌧️  Rainfall Range: {min([d['Rain'] for d in data]):.1f}mm to {max([d['Rain'] for d in data]):.1f}mm")
print(f"🌾 Yield Range: {min(yields):.0f} to {max(yields):.0f} kg/hectare")
print(f"💰 Price Range: ${min(prices):.0f} to ${max(prices):.0f} per kg")
print(f"📈 Demand Range: {min(demands):.0f} to {max(demands):.0f} kg")

# Calculate correlations
yield_temp_corr = np.corrcoef(temps, yields)[0, 1]
price_yield_corr = np.corrcoef(yields, prices)[0, 1]
demand_price_corr = np.corrcoef(demands, prices)[0, 1]

print(f"\n🔗 KEY CORRELATIONS:")
print(f"   Temperature ↔ Yield: {yield_temp_corr:.3f}")
print(f"   Yield ↔ Price: {price_yield_corr:.3f} (inverse relationship)")
print(f"   Demand ↔ Price: {demand_price_corr:.3f}")

# Risk analysis
drought_events = sum(1 for d in data if d['Rain'] < 30)
high_demand = sum(1 for d in data if d['Demand'] > np.mean(demands) + np.std(demands))

print(f"\n⚠️  CLIMATE RISKS DETECTED:")
print(f"   Drought events (rainfall < 30mm): {drought_events} cases ({100*drought_events/len(data):.1f}%)")
print(f"   High demand spikes: {high_demand} cases ({100*high_demand/len(data):.1f}%)")

# Create visualizations
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Agricultural Climate & Market Analysis\n1050 Dataset Points', fontsize=16, fontweight='bold')

# 1. Temperature vs Yield
axes[0, 0].scatter(temps, yields, alpha=0.6, c='red', s=30)
z = np.polyfit(temps, yields, 1)
p = np.poly1d(z)
axes[0, 0].plot(sorted(temps), p(sorted(temps)), "b--", lw=2)
axes[0, 0].set_xlabel('Temperature (°C)')
axes[0, 0].set_ylabel('Yield (kg/hectare)')
axes[0, 0].set_title(f'Temperature Impact on Yield\nr={yield_temp_corr:.3f}')
axes[0, 0].grid(alpha=0.3)

# 2. Rainfall distribution
axes[0, 1].hist([d['Rain'] for d in data], bins=30, color='blue', alpha=0.7, edgecolor='black')
axes[0, 1].axvline(30, color='red', linestyle='--', linewidth=2, label='Drought threshold')
axes[0, 1].set_xlabel('Rainfall (mm)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Rainfall Distribution\n(Drought Risk: <30mm)')
axes[0, 1].legend()
axes[0, 1].grid(alpha=0.3)

# 3. Price vs Yield (inverse relationship)
axes[0, 2].scatter(yields, prices, alpha=0.6, c='green', s=30)
z2 = np.polyfit(yields, prices, 1)
p2 = np.poly1d(z2)
axes[0, 2].plot(sorted(yields), p2(sorted(yields)), "b--", lw=2)
axes[0, 2].set_xlabel('Yield (kg/hectare)')
axes[0, 2].set_ylabel('Market Price ($/kg)')
axes[0, 2].set_title(f'Yield-Price Inverse Relationship\nr={price_yield_corr:.3f}')
axes[0, 2].grid(alpha=0.3)

# 4. Crop-wise average yield
crop_yields = {}
for d in data:
    if d['Crop'] not in crop_yields:
        crop_yields[d['Crop']] = []
    crop_yields[d['Crop']].append(d['Yield'])
avg_yields = {c: np.mean(v) for c, v in crop_yields.items()}
colors_crop = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#FFD93D']
axes[1, 0].bar(avg_yields.keys(), avg_yields.values(), color=colors_crop, edgecolor='black')
axes[1, 0].set_ylabel('Average Yield (kg/hectare)')
axes[1, 0].set_title('Crop Performance Comparison')
axes[1, 0].tick_params(axis='x', rotation=45)
axes[1, 0].grid(alpha=0.3, axis='y')

# 5. Demand volatility
axes[1, 1].plot(demands, marker='o', linestyle='-', alpha=0.7, linewidth=1, markersize=3)
mean_demand = np.mean(demands)
axes[1, 1].axhline(mean_demand, color='r', linestyle='--', label='Mean')
axes[1, 1].axhline(mean_demand + np.std(demands), color='orange', linestyle='--', label='High demand')
axes[1, 1].set_xlabel('Time (days)')
axes[1, 1].set_ylabel('Demand (kg)')
axes[1, 1].set_title('Market Demand Over Time\n(Identifies demand spikes)')
axes[1, 1].legend()
axes[1, 1].grid(alpha=0.3)

# 6. Price stability
price_changes = [abs(prices[i] - prices[i-1]) for i in range(1, len(prices))]
axes[1, 2].hist(price_changes, bins=30, color='purple', alpha=0.7, edgecolor='black')
axes[1, 2].set_xlabel('Daily Price Change ($/kg)')
axes[1, 2].set_ylabel('Frequency')
axes[1, 2].set_title('Market Price Volatility\n(Shows pricing risk)')
axes[1, 2].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('agriculture_analysis.png', dpi=100, bbox_inches='tight')
print(f"\n✅ Analysis saved to: agriculture_analysis.png")
plt.show()

print("\n" + "=" * 60)
print("💡 KEY INSIGHTS FOR FARMERS:")
print("=" * 60)
print(f"1. Temperature management is critical - {yield_temp_corr:.1%} correlation with yield")
print(f"2. Drought risk: Monitor {drought_events} high-risk days annually")
print(f"3. Price volatility: Avg daily change ${np.mean(price_changes):.2f}/kg")
print(f"4. Demand peaks: {high_demand} high-demand periods - prime selling opportunity")
print("=" * 60)
