class RFIDCalculator:
    """
    A class to perform calculations related to RFID Reader sensor data.
    """

    @staticmethod
    def calculate_average_rss(rss_A: int, rss_B: int) -> float:
        """
        Calculate the average Received Signal Strength (RSS) based on RSS_A and RSS_B.

        Args:
            rss_A (int): The Received Signal Strength (RSS) from antenna A.
            rss_B (int): The Received Signal Strength (RSS) from antenna B.

        Returns:
            float: The average Received Signal Strength.
        """
        return (rss_A + rss_B) / 2