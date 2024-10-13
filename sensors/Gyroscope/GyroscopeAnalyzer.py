import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple
from .GyroscopeCalculator import GyroscopeCalculator

class GyroscopeAnalyzer:
    """
    A class to analyze gyroscope data.

    Attributes:
        df (pd.DataFrame): The DataFrame containing the gyroscope data.

    Methods:
        plot_angular_velocity(): Plot the angular velocity magnitude over time.
        plot_rotation_detection(): Plot the rotation detection for each axis.
        analyze_stabilization(): Analyze the stabilization of the gyroscope.
        run_analysis(): Run a comprehensive analysis of the gyroscope data.
    """

    def __init__(self, csv_file_path: str):
        """
        Initialize the GyroscopeAnalyzer object.

        Args:
            csv_file_path (str): The path to the CSV file containing the gyroscope data.
        """
        self.df = pd.read_csv(csv_file_path)
        self.df['timestamp'] = pd.to_datetime(self.df['index'], unit='s')
        self.df['time_delta'] = self.df['timestamp'].diff().dt.total_seconds()
        self.df['rotation_angle'] = self.df.apply(lambda row: GyroscopeCalculator.calculate_rotation_angle(row['angular_velocity_magnitude'], row['time_delta']), axis=1)

    def plot_angular_velocity(self):
        """
        Plot the angular velocity magnitude over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['angular_velocity_magnitude'])
        plt.title('Angular Velocity Magnitude Over Time')
        plt.xlabel('Time')
        plt.ylabel('Angular Velocity Magnitude (rad/s)')
        plt.grid(True)
        plt.show()

    def plot_rotation_detection(self):
        """
        Plot the rotation detection for each axis.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['gyr_x'], label='X-axis')
        plt.plot(self.df['timestamp'], self.df['gyr_y'], label='Y-axis')
        plt.plot(self.df['timestamp'], self.df['gyr_z'], label='Z-axis')
        plt.title('Rotation Detection')
        plt.xlabel('Time')
        plt.ylabel('Angular Velocity (rad/s)')
        plt.legend()
        plt.grid(True)
        plt.show()

    def analyze_stabilization(self) -> Tuple[float, float, float]:
        """
        Analyze the stabilization of the gyroscope.

        Returns:
            Tuple[float, float, float]: The mean standard deviation for each axis.
        """
        window_size = 10  # adjust as needed
        rolling_std = self.df[['gyr_x', 'gyr_y', 'gyr_z']].rolling(window=window_size).std()
        return rolling_std['gyr_x'].mean(), rolling_std['gyr_y'].mean(), rolling_std['gyr_z'].mean()

    def run_analysis(self):
        """
        Run a comprehensive analysis of the gyroscope data.
        """
        print("Running Gyroscope Analysis...")
        
        # plotted angular velocity
        self.plot_angular_velocity()
        
        # plotted rotation detection
        self.plot_rotation_detection()
        
        # analyzed stabilization
        x_stability, y_stability, z_stability = self.analyze_stabilization()
        print(f"Average Stability (lower is more stable):")
        print(f"X-axis: {x_stability:.4f}")
        print(f"Y-axis: {y_stability:.4f}")
        print(f"Z-axis: {z_stability:.4f}")
        
        # calculated additional statistics
        print("\nGyroscope Statistics:")
        print(f"Max Angular Velocity: {self.df['angular_velocity_magnitude'].max():.4f} rad/s")
        print(f"Mean Angular Velocity: {self.df['angular_velocity_magnitude'].mean():.4f} rad/s")
        print(f"Total Rotation Angle: {self.df['rotation_angle'].sum():.4f} radians")

        # identified periods of high rotation
        high_rotation_threshold = self.df['angular_velocity_magnitude'].quantile(0.95)
        high_rotation_periods = self.df[self.df['angular_velocity_magnitude'] > high_rotation_threshold]
        print(f"\nPeriods of High Rotation (above {high_rotation_threshold:.4f} rad/s):")
        for _, period in high_rotation_periods.iterrows():
            print(f"Time: {period['timestamp']}, Angular Velocity: {period['angular_velocity_magnitude']:.4f} rad/s")

        print("\nGyroscope Data Analysis Completed!")
