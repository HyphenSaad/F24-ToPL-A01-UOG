import math
from geopy.distance import geodesic

class GNSS_GPS_Calculator:
    """
    A class to perform calculations related to GNSS/GPS data.
    """

    @staticmethod
    def calculate_total_speed(speed: float, bearing: float) -> float:
        """
        Calculate the total speed based on speed and bearing.

        Args:
            speed (float): The speed value.
            bearing (float): The bearing value.

        Returns:
            float: The calculated total speed.
        """
        return math.sqrt(speed ** 2 + bearing ** 2)
    
    @staticmethod
    def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """
        Calculate the distance between two GPS coordinates.

        Args:
            lat1 (float): Latitude of the first point.
            lon1 (float): Longitude of the first point.
            lat2 (float): Latitude of the second point.
            lon2 (float): Longitude of the second point.

        Returns:
            float: The calculated distance in meters.
        """
        return geodesic((lat1, lon1), (lat2, lon2)).meters