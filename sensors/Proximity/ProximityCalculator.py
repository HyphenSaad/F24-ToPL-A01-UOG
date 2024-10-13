class ProximityCalculator:
    """
    A class to perform calculations related to proximity sensor data.
    """

    @staticmethod
    def calculate_double_proximity(proximity: float) -> float:
        """
        Calculate the double of the proximity value.

        Args:
            proximity (float): The proximity value.

        Returns:
            float: The doubled proximity value.
        """
        return proximity * 2