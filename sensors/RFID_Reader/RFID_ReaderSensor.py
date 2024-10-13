from ..Base.SensorBase import SensorBase
from .RFIDCalculator import RFIDCalculator

class RFID_ReaderSensor(SensorBase):
    """
    A class to store RFID Reader Sensor Data.

    This class inherits from SensorBase and provides functionality specific to RFID readers.

    Attributes:
        reader_number (int): The identifier for the RFID reader.
        tag_id (int): The identifier for the RFID tag.
        rss_A (int): The Received Signal Strength (RSS) from antenna A.
        rss_B (int): The Received Signal Strength (RSS) from antenna B.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID, to identify sensor type.
        app_timestamp (float): Application timestamp.
    """

    def __init__(self, app_timestamp, reader_number, tag_id, rss_A, rss_B):
        """
        Initialize the RFID_ReaderSensor object.

        Args:
            app_timestamp (float): The application timestamp.
            reader_number (int): The identifier for the RFID reader.
            tag_id (int): The identifier for the RFID tag.
            rss_A (int): The Received Signal Strength (RSS) from antenna A.
            rss_B (int): The Received Signal Strength (RSS) from antenna B.
        """
        super().__init__('RFID', float(app_timestamp))
        self.reader_number = int(reader_number)
        self.tag_id = int(tag_id)
        self.rss_A = int(rss_A)
        self.rss_B = int(rss_B)

    def export_row(self, index, include_calculated=True):
        """
        Export RFID Reader data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include the calculated average RSS.

        Returns:
            str: A comma-separated string containing the RFID reader data.
        """
        base_row = f'{index},{self.reader_number},{self.tag_id},{self.rss_A},{self.rss_B}'
        if include_calculated:
            # calculated average rss using RFIDCalculator
            avg_rss = RFIDCalculator.calculate_average_rss(self.rss_A, self.rss_B)
            return f'{base_row},{avg_rss}'
        return base_row
    
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for the CSV file.

        Args:
            include_calculated (bool): Whether to include the header for the calculated value.

        Returns:
            str: A comma-separated string of header names.
        """
        return 'index,reader_number,tag_id,rss_A,rss_B' + (',avg_rss' if include_calculated else '')