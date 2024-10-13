class BluetoothCalculator:
    """
    A class to perform calculations related to Bluetooth sensor data.
    """

    @staticmethod
    def calculate_signal_strength(RSS: int) -> str:
        """
        Calculate the signal strength based on the Received Signal Strength (RSS).

        Args:
            RSS (int): Received Signal Strength.

        Returns:
            str: 'Strong Signal' if RSS >= -60, otherwise 'Weak Signal'.
        """
        return 'Strong Signal' if RSS >= -60 else 'Weak Signal'