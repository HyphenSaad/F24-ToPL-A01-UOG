class TemperatureCalculator:
    """
    A class to perform calculations related to temperature data.

    This class provides static methods for temperature-related calculations.

    Methods:
        celsius_to_fahrenheit(celsius): Convert Celsius to Fahrenheit.
    """

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """
        Convert temperature from Celsius to Fahrenheit.

        Args:
            celsius (float): Temperature in Celsius.

        Returns:
            float: Temperature in Fahrenheit.
        """
        return (celsius * 9/5) + 32