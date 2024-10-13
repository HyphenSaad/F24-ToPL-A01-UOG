from ..Base.SensorBase import SensorBase
from .PressureCalculator import PressureCalculator

class PressureSensor(SensorBase):
    """
    A class to store and process pressure sensor data.

    This class inherits from SensorBase and provides functionality
    to store pressure sensor data.

    Attributes:
        pres (float): The pressure value.

    Inherited Attributes:
        tag (str): Sensor tag or ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.
        accuracy (int): Sensor accuracy.

    Methods:
        export_row(index, include_calculated): Export pressure data as a row for CSV file.
        get_headers(include_calculated): Get the headers for the CSV file.

    Inherited Methods:
        Other methods inherited from SensorBase.
    """

    def __init__(self, app_timestamp, sensor_timestamp, pres, accuracy):
        """
        Initialize a PressureSensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            pres (float): Pressure value.
            accuracy (int): Sensor accuracy.
        """
        super().__init__('PRES', float(app_timestamp), float(sensor_timestamp), int(accuracy))
        self.pres = float(pres)
    
    def export_row(self, index, include_calculated=False):
        """
        Export pressure data as a row for CSV file.

        Args:
            index (int): Row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: Formatted string containing index, pressure, and optionally calculated PSI and altitude.
        """
        base_row = f'{index},{self.pres}'
        if include_calculated:
            psi = PressureCalculator.calculate_psi(self.pres)
            altitude = PressureCalculator.estimate_altitude(self.pres)
            return f'{base_row},{psi},{altitude}'
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
        return 'index,pres' + (',pres_in_psi,estimated_altitude' if include_calculated else '')