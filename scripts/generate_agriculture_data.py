#!/usr/bin/env python3
import csv
import random
from datetime import datetime, timedelta
import math

print("Generating Agricultural Climate Dataset (1000+ rows)...")
print("="*70)

# Set seed for reproducibility
random.seed(42)

# Date range: 3 years of daily data
start_date = datetime(2021, 1, 1)
crops = ['Wheat', 'Corn', 'Soybeans', 'Rice', 'Barley']
regions = ['North Valley', 'South Plains', 'East Coast', 'West Ridge', 'Central Basin']

# Generate CSV data
rows = []
rows.append('Date,Region,Crop,Temperature_C,Rainfall_mm,Humidity_percent,Soil_Moisture_percent,Yield_kg_per_hectare,Market_Price_per_kg,Market_Demand_kg,Drought_Risk,Flood_Risk,Frost_Risk,Heat_Stress_Risk,Disease_Risk')

record_count = 0
for day_offset in range(1095):  # 3 years
    date = start_date + timedelta(days=day_offset)
    day_of_year = date.timetuple().tm_yday
    
    for region in regions:
        for crop in crops:
            # Weather patterns with seasonality
            seasonal_temp = 20 + 15 * math.sin(2 * math.pi * day_of_year / 365)
            seasonal_rain = 50 + 30 * math.sin(2 * math.pi * (day_of_year - 90) / 365)
            
            # Add noise
            temperature = seasonal_temp + random.gauss(0, 5)
            rainfall = max(0, seasonal_rain + random.gauss(0, 15))
            humidity = 60 + random.gauss(0, 10)
            soil_moisture = 50 + random.gauss(0, 15)
            
            # Crop yield
            base_yield = {'Wheat': 4000, 'Corn': 9000, 'Soybeans': 2500, 'Rice': 6000, 'Barley': 3500}
            weather_factor = (temperature - 20) * 10 + rainfall * 2 + soil_moisture * 5
            yield_val = max(100, base_yield[crop] + weather_factor + random.gauss(0, 200))
            
            # Market price
            base_price = {'Wheat': 250, 'Corn': 200, 'Soybeans': 400, 'Rice': 350, 'Barley': 220}
            price = max(50, base_price[crop] * (1 - yield_val / 10000) + random.gauss(0, 20))
            
            # Demand
            base_demand = {'Wheat': 50000, 'Corn': 80000, 'Soybeans': 30000, 'Rice': 60000, 'Barley': 25000}
            demand = max(1000, base_demand[crop] * (1 + 0.3 * math.sin(2 * math.pi * day_of_year / 365)) + random.gauss(0, 5000))
            
            # Risk indicators
            drought_risk = 1 if rainfall < 30 else (0.5 if rainfall < 50 else 0)
            flood_risk = 1 if rainfall > 150 else (0.5 if rainfall > 100 else 0)
            frost_risk = 1 if temperature < 0 else 0
            heat_stress = 1 if temperature > 35 else (0.5 if temperature > 30 else 0)
            disease_risk = humidity * 0.8 / 100
            
            row = f"{date.date()},{region},{crop},{temperature:.2f},{rainfall:.2f},{humidity:.2f},{soil_moisture:.2f},{yield_val:.2f},{price:.2f},{demand:.2f},{drought_risk:.2f},{flood_risk:.2f},{frost_risk:.2f},{heat_stress:.2f},{disease_risk:.2f}"
            rows.append(row)
            record_count += 1

# Write to CSV
with open('agriculture_climate_data.csv', 'w', newline='') as f:
    f.write('\n'.join(rows))

print(f"\n✓ Dataset created with {record_count} rows")
print(f"✓ Time period: 2021-01-01 to 2023-12-31")
print(f"✓ Regions: {len(regions)}")
print(f"✓ Crops: {len(crops)}")
print(f"✓ File saved: agriculture_climate_data.csv")
print(f"\nFirst 5 rows preview:")
for i, row in enumerate(rows[:6]):
    print(f"  {row}")
