from ..IMU_SensorBase.IMU_SensorBase import IMU_SensorBase

class IMU_LPMS_B_Sensor(IMU_SensorBase):
    """
    A wrapper class for IMU_LPMS_B_Sensor data.

    This class inherits from IMU_SensorBase and provides specific functionality
    for the LPMS-B IMU sensor.

    Attributes:
        Inherits all attributes from IMU_SensorBase.

    Methods:
        __init__: Initializes the IMU_LPMS_B_Sensor object.
        get_headers: Returns the headers for CSV export.
    """

    def __init__(self, app_timestamp, counter, acc_X, acc_Y, acc_Z, gyr_X, gyr_Y, gyr_Z,
                 mag_X, mag_Y, mag_Z, roll, pitch, yaw, quat_1, quat_2, quat_3, quat_4,
                 pressure, temp):
        """
        Initialize the IMU_LPMS_B_Sensor object.

        Args:
            app_timestamp (float): Application timestamp.
            counter (int): Sensor reading counter.
            acc_X, acc_Y, acc_Z (float): Acceleration in X, Y, Z axes.
            gyr_X, gyr_Y, gyr_Z (float): Gyroscope readings in X, Y, Z axes.
            mag_X, mag_Y, mag_Z (float): Magnetometer readings in X, Y, Z axes.
            roll, pitch, yaw (float): Euler angles.
            quat_1, quat_2, quat_3, quat_4 (float): Quaternion components.
            pressure (float): Pressure reading.
            temp (float): Temperature reading.
        """
        super().__init__('IMUL', app_timestamp, counter, acc_X, acc_Y, acc_Z, gyr_X, gyr_Y, gyr_Z,
                         mag_X, mag_Y, mag_Z, roll, pitch, yaw, quat_1, quat_2, quat_3, quat_4,
                         pressure, temp)
        
    @staticmethod
    def get_headers(include_calculated=False):
        """
        Get the headers for CSV export.

        Args:
            include_calculated (bool): Whether to include calculated values in the headers.

        Returns:
            str: A comma-separated string of header names.
        """
        base_headers = 'index,acc_x,acc_y,acc_z,gyr_x,gyr_y,gyr_z,mag_x,mag_y,mag_z,roll,pitch,yaw,quat_1,quat_2,quat_3,quat_4,pressure,temp'
        # added angular velocity magnitude to headers if calculated values are included
        return base_headers + (',angular_velocity_magnitude' if include_calculated else '')