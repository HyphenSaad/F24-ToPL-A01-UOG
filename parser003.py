import os
import argparse
from typing import List, Optional
from datetime import datetime

from sensors.Accelerometer import AccelerometerSensor
from sensors.BLE4 import BLE4Sensor
from sensors.Bluetooth import BluetoothSensor
from sensors.GNSS_GPS import GNSS_GPS_Sensor
from sensors.Gyroscope import GyroscopeSensor
from sensors.Humidity import HumiditySensor
from sensors.IMU_LPMS_B import IMU_LPMS_B_Sensor
from sensors.IMU_XSens import IMU_XSensSensor
from sensors.Light import LightSensor
from sensors.Magnetometer import MagnetometerSensor
from sensors.Orientation import OrientationSensor
from sensors.POSI import POSI_Sensor
from sensors.Pressure import PressureSensor
from sensors.Proximity import ProximitySensor
from sensors.RFID_Reader import RFID_ReaderSensor
from sensors.Sound import SoundSensor
from sensors.Temperature import TemperatureSensor
from sensors.Wifi import WifiSensor

class SensorDataParser:
    """
    A class to handle parsing and exporting of sensor data.

    This class encapsulates all the functionality related to parsing sensor data
    from a source file and exporting it to CSV format.
    """

    def __init__(self):
        """
        Initialize the SensorDataParser with necessary constants and mappings.
        """
        self.HEADER_LINES = 36
        self.SENSORS = ['ACCE', 'GYRO', 'MAGN', 'PRES', 'LIGH',
                        'PROX', 'HUMI', 'TEMP', 'AHRS', 'GNSS',
                        'WIFI', 'BLUE', 'BLE4', 'SOUN', 'RFID',
                        'IMUX', 'IMUL', 'POSI']
        self.sensor_class_map = {
            'ACCE': AccelerometerSensor.AccelerometerSensor,
            'GYRO': GyroscopeSensor.GyroscopeSensor,
            'MAGN': MagnetometerSensor.MagnetometerSensor,
            'PRES': PressureSensor.PressureSensor,
            'LIGH': LightSensor.LightSensor,
            'PROX': ProximitySensor.ProximitySensor,
            'HUMI': HumiditySensor.HumiditySensor,
            'TEMP': TemperatureSensor.TemperatureSensor,
            'AHRS': OrientationSensor.OrientationSensor,
            'GNSS': GNSS_GPS_Sensor.GNSS_GPS_Sensor,
            'WIFI': WifiSensor.WifiSensor,
            'BLUE': BluetoothSensor.BluetoothSensor,
            'BLE4': BLE4Sensor.BLE4Sensor,
            'SOUN': SoundSensor.SoundSensor,
            'RFID': RFID_ReaderSensor.RFID_ReaderSensor,
            'IMUX': IMU_XSensSensor.IMU_XSensSensor,
            'IMUL': IMU_LPMS_B_Sensor.IMU_LPMS_B_Sensor,
            'POSI': POSI_Sensor.POSI_Sensor
        }

    def parser(self, file_source: str, target_sensor: Optional[str] = None, include_calculated: bool = False) -> None:
        """
        Parse and export sensor data from a source file.

        This function orchestrates the entire process of parsing sensor data from a file
        and exporting it to CSV format. It follows these main steps:
        1. Validate input parameters
        2. Parse the sensor data from the source file
        3. Export the parsed data to CSV file(s)

        Args:
            file_source (str): Path to the source file containing sensor data.
            target_sensor (str, optional): Name of the specific sensor to export data for.
                If None, data for all sensors will be processed.
            include_calculated (bool): Whether to include calculated values in the export.

        Raises:
            FileNotFoundError: If the source file does not exist.
            ValueError: If the source file is not a .txt file or if the target file is not a .csv file.
        """
        # validated input parameters to ensure correct file types and sensor names
        self.validate_input_parameters(file_source, target_sensor)
        
        # parsed sensor data from the source file into a list of sensor objects
        sensors_data = self.parse_sensor_data(file_source)
        
        # exported parsed data to csv file(s) based on the specified parameters
        self.export_sensor_data(sensors_data, target_sensor, include_calculated)

    def validate_input_parameters(self, file_source: str, target_sensor: Optional[str]) -> None:
        """
        Validate the input parameters for the parser function.

        This function performs several checks:
        1. Ensures the source file has a .txt extension
        2. Verifies that the source file exists
        3. If a target file is specified, ensures it has a .csv extension
        4. If a target sensor is specified, ensures it's a valid sensor type

        Args:
            file_source (str): Path to the source file containing sensor data.
            target_sensor (str, optional): Name of the specific sensor to export data for.

        Raises:
            ValueError: If any of the input parameters are invalid.
            FileNotFoundError: If the source file does not exist.
        """
        # checked if the source file had a .txt extension to ensure correct file format
        if not file_source.endswith('.txt'):
            raise ValueError('Invalid File Type! Source File Must Be .txt!')
        
        # verified that the source file existed to prevent processing non-existent files
        if not os.path.exists(file_source):
            raise FileNotFoundError('Source File Not Found!')
        
        # checked if the specified target sensor was valid to prevent processing invalid sensor types
        if target_sensor is not None and target_sensor not in self.SENSORS:
            raise ValueError(f'Invalid Sensor! Available Sensors: {", ".join(self.SENSORS)}')

    def parse_sensor_data(self, file_source: str) -> List:
        """
        Parse sensor data from the source file.

        This function reads the source file line by line, skipping header lines,
        and creates appropriate sensor objects based on the data in each line.

        Args:
            file_source (str): Path to the source file containing sensor data.

        Returns:
            List: A list of parsed sensor objects.
        """
        sensors_data = []  # list to store all the parsed sensors data 

        # opened and read the source file to process sensor data
        with open(file_source, 'r') as file:
            for line_number, line in enumerate(file, 1):
                # skipped header lines to focus on actual data
                if line_number <= self.HEADER_LINES:
                    continue
                
                # parsed each line into sensor type and values for object creation
                data_row = line.strip().split(';')
                sensor_type = data_row[0]
                sensor_values = data_row[1:]

                # created a sensor object based on the sensor tag and appended it to sensors_data list
                sensor_class = self.sensor_class_map.get(sensor_type)
                if sensor_class:
                    try:
                        sensors_data.append(sensor_class(*sensor_values))
                    except Exception as e:
                        print(f"Error parsing line {line_number}: {e}")

        print(f"[INFO] Parsed Total {len(sensors_data)} Lines\n")
        return sensors_data

    def export_sensor_data(self, sensors_data: List, target_sensor: Optional[str], include_calculated: bool) -> None:
        """
        Export the parsed sensor data to CSV file(s).

        This function handles the export process, which includes:
        1. Determining whether to export a single sensor or all sensors
        2. Creating necessary directories with timestamps
        3. Writing data to CSV file(s) with timestamps
        4. Handling the export process for multiple sensors if required

        Args:
            sensors_data (List): List of parsed sensor objects.
            target_sensor (str, optional): Name of the specific sensor to export data for.
            include_calculated (bool): Whether to include calculated values in the export.
        """
        # generated a timestamp for unique file naming
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if include_calculated:
            timestamp = f"c_{timestamp}"
        
        # determined if exporting a single sensor or all sensors based on input parameters
        export_single_sensor = target_sensor is not None

        target_file_name = None

        # set up export directory and file name if exporting all sensors
        if target_sensor is None:
            export_dir = f'all_sensors_data_{timestamp}'
            os.makedirs(export_dir, exist_ok=True)
            target_sensor = 'ACCE'  # started with accelerometer data
            target_file_name = f'{export_dir}/{target_sensor.upper()}_sensor_{timestamp}.csv'
        elif export_single_sensor:
            # for single sensor, generate file name based on sensor type
            target_file_name = f'{target_sensor.upper()}_sensor_{timestamp}.csv'

        # defined headers for each sensor type, including calculated values if specified
        headers = self.get_headers(include_calculated)

        while True:
            # opened the target file and wrote data
            with open(target_file_name, 'w') as file:
                # wrote the header line for the current sensor
                file.write(f"{headers[target_sensor]}\n")

                # exported data for the current sensor
                index = 1
                for sensor in sensors_data:
                    if sensor.tag == target_sensor:
                        file.write(f'{sensor.export_row(index, include_calculated)}\n')
                        index += 1
                
            print(f"[INFO] Exported Total {index - 1} Records For Sensor {target_sensor.upper()}")
            print(f"[INFO] Exported Data Saved in '{target_file_name}'")

            # if exporting a single sensor, ended the process
            if export_single_sensor:
                break

            # moved to the next sensor if exporting all sensors
            index_of_target_sensor = self.SENSORS.index(target_sensor)
            if index_of_target_sensor < len(self.SENSORS) - 1:
                target_sensor = self.SENSORS[index_of_target_sensor + 1]
                target_file_name = f'{export_dir}/{target_sensor.upper()}_sensor_{timestamp}.csv'
            else: 
                break  # finished processing all sensors

    def get_headers(self, include_calculated: bool) -> dict:
        """
        Get the headers for each sensor type.

        This function returns a dictionary of headers for each sensor type,
        including calculated values if specified.

        Args:
            include_calculated (bool): Whether to include calculated values in the headers.

        Returns:
            dict: A dictionary of headers for each sensor type.
        """
        return {
            'ACCE': AccelerometerSensor.AccelerometerSensor.get_headers(include_calculated),
            'GYRO': GyroscopeSensor.GyroscopeSensor.get_headers(include_calculated),
            'MAGN': MagnetometerSensor.MagnetometerSensor.get_headers(include_calculated),
            'PRES': PressureSensor.PressureSensor.get_headers(include_calculated),
            'LIGH': LightSensor.LightSensor.get_headers(include_calculated),
            'PROX': ProximitySensor.ProximitySensor.get_headers(include_calculated),
            'HUMI': HumiditySensor.HumiditySensor.get_headers(include_calculated),
            'TEMP': TemperatureSensor.TemperatureSensor.get_headers(include_calculated),
            'AHRS': OrientationSensor.OrientationSensor.get_headers(include_calculated),
            'GNSS': GNSS_GPS_Sensor.GNSS_GPS_Sensor.get_headers(include_calculated),
            'WIFI': WifiSensor.WifiSensor.get_headers(include_calculated),
            'BLUE': BluetoothSensor.BluetoothSensor.get_headers(include_calculated),
            'BLE4': BLE4Sensor.BLE4Sensor.get_headers(include_calculated),
            'SOUN': SoundSensor.SoundSensor.get_headers(include_calculated),
            'RFID': RFID_ReaderSensor.RFID_ReaderSensor.get_headers(include_calculated),
            'IMUX': IMU_XSensSensor.IMU_XSensSensor.get_headers(include_calculated),
            'IMUL': IMU_LPMS_B_Sensor.IMU_LPMS_B_Sensor.get_headers(include_calculated),
            'POSI': POSI_Sensor.POSI_Sensor.get_headers(include_calculated)
        }

