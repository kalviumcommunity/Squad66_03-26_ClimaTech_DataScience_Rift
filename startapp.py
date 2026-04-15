from flask import Flask, render_template, jsonify
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import base64
import json

app = Flask(__name__)

def generate_farm_data():
    """Generate 1050 agricultural climate data points"""
    np.random.seed(42)
    start_date = datetime(2021, 1, 1)
    dates = [start_date + timedelta(days=x) for x in range(210)]
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
            yield_kg = base_yield[crop] + weather_factor + np.random.normal(0, 200)
            yield_kg = max(100, yield_kg)
            
            base_price = {'Wheat': 250, 'Corn': 200, 'Soybeans': 400, 'Rice': 350, 'Barley': 220}
            price = base_price[crop] * (1 - yield_kg / 10000) + np.random.normal(0, 20)
            price = max(50, price)
            
            base_demand = {'Wheat': 50000, 'Corn': 80000, 'Soybeans': 30000, 'Rice': 60000, 'Barley': 25000}
            demand = base_demand[crop] * (1 + 0.3 * np.sin(2 * np.pi * day_of_year / 365)) + np.random.normal(0, 2000)
            demand = max(1000, demand)
            
            data.append({'Date': date, 'Crop': crop, 'Temp': temperature, 'Rain': rainfall, 
                         'Yield': yield_kg, 'Price': price, 'Demand': demand})
    
    return data

def create_chart(chart_type, data):
    """Create individual visualizations based on chart type"""
    temps = [d['Temp'] for d in data]
    prices = [d['Price'] for d in data]
    yields = [d['Yield'] for d in data]
    demands = [d['Demand'] for d in data]
    crops_list = [d['Crop'] for d in data]
    rains = [d['Rain'] for d in data]
    
    fig = plt.figure(figsize=(14, 8))
    
    if chart_type == 'overview':
        # 6-panel overview
        fig, axes = plt.subplots(2, 3, figsize=(16, 10))
        fig.suptitle('Agricultural Climate & Market Analysis - 1050 Dataset Points', fontsize=16, fontweight='bold')
        
        yield_temp_corr = np.corrcoef(temps, yields)[0, 1]
        price_yield_corr = np.corrcoef(yields, prices)[0, 1]
        
        axes[0, 0].scatter(temps, yields, alpha=0.6, c='red', s=30)
        z = np.polyfit(temps, yields, 1)
        p = np.poly1d(z)
        axes[0, 0].plot(sorted(temps), p(sorted(temps)), "b--", lw=2)
        axes[0, 0].set_xlabel('Temperature (°C)')
        axes[0, 0].set_ylabel('Yield (kg/hectare)')
        axes[0, 0].set_title(f'Temperature Impact on Yield\nr={yield_temp_corr:.3f}')
        axes[0, 0].grid(alpha=0.3)
        
        axes[0, 1].hist(rains, bins=30, color='blue', alpha=0.7, edgecolor='black')
        axes[0, 1].axvline(30, color='red', linestyle='--', linewidth=2, label='Drought threshold')
        axes[0, 1].set_xlabel('Rainfall (mm)')
        axes[0, 1].set_ylabel('Frequency')
        axes[0, 1].set_title('Rainfall Distribution\n(Drought Risk: <30mm)')
        axes[0, 1].legend()
        axes[0, 1].grid(alpha=0.3)
        
        axes[0, 2].scatter(yields, prices, alpha=0.6, c='green', s=30)
        z2 = np.polyfit(yields, prices, 1)
        p2 = np.poly1d(z2)
        axes[0, 2].plot(sorted(yields), p2(sorted(yields)), "b--", lw=2)
        axes[0, 2].set_xlabel('Yield (kg/hectare)')
        axes[0, 2].set_ylabel('Market Price ($/kg)')
        axes[0, 2].set_title(f'Yield-Price Inverse Relationship\nr={price_yield_corr:.3f}')
        axes[0, 2].grid(alpha=0.3)
        
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
        
        axes[1, 1].plot(demands, marker='o', linestyle='-', alpha=0.7, linewidth=1, markersize=3)
        mean_demand = np.mean(demands)
        axes[1, 1].axhline(mean_demand, color='r', linestyle='--', label='Mean')
        axes[1, 1].axhline(mean_demand + np.std(demands), color='orange', linestyle='--', label='High demand')
        axes[1, 1].set_xlabel('Time (days)')
        axes[1, 1].set_ylabel('Demand (kg)')
        axes[1, 1].set_title('Market Demand Over Time')
        axes[1, 1].legend()
        axes[1, 1].grid(alpha=0.3)
        
        price_changes = [abs(prices[i] - prices[i-1]) for i in range(1, len(prices))]
        axes[1, 2].hist(price_changes, bins=30, color='purple', alpha=0.7, edgecolor='black')
        axes[1, 2].set_xlabel('Daily Price Change ($/kg)')
        axes[1, 2].set_ylabel('Frequency')
        axes[1, 2].set_title('Market Price Volatility')
        axes[1, 2].grid(alpha=0.3)
        
    elif chart_type == 'climate':
        ax = fig.add_subplot(111)
        ax.scatter(temps, rains, alpha=0.6, c='purple', s=50, edgecolors='black')
        ax.set_xlabel('Temperature (°C)', fontsize=12)
        ax.set_ylabel('Rainfall (mm)', fontsize=12)
        ax.set_title('Climate Conditions: Temperature vs Rainfall', fontsize=14, fontweight='bold')
        ax.grid(alpha=0.3)
        
    elif chart_type == 'market':
        ax = fig.add_subplot(111)
        ax.scatter(demands, prices, alpha=0.6, c='orange', s=50, edgecolors='black')
        z = np.polyfit(demands, prices, 1)
        p = np.poly1d(z)
        ax.plot(sorted(demands), p(sorted(demands)), "r--", lw=2, label='Trend')
        ax.set_xlabel('Market Demand (kg)', fontsize=12)
        ax.set_ylabel('Price ($/kg)', fontsize=12)
        ax.set_title('Market Dynamics: Demand vs Price', fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(alpha=0.3)
        
    elif chart_type == 'crops':
        crop_avgs = {}
        crop_max = {}
        crop_min = {}
        for d in data:
            if d['Crop'] not in crop_avgs:
                crop_avgs[d['Crop']] = []
                crop_max[d['Crop']] = d['Yield']
                crop_min[d['Crop']] = d['Yield']
            crop_avgs[d['Crop']].append(d['Yield'])
            crop_max[d['Crop']] = max(crop_max[d['Crop']], d['Yield'])
            crop_min[d['Crop']] = min(crop_min[d['Crop']], d['Yield'])
        
        ax = fig.add_subplot(111)
        crops = list(crop_avgs.keys())
        avgs = [np.mean(crop_avgs[c]) for c in crops]
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#FFD93D']
        bars = ax.bar(crops, avgs, color=colors, edgecolor='black', linewidth=2)
        ax.set_ylabel('Average Yield (kg/hectare)', fontsize=12)
        ax.set_title('Crop Performance Analysis', fontsize=14, fontweight='bold')
        ax.grid(alpha=0.3, axis='y')
        
    elif chart_type == 'risk':
        ax = fig.add_subplot(111)
        drought_days = sum(1 for r in rains if r < 30)
        low_yield_days = sum(1 for y in yields if y < np.mean(yields) - np.std(yields))
        high_price_days = sum(1 for p in prices if p > np.mean(prices) + np.std(prices))
        
        risks = ['Drought\nEvents', 'Low Yield\nDays', 'Price\nSpikes']
        counts = [drought_days, low_yield_days, high_price_days]
        colors = ['#ef4444', '#f97316', '#eab308']
        bars = ax.bar(risks, counts, color=colors, edgecolor='black', linewidth=2)
        ax.set_ylabel('Frequency (days)', fontsize=12)
        ax.set_title('Risk Assessment Dashboard', fontsize=14, fontweight='bold')
        ax.grid(alpha=0.3, axis='y')
        
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(count)}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    plt.close()
    
    return img_base64

