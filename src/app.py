import rumps
import psutil
import subprocess
import plistlib
import time

class BatteryApp(rumps.App):
    def __init__(self):
        super(BatteryApp, self).__init__("Battery")
        self.menu = ["Details", "Stats1", "Stats2", "Stats3", "Stats4"]
        self.last_detailed_update = 0
        self.cached_details = None
        self.update_battery_status(None)

    def get_detailed_battery_info(self):
        # Optimization: Cache detailed stats for 60 seconds
        if self.cached_details and (time.time() - self.last_detailed_update < 60):
            return self.cached_details

        try:
            cmd = ["ioreg", "-a", "-r", "-c", "AppleSmartBattery"]
            output = subprocess.check_output(cmd)
            data = plistlib.loads(output)
            if data:
                battery_data = data[0]
                
                # Hardware Cap
                current_raw = battery_data.get("AppleRawCurrentCapacity")
                max_raw = battery_data.get("AppleRawMaxCapacity")
                hardware_percent = (current_raw / max_raw * 100) if max_raw else 0
                
                # Health
                design_cap = battery_data.get("DesignCapacity")
                # NominalChargeCapacity might be better for health calculation against DesignCapacity
                # But sometimes MaxCapacity is used. Let's use AppleRawMaxCapacity vs DesignCapacity for health check if available
                # Or just display raw MaxCapacity.
                # Common health metric: NominalChargeCapacity / DesignCapacity
                nominal_cap = battery_data.get("NominalChargeCapacity")
                health_percent = (nominal_cap / design_cap * 100) if design_cap else 0

                cycles = battery_data.get("CycleCount")
                
                # Temperature is usually in centikelvin (decikelvin?) or just raw. 
                # Checking sample output: "Temperature" = 3023. 
                # 3023 / 100 = 30.23 C. Sounds reasonable.
                # Temperature
                temp_raw = battery_data.get("Temperature", 0)
                temp_c = temp_raw / 100.0
                
                # Electrical stats
                voltage_mv = battery_data.get("Voltage", 0)
                voltage_v = voltage_mv / 1000.0
                
                amperage_ma = battery_data.get("InstantAmperage", 0)
                
                power_w = (voltage_v * amperage_ma) / 1000.0
                
                # Capacity
                current_capacity = current_raw
                max_capacity = max_raw
                design_capacity = design_cap

                self.cached_details = {
                    "hardware_percent": hardware_percent,
                    "health_percent": health_percent,
                    "cycles": cycles,
                    "temp_c": temp_c,
                    "voltage_v": voltage_v,
                    "amperage_ma": amperage_ma,
                    "power_w": power_w,
                    "current_capacity": current_capacity,
                    "max_capacity": max_capacity,
                    "design_capacity": design_capacity
                }
                self.last_detailed_update = time.time()
                return self.cached_details
            return None
        except Exception as e:
            print(f"Error fetching detailed stats: {e}")
            return None

    @rumps.timer(5)
    def update_battery_status(self, _):
        battery = psutil.sensors_battery()
        if battery:
            percent = int(battery.percent)
            plugged = battery.power_plugged
            status_icon = "⚡️" if plugged else "🔋"
            
            self.title = f"{status_icon} {percent}%"
            
            # Update menu details
            time_left = battery.secsleft
            if time_left == psutil.POWER_TIME_UNLIMITED:
                time_str = "Unlimited"
            elif time_left == psutil.POWER_TIME_UNKNOWN:
                time_str = "Unknown"
            else:
                hours = time_left // 3600
                minutes = (time_left % 3600) // 60
                time_str = f"{hours}h {minutes}m"
            
            self.menu["Details"].title = f"Remaining: {time_str}"
            
            # Detailed stats
            details = self.get_detailed_battery_info()
            if details:
                self.menu["Stats1"].title = f"Hardware: {details['hardware_percent']:.1f}% | Health: {details['health_percent']:.1f}%"
                self.menu["Stats2"].title = f"Cycles: {details['cycles']} | Temp: {details['temp_c']:.1f}°C"
                self.menu["Stats3"].title = f"V: {details['voltage_v']:.2f}V | A: {details['amperage_ma']}mA | P: {details['power_w']:.1f}W"
                self.menu["Stats4"].title = f"Cap: {details['current_capacity']}/{details['max_capacity']} mAh (Design: {details['design_capacity']})"
        else:
            self.title = "No Battery"

if __name__ == "__main__":
    BatteryApp().run()
