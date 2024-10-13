class LightCalculator:
    """
    A class to perform calculations related to light sensor data.
    """

    @staticmethod
    def calculate_double_light(light: float) -> float:
        """
        Calculate double of the light intensity.

        Args:
            light (float): Light intensity value.

        Returns:
            float: Double of the input light intensity.
        """
        return light * 2

    @staticmethod
    def detect_day_night(light: float, threshold: float = 50.0) -> str:
        """
        Detect whether it's day or night based on light intensity.

        Args:
            light (float): Light intensity value.
            threshold (float): Threshold to distinguish between day and night. Default is 50.0.

        Returns:
            str: 'Day' if light intensity is above threshold, 'Night' otherwise.
        """
        return 'Day' if light > threshold else 'Night'