def create_visualizations(data):
    """Create default overview visualization"""
    return create_chart('overview', data)

def calculate_metrics(data):
    """Calculate key metrics"""
    temps = [d['Temp'] for d in data]
    prices = [d['Price'] for d in data]
    yields = [d['Yield'] for d in data]
    demands = [d['Demand'] for d in data]
    rains = [d['Rain'] for d in data]
    
    yield_temp_corr = np.corrcoef(temps, yields)[0, 1]
    price_yield_corr = np.corrcoef(yields, prices)[0, 1]
    demand_price_corr = np.corrcoef(demands, prices)[0, 1]
    
    drought_events = sum(1 for r in rains if r < 30)
    high_demand = sum(1 for d in demands if d > np.mean(demands) + np.std(demands))
    
    crop_yields = {}
    for d in data:
        if d['Crop'] not in crop_yields:
            crop_yields[d['Crop']] = []
        crop_yields[d['Crop']].append(d['Yield'])
    
    metrics = {
        'total_observations': len(data),
        'crops': len(set([d['Crop'] for d in data])),
        'temp_range': f"{min(temps):.1f}°C to {max(temps):.1f}°C",
        'rainfall_range': f"{min(rains):.1f}mm to {max(rains):.1f}mm",
        'yield_range': f"{min(yields):.0f} to {max(yields):.0f} kg/ha",
        'price_range': f"${min(prices):.0f} to ${max(prices):.0f}/kg",
        'demand_range': f"{min(demands):.0f} to {max(demands):.0f} kg",
        'temp_yield_corr': f"{yield_temp_corr:.3f}",
        'yield_price_corr': f"{price_yield_corr:.3f}",
        'demand_price_corr': f"{demand_price_corr:.3f}",
        'drought_events': f"{drought_events} ({100*drought_events/len(data):.1f}%)",
        'high_demand_spikes': f"{high_demand} ({100*high_demand/len(data):.1f}%)",
        'best_crop': max(crop_yields.items(), key=lambda x: np.mean(x[1]))[0],
        'best_crop_yield': f"{max([np.mean(v) for v in crop_yields.values()]):.0f} kg/ha"
    }
    
    return metrics

@app.route('/')
def index():
    data = generate_farm_data()
    metrics = calculate_metrics(data)
    chart_img = create_visualizations(data)
    return render_template('index.html', metrics=metrics, chart_img=chart_img)

@app.route('/api/chart/<chart_type>')
def api_chart(chart_type):
    data = generate_farm_data()
    if chart_type not in ['overview', 'climate', 'market', 'crops', 'risk']:
        chart_type = 'overview'
    chart_img = create_chart(chart_type, data)
    return jsonify({'chart': chart_img, 'type': chart_type})

@app.route('/api/data')
def api_data():
    data = generate_farm_data()
    metrics = calculate_metrics(data)
    return jsonify(metrics)

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚜 RIFT - Agricultural Intelligence Dashboard")
    print("="*70)
    print("\n📊 Starting Flask server...")
    print("🌐 Open browser: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop\n")
    app.run(debug=True, port=5000)
