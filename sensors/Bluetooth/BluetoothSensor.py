from ..Base.SensorBase import SensorBase
from .BluetoothCalculator import BluetoothCalculator

class BluetoothSensor(SensorBase):
    """
    A class to represent a Bluetooth Sensor.

    This class inherits from SensorBase and is used to store and process
    Bluetooth sensor data.

    Attributes:
        name (str): Name of the Bluetooth device.
        MAC_Address (str): MAC address of the Bluetooth device.
        RSS (int): Received Signal Strength.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.

    Methods:
        export_row(index, include_calculated): Export Bluetooth data as a row for CSV file.
    """

    def __init__(self, app_timestamp, name, MAC_Address, RSS):
        """
        Initialize the BluetoothSensor object.

        Args:
            app_timestamp (float): Application timestamp.
            name (str): Name of the Bluetooth device.
            MAC_Address (str): MAC address of the Bluetooth device.
            RSS (int): Received Signal Strength.
        """
        super().__init__('BLUE', float(app_timestamp))
        self.name = str(name)
        self.MAC_Address = str(MAC_Address)
        self.RSS = int(RSS)

    def export_row(self, index, include_calculated=False):
        """
        Export Bluetooth data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: A comma-separated string of values representing the row.
        """
        # created base row with sensor data
        base_row = f'{index},{self.name},{self.MAC_Address},{self.RSS}'
        
        if include_calculated:
            # calculated signal strength using BluetoothCalculator
            signal_strength = BluetoothCalculator.calculate_signal_strength(self.RSS)
            return f'{base_row},{signal_strength}'
        
        return base_row
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for the CSV file.

        Args:
            include_calculated (bool): Whether to include headers for calculated values.

        Returns:
            str: A comma-separated string of header names.
        """
        return 'index,name,MAC_Address,RSS' + (',signal_strength' if include_calculated else '')