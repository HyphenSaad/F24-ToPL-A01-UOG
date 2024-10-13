# Sensor Data Parsing and Analysis

## Theory of Programming Languages (ToPL) - Assignment # 1

**Name:** Saad Mansoor  
**Roll Number:** 24015919-003  
**Program:** MS Computer Science  
**University:** University of Gujrat, Hafiz Hayat Campus (UOG-HH)  
**Department:** Department of Computer Science  
**Submission Date:** 12 October, 2024

## Objective

To apply fundamental research programming concepts to parse and analyze sensor data from a mobile device log file using Python.

## Task 1: Sensor Data Parsing and Separation

### Solution

For Task 1, I have implemented a comprehensive `SensorDataParser` class that handles the parsing and exporting of sensor data from a mobile device log file. Here's an overview of the solution:

1. **Class Structure:** The `SensorDataParser` class is designed to handle various sensor types, including Accelerometer, Gyroscope, Magnetometer, Light, WIFI, and Pressure sensors.

2. **Sensor Classes:** Individual sensor classes (e.g., `AccelerometerSensor`, `GyroscopeSensor`) are implemented to represent each sensor type. These classes handle sensor-specific data and computations.

3. **Parsing Logic:** The `parse_sensor_data` method reads the log file line by line, skipping header lines, and creates appropriate sensor objects based on the data in each line.

4. **Data Separation:** The parsed data is separated into individual sensor objects, which are stored in a list (`sensors_data`).

5. **Computations:** Sensor classes include methods to perform computations on raw data, such as calculating averages, standard deviations, or correlations. These can be included in the export by setting the `include_calculated` flag.

6. **Data Export:** The `export_sensor_data` method exports the parsed and processed data to CSV files, either for a single specified sensor or for all sensors.

Key features of the implementation:

- Robust error handling and input validation
- Flexible parsing for multiple sensor types
- Option to include calculated values in the export
- Timestamp-based file naming for easy tracking
- Comprehensive logging of the parsing and export process

### How to Run Task 1

To run the sensor data parser:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `parser003.py`.
3. Run the script using one of the following commands:

   - To parse all sensors' data:

     ```
     python parser003.py <source_file> -all
     ```

   - To parse data for a specific sensor:

     ```
     python parser003.py <source_file> -o <sensor_name>
     ```

   - To include calculated values:
     ```
     python parser003.py <source_file> -all -c
     ```

   Replace `<source_file>` with the path to your input file and `<sensor_name>` with the desired sensor (e.g., ACCE, GYRO, etc.).

## Task 2: Sensor Data Analysis and Visualization

### Solution

For Task 2, I have implemented a `SensorDataAnalyzer` class that focuses on analyzing and visualizing the data parsed in Task 1. Here's an overview of the solution:

1. **Analyzer Structure:** The `SensorDataAnalyzer` class is designed to work with various sensor types, including Accelerometer, Gyroscope, Magnetometer, Pressure, Light, Orientation, and GNSS.

2. **Sensor-Specific Analyzers:** Individual analyzer classes (e.g., `AccelerometerAnalyzer`, `GyroscopeAnalyzer`) are implemented for each sensor type to handle sensor-specific analysis and visualization.

3. **Analysis Process:** The `analyze` method orchestrates the entire analysis process, including input validation and running the appropriate sensor-specific analyzer.

4. **Visualization:** Each sensor-specific analyzer includes methods to create informative graphs and charts using matplotlib or seaborn, illustrating patterns, trends, or anomalies in the data.

5. **Statistical Analysis:** The analyzers perform statistical computations to extract meaningful insights from the sensor data.

Key features of the implementation:

- Modular design allowing easy addition of new sensor analyzers
- Comprehensive error handling and input validation
- Flexible analysis options for different sensor types
- Generation of insightful visualizations

### How to Run Task 2

To run the sensor data analyzer:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `analyzer003.py`.
3. Run the script using the following command:

   ```
   python analyzer003.py <source_file> <sensor_name>
   ```

   Replace `<source_file>` with the path to your input CSV file (generated from Task 1) and `<sensor_name>` with the desired sensor to analyze (e.g., ACCE, GYRO, etc.).
