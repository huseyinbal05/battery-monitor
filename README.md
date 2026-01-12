# Battery Monitor App

A lightweight, efficient macOS menu bar application that monitors your battery status and provides detailed statistics.

## Live Demo
![Application Demo](https://raw.githubusercontent.com/huseyinbal05/battery-monitor/main/demo.png) *(Note: Add a screenshot if you have one, otherwise remove this line)*

## Features

- **Menu Bar Integration**: Displays current battery percentage and charging status in your menu bar.
- **Detailed Statistics**:
  - **Hardware %**: The actual hardware battery percentage.
  - **Health %**: Battery health indicator.
  - **Cycle Count**: Total charge cycles.
  - **Temperature**: Battery temperature.
  - **Electrical Stats**: Voltage, Amperage, and Power.
  - **Capacity**: Current, Max, and Design capacity in mAh.
- **Compact UI**: Grouped statistics for a clean look.
- **Optimized**: Caches detailed stats to save energy.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/huseyinbal05/battery-monitor.git
    cd battery-monitor
    ```

2.  Install dependencies:
    ```bash
    uv sync
    ```

## Usage

1. Double-click the `run.command` file in the folder.
   
   OR

   Run from terminal:
   ```bash
   uv run src/app.py
   ```
2. The battery monitor will appear in your menu bar.

## License

MIT License - see [LICENSE](LICENSE).
