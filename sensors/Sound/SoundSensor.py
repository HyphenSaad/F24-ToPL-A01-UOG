from ..Base.SensorBase import SensorBase
from .SoundCalculator import SoundCalculator

class SoundSensor(SensorBase):
    """
    A class to store Sound Sensor Data.

    This class inherits from SensorBase and provides functionality specific to sound sensors.

    Attributes:
        RMS (float): Root Mean Square of the sound signal.
        pressure (float): Sound pressure.
        SPL (float): Sound Pressure Level.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.

    Methods:
        export_row(index): Export sound data as a row for CSV file.

    Inherited Methods:
        From SensorBase class.
    """

    def __init__(self, app_timestamp, RMS, pressure, SPL):
        """
        Initialize a SoundSensor object.

        Args:
            app_timestamp (float): Application timestamp.
            RMS (float): Root Mean Square of the sound signal.
            pressure (float): Sound pressure.
            SPL (float): Sound Pressure Level.
        """
        super().__init__('SOUN', float(app_timestamp))
        self.RMS = float(RMS)
        self.pressure = float(pressure)
        self.SPL = float(SPL)
    
    def export_row(self, index, include_calculated=True):
        """
        Export sound data as a row for CSV file.

        Args:
            index (int): Row index.
            include_calculated (bool): Whether to include the calculated sound pressure level category.

        Returns:
            str: Comma-separated string of sensor data.
        """
        base_row = f'{index},{self.RMS},{self.pressure},{self.SPL}'
        if include_calculated:
            return f'{base_row},{SoundCalculator.calculate_spl_category(self.SPL)}'
        return base_row
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for the CSV file.

        Args:
            include_calculated (bool): Whether to include the header for calculated sound pressure level category.

        Returns:
            str: Comma-separated string of header names.
        """
        return 'index,RMS,pressure,SPL' + (',sound_pressure_level' if include_calculated else '')