from ..Base.SensorBase import SensorBase
from .WifiCalculator import WifiCalculator

class WifiSensor(SensorBase):
    """
    A class to store WiFi sensor data.

    This class inherits from SensorBase and provides functionality specific to WiFi sensors.

    Attributes:
        name_SSID (str): Name of the SSID.
        MAC_BSSID (str): MAC address of the BSSID.
        RSS (int): Received Signal Strength.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.

    Methods:
        export_row(index, include_calculated): Export WiFi data as a row for CSV file.
        get_headers(include_calculated): Get the headers for the CSV file.

    Inherited Methods:
        Other methods inherited from SensorBase.
    """

    def __init__(self, app_timestamp, sensor_timestamp, name_SSID, MAC_BSSID, RSS):
        """
        Initialize a WifiSensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            name_SSID (str): Name of the SSID.
            MAC_BSSID (str): MAC address of the BSSID.
            RSS (int): Received Signal Strength.
        """
        super().__init__('WIFI', float(app_timestamp), float(sensor_timestamp))
        self.name_SSID = str(name_SSID)
        self.MAC_BSSID = str(MAC_BSSID)
        self.RSS = int(RSS)
    
    def export_row(self, index, include_calculated=True):
        """
        Export WiFi data as a row for a CSV file.

        Args:
            index (int): Index of the row.
            include_calculated (bool): Whether to include the calculated signal strength category.

        Returns:
            str: Comma-separated string containing WiFi sensor data.
        """
        base_data = f'{index},{self.name_SSID},{self.MAC_BSSID},{self.RSS}'
        if include_calculated:
            # calculated signal strength using WifiCalculator
            signal_strength = WifiCalculator.calculate_signal_strength(self.RSS)
            return f'{base_data},{signal_strength}'
        return base_data
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for the CSV file.

        Args:
            include_calculated (bool): Whether to include the header for calculated signal strength.

        Returns:
            str: Comma-separated string of header names.
        """
        return 'index,name_SSID,MAC_BSSID,RSS' + (',signal_strength' if include_calculated else '')