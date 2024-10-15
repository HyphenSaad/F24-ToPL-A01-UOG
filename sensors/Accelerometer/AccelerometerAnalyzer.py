import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
        self.df['magnitude'] = np.sqrt(self.df['acc_x']**2 + self.df['acc_y']**2 + self.df['acc_z']**2)

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

    def visualize_activity_recognition(self):
        """
        Visualize the accelerometer data to identify different activities (sitting, walking, and running) over time.
        """
        plt.figure(figsize=(15, 8))

        # defined thresholds for activity recognition
        sitting_threshold = 8.5
        walking_threshold = 10.5
        running_threshold = 20.0

        # creating activity labels
        self.df['activity'] = pd.cut(self.df['magnitude'], 
                                     bins=[-np.inf, sitting_threshold, walking_threshold, running_threshold, np.inf],
                                     labels=['unknown', 'sitting/stationary', 'walking', 'running'])

        # plotting the data
        plt.plot(self.df['timestamp'], self.df['magnitude'], color='black', linewidth=0.8, label='Magnitude')

        # colored the background based on activities
        colors = {'unknown': 'white', 'sitting/stationary': 'lightblue', 'walking': 'lightgreen', 'running': 'lightcoral'}
        for activity in ['sitting/stationary', 'walking', 'running']:
            mask = self.df['activity'] == activity
            plt.fill_between(self.df['timestamp'], 0, self.df['magnitude'], where=mask, 
                             facecolor=colors[activity], alpha=0.66, label=f'{activity.capitalize()} State')

        plt.title('Activity Recognition', fontsize=14)
        plt.xlabel('Time')
        plt.ylabel('Acceleration Magnitude (m/s^2)')

        plt.axhline(y=sitting_threshold, color='blue', linestyle='--', linewidth=1, label='Sitting/Stationary Threshold')
        plt.axhline(y=walking_threshold, color='green', linestyle='--', linewidth=1, label='Walking Threshold')
        plt.axhline(y=running_threshold, color='red', linestyle='--', linewidth=1, label='Running Threshold')

        plt.legend(loc='upper right')
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.tight_layout()
        plt.show()

    def plot_3d_orientation(self):
        """
        Plot the accelerometer data in 3D to visualize the orientation of the device.
        """
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.df['acc_x'], self.df['acc_y'], self.df['acc_z'])
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        ax.set_title('3D Orientation of the Device')
        plt.show()

    def detect_impacts(self, threshold: float = 15) -> pd.DataFrame:
        """
        Detect impacts based on a magnitude threshold.

        Args:
            threshold (float): The magnitude threshold for impact detection.

        Returns:
            pd.DataFrame: A DataFrame containing detected impacts.
        """
        impacts = self.df[self.df['magnitude'] > threshold]
        return impacts

    def visualize_impacts(self, threshold: float = 15):
        """
        Visualize detected impacts on the magnitude plot.

        Args:
            threshold (float): The magnitude threshold for impact detection.
        """
        impacts = self.detect_impacts(threshold)
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['magnitude'], label='Magnitude')
        plt.scatter(impacts['timestamp'], impacts['magnitude'], color='red', label='Impacts')
        plt.title(f'Impact Detection (Threshold: {threshold} m/s^2)')
        plt.xlabel('Time')
        plt.ylabel('Acceleration Magnitude (m/s^2)')
        plt.axhline(y=threshold, color='g', linestyle='--', label='Threshold')
        plt.legend()
        plt.grid(True)
        plt.show()

    def run_analysis(self):
        """
        Run a comprehensive analysis of the accelerometer data.
        """
        print("Running Accelerometer Analysis...")
        
        # to visualize activity recognition
        self.visualize_activity_recognition()
        
        # to plot 3D orientation
        self.plot_3d_orientation()
        
        # to visualize impacts
        self.visualize_impacts()
        
        # to detect impacts
        impacts = self.detect_impacts()
        print(f"Number of Detected Impacts: {len(impacts)}")
        if not impacts.empty:
            print("Impact Times:")
            for _, impact in impacts.iterrows():
                print(f"  {impact['timestamp']}: Magnitude = {impact['magnitude']:.2f} m/s^2")

        # to print accelerometer statistics
        print("\nAccelerometer Statistics:")
        print(f"Max Acceleration Magnitude: {self.df['magnitude'].max():.2f} m/s^2")
        print(f"Min Acceleration Magnitude: {self.df['magnitude'].min():.2f} m/s^2")
        print(f"Mean Acceleration Magnitude: {self.df['magnitude'].mean():.2f} m/s^2")
        print(f"Standard Deviation of Acceleration Magnitude: {self.df['magnitude'].std():.2f} m/s^2")

        print("\nAccelerometer Data Analysis Completed!")
