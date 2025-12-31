# Battery Monitor App

A lightweight, efficient macOS menu bar application that monitors your battery status and provides detailed statistics.

## Features

- **Menu Bar Integration**: Displays current battery percentage and charging status in your menu bar.
- **Detailed Statistics**:
  - **Hardware %**: The actual hardware battery percentage (often slightly different from the OS display).
  - **Health %**: Battery health based on nominal vs design capacity.
  - **Cycle Count**: Number of charge cycles.
  - **Temperature**: Current battery temperature.
  - **Electrical Stats**: Real-time Voltage, Amperage, and Power usage.
  - **Capacity**: Current, Max, and Design capacity in mAh.
- **Compact UI**: Optimized layout to show maximum information in minimum space.
- **Optimized Performance**: Intelligent caching mechanism (updates detailed stats every 60s) to minimize system resource usage.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/huseyinbal05/battery-monitor.git
    cd battery-monitor
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the application:
```bash
python3 src/app.py
```

## Build from Source

To create a standalone macOS application:

```bash
python3 setup.py py2app
```

The application will be available in `dist/Battery Monitor.app`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
