class HumidityCalculator:
    """
    A class to perform calculations related to humidity data.
    """

    @staticmethod
    def calculate_humidity_percentage(humidity: float) -> float:
        """
        Calculate the humidity in percentage.

        Args:
            humidity (float): The raw humidity value.

        Returns:
            float: The humidity value in percentage.
        """
        return humidity * 100