def print_help() -> None:
    """
    Print a help message describing the usage of the script.

    This function displays information about how to use the script,
    including the correct syntax and available options.
    """
    print('Usage:')
    print('python parser003.py <source_file> [options]')
    print('\nOptions:')
    print('-h, --help\t\tShow this help message and exit')
    print('-all\t\t\tParse all sensors data')
    print('-o <sensor_name>\tParse specific sensor data')
    print('-c\t\t\tInclude calculated values')

def print_intro() -> None:
    """
    Print an introductory message for the script.

    This function displays a formatted introduction message that includes
    the script's purpose and developer information.
    """
    ROW_WIDTH = 62
    print('=' * ROW_WIDTH)
    print('003 - SENSOR DATA PARSER'.center(ROW_WIDTH))
    print('-' * ROW_WIDTH)
    print('To Parse Data Generated by GetSensorData App'.center(ROW_WIDTH))
    print('and Export Sensor Data in CSV Format'.center(ROW_WIDTH))
    print('-' * ROW_WIDTH)
    print('Developed By: Saad Mansoor (24015919-003)'.center(ROW_WIDTH))
    print('Programming Languages - Assignment 01 - Task 01'.center(ROW_WIDTH))
    print('=' * ROW_WIDTH)
    print()

def main() -> None:
    """
    Main function to handle command-line arguments and execute the parser.

    This function processes the command-line arguments, validates them,
    and calls the appropriate functions based on the provided options.
    It also handles any exceptions that might occur during execution.
    """
    # set up argument parser to handle command-line inputs
    arg_parser = argparse.ArgumentParser(description='Sensor Data Parser', add_help=False)
    arg_parser.add_argument('source_file', nargs='?', help='Source file containing sensor data')
    arg_parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
    arg_parser.add_argument('-all', action='store_true', help='Parse all sensors data')
    arg_parser.add_argument('-o', nargs=1, metavar='sensor_name', help='Parse specific sensor data')
    arg_parser.add_argument('-c', action='store_true', help='Include calculated values')

    # parsed command-line arguments
    args = arg_parser.parse_args()

    # printed introduction
    print_intro()

    # if help was requested, printed intro and help message
    if args.help:
        print_help()
        return

    # checked if source file was provided
    if not args.source_file:
        print("Error: Source file is required.")
        print_help()
        return

    try:
        # created an instance of SensorDataParser
        parser = SensorDataParser()
        
        # executed parser based on provided arguments
        if args.all:
            parser.parser(args.source_file, include_calculated=args.c)
        elif args.o:
            parser.parser(args.source_file, target_sensor=args.o[0], include_calculated=args.c)
        else:
            print("Error: Invalid arguments.")
            print_help()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()