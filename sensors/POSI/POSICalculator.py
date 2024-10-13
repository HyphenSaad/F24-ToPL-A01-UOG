class POSICalculator:
    """
    A class to perform calculations related to POSI (Position) sensor data.
    """

    @staticmethod
    def calculate_lat_long_product(latitude: float, longitude: float) -> float:
        """
        Calculate the product of latitude and longitude.

        Args:
            latitude (float): The latitude coordinate.
            longitude (float): The longitude coordinate.

        Returns:
            float: The product of latitude and longitude.
        """
        return latitude * longitude