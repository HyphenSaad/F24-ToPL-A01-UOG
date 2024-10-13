from ..Base.SensorBase import SensorBase
from .IMUCalculator import IMUCalculator

class IMU_SensorBase(SensorBase):
    """
    A base class for IMU (Inertial Measurement Unit) sensors.

    This class inherits from SensorBase and provides common attributes and methods
    for all IMU sensors.

    Attributes:
        counter (int): A counter value.
        acc_X (float): Accelerometer X-axis reading.
        acc_Y (float): Accelerometer Y-axis reading.
        acc_Z (float): Accelerometer Z-axis reading.
        gyr_X (float): Gyroscope X-axis reading.
        gyr_Y (float): Gyroscope Y-axis reading.
        gyr_Z (float): Gyroscope Z-axis reading.
        mag_X (float): Magnetometer X-axis reading.
        mag_Y (float): Magnetometer Y-axis reading.
        mag_Z (float): Magnetometer Z-axis reading.
        roll (float): Roll angle.
        pitch (float): Pitch angle.
        yaw (float): Yaw angle.
        quat_1 (float): Quaternion component 1.
        quat_2 (float): Quaternion component 2.
        quat_3 (float): Quaternion component 3.
        quat_4 (float): Quaternion component 4.
        pressure (float): Pressure reading.
        temp (float): Temperature reading.

    Inherited Attributes:
        tag (str): Sensor tag or sensor ID to identify sensor type.
        app_timestamp (float): Application timestamp.
    """

    def __init__(self, tag, app_timestamp, counter, acc_X, acc_Y, acc_Z, gyr_X, gyr_Y, gyr_Z, 
                 mag_X, mag_Y, mag_Z, roll, pitch, yaw, quat_1, quat_2, quat_3, quat_4, 
                 pressure, temp):
        """
        Initialize the IMU_SensorBase object.

        Args:
            tag (str): Sensor tag or ID.
            app_timestamp (float): Application timestamp.
            counter (int): Counter value.
            acc_X, acc_Y, acc_Z (float): Accelerometer readings.
            gyr_X, gyr_Y, gyr_Z (float): Gyroscope readings.
            mag_X, mag_Y, mag_Z (float): Magnetometer readings.
            roll, pitch, yaw (float): Orientation angles.
            quat_1, quat_2, quat_3, quat_4 (float): Quaternion components.
            pressure (float): Pressure reading.
            temp (float): Temperature reading.
        """
        super().__init__(tag, float(app_timestamp))
        self.counter = int(counter)
        self.acc_X = float(acc_X)
        self.acc_Y = float(acc_Y)
        self.acc_Z = float(acc_Z)
        self.gyr_X = float(gyr_X)
        self.gyr_Y = float(gyr_Y)
        self.gyr_Z = float(gyr_Z)
        self.mag_X = float(mag_X)
        self.mag_Y = float(mag_Y)
        self.mag_Z = float(mag_Z)
        self.roll = float(roll)
        self.pitch = float(pitch)
        self.yaw = float(yaw)
        self.quat_1 = float(quat_1)
        self.quat_2 = float(quat_2)
        self.quat_3 = float(quat_3)
        self.quat_4 = float(quat_4)
        self.pressure = float(pressure)
        self.temp = float(temp)
    
    def export_row(self, index, include_calculated=False):
        """
        Export IMU data as a row for a CSV file.

        Args:
            index (int): The row index.
            include_calculated (bool): Whether to include calculated values.

        Returns:
            str: A comma-separated string containing all IMU data and optionally the calculated angular velocity magnitude.
        """
        # created base row with all IMU data
        base_row = f'{index},{self.acc_X},{self.acc_Y},{self.acc_Z},{self.gyr_X},{self.gyr_Y},{self.gyr_Z},{self.mag_X},{self.mag_Y},{self.mag_Z},{self.roll},{self.pitch},{self.yaw},{self.quat_1},{self.quat_2},{self.quat_3},{self.quat_4},{self.pressure},{self.temp}'
        
        if include_calculated:
            # calculated angular velocity magnitude using IMUCalculator
            angular_velocity_magnitude = IMUCalculator.calculate_angular_velocity_magnitude(self.gyr_X, self.gyr_Y, self.gyr_Z)
            return f'{base_row},{angular_velocity_magnitude}'
        
        return base_row