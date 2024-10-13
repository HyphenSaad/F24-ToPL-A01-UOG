import pandas as pd
import matplotlib.pyplot as plt

class OrientationAnalyzer:
    """
    A class to analyze orientation sensor data from a CSV file.

    Attributes:
        df (pandas.DataFrame): The dataframe containing the orientation sensor data.

    Methods:
        plot_3d_orientation(): Plot the 3D orientation of the device.
        plot_rotation_over_time(): Plot the rotation magnitude over time.
        detect_significant_rotations(threshold): Detect and plot significant rotations.
        analyze_stabilization(window_size): Analyze and plot device stabilization.
        run_analysis(): Run all analysis methods and print statistics.
    """

    def __init__(self, csv_file_path: str):
        """
        Initialize the OrientationAnalyzer object.

        Args:
            csv_file_path (str): Path to the CSV file containing orientation sensor data.
        """
        self.df = pd.read_csv(csv_file_path)
        self.df['timestamp'] = pd.to_datetime(self.df['index'], unit='s')
        
    def plot_3d_orientation(self):
        """
        Plot the 3D orientation of the device.
        """
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        ax.scatter(self.df['pitch_x'], self.df['roll_y'], self.df['yaw_z'])
        ax.set_xlabel('Pitch (X)')
        ax.set_ylabel('Roll (Y)')
        ax.set_zlabel('Yaw (Z)')
        ax.set_title('3D Device Orientation')
        plt.show()

    def plot_rotation_over_time(self):
        """
        Plot the rotation magnitude over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['rotation_magnitude'])
        plt.title('Rotation Magnitude Over Time')
        plt.xlabel('Time')
        plt.ylabel('Rotation Magnitude')
        plt.grid(True)
        plt.show()

    def detect_significant_rotations(self, threshold=0.5):
        """
        Detect and plot significant rotations.

        Args:
            threshold (float): The threshold for significant rotation magnitude.
        """
        significant_rotations = self.df[self.df['rotation_magnitude'] > threshold]
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['rotation_magnitude'], label='Rotation Magnitude')
        plt.scatter(significant_rotations['timestamp'], significant_rotations['rotation_magnitude'], 
                    color='red', label='Significant Rotations')
        plt.title('Significant Rotations Detection')
        plt.xlabel('Time')
        plt.ylabel('Rotation Magnitude')
        plt.legend()
        plt.grid(True)
        plt.show()

    def analyze_stabilization(self, window_size=10):
        """
        Analyze and plot device stabilization.

        Args:
            window_size (int): The size of the rolling window for calculating the average.
        """
        self.df['rolling_total_rotation'] = self.df['total_rotation'].rolling(window=window_size).mean()
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['total_rotation'], label='Total Rotation', alpha=0.5)
        plt.plot(self.df['timestamp'], self.df['rolling_total_rotation'], label=f'{window_size}-point Rolling Average', color='red')
        plt.title('Device Stabilization Analysis')
        plt.xlabel('Time')
        plt.ylabel('Total Rotation')
        plt.legend()
        plt.grid(True)
        plt.show()

    def run_analysis(self):
        """
        Run all analysis methods and print statistics.
        """
        print("Running Orientation Sensor Analysis...")
        
        self.plot_3d_orientation()
        self.plot_rotation_over_time()
        self.detect_significant_rotations()
        self.analyze_stabilization()
        
        print("\nOrientation Statistics:")
        print(f"Average Rotation Magnitude: {self.df['rotation_magnitude'].mean():.2f}")
        print(f"Maximum Rotation Magnitude: {self.df['rotation_magnitude'].max():.2f}")
        print(f"Minimum Rotation Magnitude: {self.df['rotation_magnitude'].min():.2f}")
        
        print("\nOrientation Sensor Data Analysis Completed!")