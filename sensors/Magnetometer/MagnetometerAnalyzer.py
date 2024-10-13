import math
import pandas as pd
import matplotlib.pyplot as plt

class MagnetometerAnalyzer:
    """
    A class to analyze magnetometer data from a CSV file.
    """

    def __init__(self, csv_file_path: str):
        """
        Initialize the MagnetometerAnalyzer object.

        Args:
            csv_file_path (str): Path to the CSV file containing magnetometer data.
        """
        self.df = pd.read_csv(csv_file_path)
        self.df['timestamp'] = pd.to_datetime(self.df['index'], unit='s')

    def plot_magnetic_field_over_time(self):
        """
        Plot the magnetic field magnitude over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['magnitude'])
        plt.title('Magnetic Field Magnitude Over Time')
        plt.xlabel('Time')
        plt.ylabel('Magnitude (μT)')
        plt.grid(True)
        plt.show()

    def plot_compass_heading(self):
        """
        Plot the compass heading in a polar plot.
        """
        plt.figure(figsize=(8, 8))
        plt.polar(self.df['heading'] * math.pi / 180, self.df['magnitude'])
        plt.title('Compass Heading')
        plt.show()

    def detect_magnetic_anomalies(self, threshold: float = 2.0) -> pd.DataFrame:
        """
        Detect magnetic anomalies in the data.

        Args:
            threshold (float): The number of standard deviations to use as the anomaly threshold.

        Returns:
            pd.DataFrame: A DataFrame containing the detected anomalies.
        """
        mean = self.df['magnitude'].mean()
        std = self.df['magnitude'].std()
        return self.df[abs(self.df['magnitude'] - mean) > threshold * std]

    def run_analysis(self):
        """
        Run a comprehensive analysis of the magnetometer data.
        """
        print("Running Magnetometer Analysis...")
        
        # plotted magnetic field over time
        self.plot_magnetic_field_over_time()
        
        # plotted compass heading
        self.plot_compass_heading()
        
        # detected magnetic anomalies
        anomalies = self.detect_magnetic_anomalies()
        print(f"Number of detected magnetic anomalies: {len(anomalies)}")
        if not anomalies.empty:
            print("Anomaly times:")
            for _, anomaly in anomalies.iterrows():
                print(f"  {anomaly['timestamp']}: Magnitude = {anomaly['magnitude']:.2f} μT")

        # calculated and printed statistics
        print("\nMagnetometer Statistics:")
        print(f"Average Magnetic Field Magnitude: {self.df['magnitude'].mean():.2f} μT")
        print(f"Maximum Magnetic Field Magnitude: {self.df['magnitude'].max():.2f} μT")
        print(f"Minimum Magnetic Field Magnitude: {self.df['magnitude'].min():.2f} μT")
        
        # analyzed compass heading
        heading_stats = self.df['heading'].describe()
        print(f"\nCompass Heading Statistics:")
        print(f"Mean Heading: {heading_stats['mean']:.2f}°")
        print(f"Median Heading: {heading_stats['50%']:.2f}°")
        
        print("\nMagnetometer Data Analysis Completed!")