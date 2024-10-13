import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple

class AccelerometerAnalyzer:
    """
    A class to analyze accelerometer data from a CSV file.
    """

    def __init__(self, csv_file_path: str):
        """
        Initialize the AccelerometerAnalyzer object.

        Args:
            csv_file_path (str): Path to the CSV file containing accelerometer data.
        """
        self.df = pd.read_csv(csv_file_path)
        self.df['timestamp'] = pd.to_datetime(self.df['index'], unit='s')

    def plot_acceleration_over_time(self):
        """
        Plot acceleration over time for all axes.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['acc_x'], label='X-axis')
        plt.plot(self.df['timestamp'], self.df['acc_y'], label='Y-axis')
        plt.plot(self.df['timestamp'], self.df['acc_z'], label='Z-axis')
        plt.title('Acceleration Over Time')
        plt.xlabel('Time')
        plt.ylabel('Acceleration (m/s^2)')
        plt.legend()
        plt.grid(True)
        plt.show()

    def plot_magnitude_over_time(self):
        """
        Plot acceleration magnitude over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['magnitude'])
        plt.title('Acceleration Magnitude Over Time')
        plt.xlabel('Time')
        plt.ylabel('Magnitude (m/s^2)')
        plt.grid(True)
        plt.show()

    def detect_activity(self) -> str:
        """
        Detect the type of activity based on average magnitude.

        Returns:
            str: The detected activity.
        """
        avg_magnitude = self.df['magnitude'].mean()
        if avg_magnitude < 1:
            return "Stationary"
        elif 1 <= avg_magnitude < 3:
            return "Walking"
        elif 3 <= avg_magnitude < 6:
            return "Running"
        else:
            return "High-intensity activity"

    def detect_orientation(self) -> Tuple[float, float, float]:
        """
        Detect the average orientation based on accelerometer data.

        Returns:
            Tuple[float, float, float]: Average acceleration along X, Y, and Z axes.
        """
        return self.df['acc_x'].mean(), self.df['acc_y'].mean(), self.df['acc_z'].mean()

    def detect_impacts(self, threshold: float = 15) -> pd.DataFrame:
        """
        Detect impacts based on a magnitude threshold.

        Args:
            threshold (float): The magnitude threshold for impact detection.

        Returns:
            pd.DataFrame: A DataFrame containing detected impacts.
        """
        return self.df[self.df['magnitude'] > threshold]

    def run_analysis(self):
        """
        Run a comprehensive analysis of the accelerometer data.
        """
        print("Running Accelerometer Analysis...")
        
        # plotted acceleration over time
        self.plot_acceleration_over_time()
        
        # plotted magnitude over time
        self.plot_magnitude_over_time()
        
        # performed activity recognition
        activity = self.detect_activity()
        print(f"Detected Activity: {activity}")
        
        # detected orientation
        x_orientation, y_orientation, z_orientation = self.detect_orientation()
        print(f"Average Orientation: X={x_orientation:.2f}, Y={y_orientation:.2f}, Z={z_orientation:.2f}")
        
        # detected impacts
        impacts = self.detect_impacts()
        print(f"Number of Detected Impacts: {len(impacts)}")
        if not impacts.empty:
            print("Impact Times:")
            for _, impact in impacts.iterrows():
                print(f"  {impact['timestamp']}: Magnitude = {impact['magnitude']:.2f} m/s^2")

        print("\nAccelerometer Statistics:")
        print(f"Max Acceleration Magnitude: {self.df['magnitude'].max():.2f} m/s^2")
        print(f"Mean Acceleration Magnitude: {self.df['magnitude'].mean():.2f} m/s^2")
        print(f"Standard Deviation of Acceleration Magnitude: {self.df['magnitude'].std():.2f} m/s^2")

        print("\nAccelerometer Data Analysis Completed!")
