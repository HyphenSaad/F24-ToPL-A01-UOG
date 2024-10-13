class SoundCalculator:
    """
    A class to perform calculations related to sound data.

    This class provides static methods for calculating sound pressure level categories.

    Methods:
        calculate_spl_category(spl): Calculate sound pressure level category.
    """

    @staticmethod
    def calculate_spl_category(spl):
        """
        Calculate the sound pressure level category.

        Args:
            spl (float): Sound Pressure Level.

        Returns:
            str: 'High' if SPL >= 90, 'Moderate' if 70 <= SPL < 90, 'Low' otherwise.
        """
        if spl >= 90:
            return 'High'
        elif 70 <= spl < 90:
            return 'Moderate'
        else:
            return 'Low'