class PressureCalculator:
    """
    A class to perform calculations related to pressure sensor data.
    """

    @staticmethod
    def calculate_psi(pressure: float) -> float:
        """
        Calculate pressure in PSI from hPa.

        Args:
            pressure (float): Pressure value in hPa.

        Returns:
            float: Pressure value in PSI.
        """
        return pressure * 0.0145038

    @staticmethod
    def estimate_altitude(pressure: float, sea_level_pressure: float = 1013.25) -> float:
        """
        Estimate altitude based on pressure.

        Args:
            pressure (float): Pressure value in hPa.
            sea_level_pressure (float): Sea level pressure in hPa. Defaults to 1013.25.

        Returns:
            float: Estimated altitude in meters.
        """
        return 44330 * (1 - (pressure / sea_level_pressure) ** (1/5.255))