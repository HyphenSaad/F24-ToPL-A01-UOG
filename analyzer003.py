import os
import argparse
from typing import List, Optional
from datetime import datetime

from sensors.Accelerometer.AccelerometerAnalyzer import AccelerometerAnalyzer
from sensors.GNSS_GPS.GNSS_GPS_Analyzer import GNSS_GPS_Analyzer
from sensors.Gyroscope.GyroscopeAnalyzer import GyroscopeAnalyzer
from sensors.Light.LightAnalyzer import LightAnalyzer
from sensors.Magnetometer.MagnetometerAnalyzer import MagnetometerAnalyzer
from sensors.Orientation.OrientationAnalyzer import OrientationAnalyzer
from sensors.Pressure.PressureAnalyzer import PressureAnalyzer

class SensorDataAnalyzer:
    """
    A class to handle parsing and analyzing of sensor data.

    This class encapsulates all the functionality related to validating input,
    and running analysis on sensor data from a source CSV file.
    """

    def __init__(self):
        """
        Initialize the SensorDataAnalyzer with necessary constants and mappings.
        """
        self.SENSORS = ['ACCE', 'GYRO', 'MAGN', 'PRES', 'LIGH', 'AHRS', 'GNSS']

        self.sensor_analyzer_map = {
            'ACCE': AccelerometerAnalyzer,
            'GYRO': GyroscopeAnalyzer,
            'MAGN': MagnetometerAnalyzer,
            'PRES': PressureAnalyzer,
            'LIGH': LightAnalyzer,
            'AHRS': OrientationAnalyzer,
            'GNSS': GNSS_GPS_Analyzer,
        }

    def analyze(self, file_source: str, target_sensor: Optional[str] = None) -> None:
        """
        Validate input and run analysis on sensor data from a source file.

        This function orchestrates the entire process of validating input and
        running analysis on sensor data from a CSV file. It follows these main steps:
        1. Validate input parameters
        2. Run analysis on the sensor data from the source file

        Args:
            file_source (str): Path to the source CSV file containing sensor data.
            target_sensor (str, optional): Name of the specific sensor to analyze data for.

        Raises:
            FileNotFoundError: If the source file does not exist.
            ValueError: If the source file is not a .csv file or if the target sensor is invalid.
        """
        self.validate_input_parameters(file_source, target_sensor)
        
        self.sensor_analyzer_map[target_sensor](file_source).run_analysis()

    def validate_input_parameters(self, file_source: str, target_sensor: Optional[str]) -> None:
        """
        Validate the input parameters for the analyzer function.

        This function performs several checks:
        1. Ensures the source file has a .csv extension
        2. Verifies that the source file exists
        3. If a target sensor is specified, ensures it's a valid sensor type

        Args:
            file_source (str): Path to the source file containing sensor data.
            target_sensor (str, optional): Name of the specific sensor to analyze data for.

        Raises:
            ValueError: If any of the input parameters are invalid.
            FileNotFoundError: If the source file does not exist.
        """
        if not file_source.endswith('.csv'):
            raise ValueError('Invalid File Type! Source File Must Be .csv!')
        
        if not os.path.exists(file_source):
            raise FileNotFoundError('Source File Not Found!')
        
        if target_sensor is not None and target_sensor not in self.SENSORS:
            raise ValueError(f'Invalid Sensor! Available Sensors: {", ".join(self.SENSORS)}')

def print_help() -> None:
    """
    Print a help message describing the usage of the script.

    This function displays information about how to use the script,
    including the correct syntax and available options.
    """
    print('Usage:')
    print('python analyzer003.py <source_file> <sensor_name>')
    print('\nOptions:')
    print('-h, --help\t\tShow this help message and exit')

def print_intro() -> None:
    """
    Print an introductory message for the script.

    This function displays a formatted introduction message that includes
    the script's purpose and developer information.
    """
    ROW_WIDTH = 62
    print('=' * ROW_WIDTH)
    print('003 - SENSOR DATA ANALYZER'.center(ROW_WIDTH))
    print('-' * ROW_WIDTH)
    print('To Analyze Data from CSV Files'.center(ROW_WIDTH))
    print('-' * ROW_WIDTH)
    print('Developed By: Saad Mansoor (24015919-003)'.center(ROW_WIDTH))
    print('Programming Languages - Assignment 01 - Task 02'.center(ROW_WIDTH))
    print('=' * ROW_WIDTH)
    print()

def main() -> None:
    """
    Main function to handle command-line arguments and execute the analyzer.

    This function processes the command-line arguments, validates them,
    and calls the appropriate functions based on the provided options.
    It also handles any exceptions that might occur during execution.
    """
    arg_parser = argparse.ArgumentParser(description='Sensor Data Analyzer', add_help=False)
    arg_parser.add_argument('source_file', nargs='?', help='Source CSV file containing sensor data')
    arg_parser.add_argument('sensor_name', nargs='?', help='Name of the sensor to analyze data for')
    arg_parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')

    args = arg_parser.parse_args()

    print_intro()

    if args.help:
        print_help()
        return

    if not args.source_file:
        print("Error: Source file is required.")
        print_help()
        return
    
    if not args.sensor_name:
        print("Error: Sensor name is required.")
        print_help()
        return
    
    try:
        analyzer = SensorDataAnalyzer()
        analyzer.analyze(args.source_file, args.sensor_name)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()