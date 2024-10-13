from ..Base.SensorBase import SensorBase
from .GNSS_GPS_Calculator import GNSS_GPS_Calculator

class GNSS_GPS_Sensor(SensorBase):
    """
    A class to represent a GNSS/GPS Sensor.

    This class inherits from SensorBase and is used to store and process
    GNSS/GPS sensor data.

    Attributes:
        latit (float): Latitude.
        long (float): Longitude.
        altitude (float): Altitude.
        bearing (float): Bearing.
        speed (float): Speed.
        sat_in_view (int): Number of satellites in view.
        sat_in_use (int): Number of satellites in use.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.
        sensor_timestamp (float): Sensor timestamp.
        accuracy (float): Sensor accuracy.

    Methods:
        export_row(index, include_calculated): Export GNSS/GPS data as a row for CSV file.
    """

    def __init__(self, app_timestamp, sensor_timestamp, latit, long, altitude, bearing, accuracy, speed, sat_in_view, sat_in_use):
        """
        Initialize the GNSS_GPS_Sensor object.

        Args:
            app_timestamp (float): Application timestamp.
            sensor_timestamp (float): Sensor timestamp.
            latit (float): Latitude.
            long (float): Longitude.
            altitude (float): Altitude.
            bearing (float): Bearing.
            accuracy (float): Sensor accuracy.
            speed (float): Speed.
            sat_in_view (int): Number of satellites in view.
            sat_in_use (int): Number of satellites in use.
        """
        super().__init__('GNSS', float(app_timestamp), float(sensor_timestamp), float(accuracy))
        self.latit = float(latit)
        self.long = float(long)
        self.altitude = float(altitude)
        self.bearing = float(bearing)
        self.speed = float(speed)
        self.sat_in_view = int(sat_in_view)
        self.sat_in_use = int(sat_in_use)
    
    def export_row(self, index, include_calculated=False):
        """
        Export GNSS/GPS data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: A comma-separated string of values representing the row.
        """
        base_row = f'{index},{self.latit},{self.long},{self.altitude},{self.bearing},{self.speed},{self.sat_in_view},{self.sat_in_use}'
        if include_calculated:
            total_speed = GNSS_GPS_Calculator.calculate_total_speed(self.speed, self.bearing)
            return f'{base_row},{total_speed}'
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
        return 'index,latit,long,altitude,bearing,speed,sat_in_view,sat_in_use' + (',total_speed' if include_calculated else '')