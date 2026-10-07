"""
Digital Twin Simulation Engine for Pavement Asset Management
Author: Syed Nafiz Reja Hasib
"""

import pandas as pd
import numpy as np
import json
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

class PavementAsset:
    """
    Represents a physical pavement segment in a 7D BIM environment.
    """
    def __init__(self, asset_id: str, mix_type: str, tsr_base: float, alpha: float, installation_date: str):
        self.asset_id = asset_id
        self.mix_type = mix_type
        self.tsr = tsr_base
        self.alpha = alpha  # Degradation coefficient (lower = higher resistance)
        self.installation_date = datetime.strptime(installation_date, '%Y-%m-%d')
        self.history = []

    def apply_climate_stress(self, months_elapsed: int, precip_mm: float, temp_c: float):
        """
        Calculates mechanical degradation based on environmental stress loads.
        """
        # Formulate climate stress factor
        stress_factor = (precip_mm * 0.001) * (temp_c / 25.0)
        
        # Calculate degradation
        degradation = self.alpha * stress_factor
        self.tsr = max(0.40, self.tsr - degradation)  # Floor value at 40% TSR
        
        # Log state for BIM telemetry
        current_date = self.installation_date + relativedelta(months=months_elapsed)
        self.history.append({
            'Asset_ID': self.asset_id,
            'Date': current_date.strftime('%Y-%m'),
            'Mix_Type': self.mix_type,
            'Precipitation_mm': round(precip_mm, 2),
            'Mean_Temp_C': round(temp_c, 2),
            'Current_TSR': round(self.tsr, 3),
            'Condition_State': 'Critical' if self.tsr < 0.60 else 'Stable'
        })

def run_lifecycle_simulation(duration_months: int = 60):
    """
    Executes an accelerated lifecycle simulation comparing conventional WMA 
    against Nano-Modified WMA under synthetic climatic loads.
    """
    print(f"Initializing {duration_months}-month Digital Twin Simulation...")
    
    # Initialize Pavement Assets based on SWPU baseline concepts
    standard_wma = PavementAsset(asset_id="SEG_1001", mix_type="Standard_WMA", tsr_base=0.72, alpha=0.045, installation_date="2026-08-01")
    nano_wma = PavementAsset(asset_id="SEG_1002", mix_type="Nano_WMA", tsr_base=0.88, alpha=0.015, installation_date="2026-08-01")
    
    # Generate Synthetic Climate Data (Seasonal variation)
    np.random.seed(42)
    months = np.arange(1, duration_months + 1)
    rainfall_data = np.random.normal(100, 30, duration_months) # Average 100mm per month
    temp_data = 20 + 15 * np.sin(np.pi * months / 6)           # Seasonal sine wave temperature curve
    
    # Apply time-step degradation
    for m, r, t in zip(months, rainfall_data, temp_data):
        precip = max(0, r)
        temp = max(1, t)
        standard_wma.apply_climate_stress(m, precip, temp)
        nano_wma.apply_climate_stress(m, precip, temp)
        
    # Aggregate telemetry data
    combined_history = standard_wma.history + nano_wma.history
    df_results = pd.DataFrame(combined_history)
    
    print("Simulation complete. Telemetry ready for BIM dashboard integration.")

if __name__ == "__main__":
    run_lifecycle_simulation()
