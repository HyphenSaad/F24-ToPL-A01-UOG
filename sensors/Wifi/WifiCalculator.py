class WifiCalculator:
    """
    A class to perform calculations related to WiFi sensor data.

    This class provides static methods for WiFi-related calculations.

    Methods:
        calculate_signal_strength(rss): Calculate signal strength category based on RSS.
    """

    @staticmethod
    def calculate_signal_strength(rss):
        """
        Calculate the signal strength category based on RSS value.

        Args:
            rss (int): Received Signal Strength.

        Returns:
            str: Signal strength category (Excellent, Good, Fair, Weak, or Very Weak).
        """
        if rss >= -50:
            return 'Excellent'
        elif -50 > rss >= -70:
            return 'Good'
        elif -70 > rss >= -80:
            return 'Fair'
        elif -80 > rss >= -90:
            return 'Weak'
        else:
            return 'Very Weak'