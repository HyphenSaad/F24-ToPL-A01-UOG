import pandas as pd
import matplotlib.pyplot as plt

class PressureAnalyzer:
    """
    A class to analyze pressure sensor data from a CSV file.

    Attributes:
        df (pandas.DataFrame): The dataframe containing the pressure sensor data.

    Methods:
        plot_pressure_over_time(): Plot the pressure over time.
        plot_altitude_over_time(): Plot the estimated altitude over time.
        analyze_weather_patterns(): Analyze and plot weather patterns.
        run_analysis(): Run all analysis methods and print statistics.
    """

    def __init__(self, csv_file_path: str):
        """
        Initialize the PressureAnalyzer object.

        Args:
            csv_file_path (str): Path to the CSV file containing pressure sensor data.
        """
        self.df = pd.read_csv(csv_file_path)
        self.df['timestamp'] = pd.to_datetime(self.df['index'], unit='s')

    def plot_pressure_over_time(self):
        """
        Plot the pressure over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['pres'])
        plt.title('Pressure Over Time')
        plt.xlabel('Time')
        plt.ylabel('Pressure (hPa)')
        plt.grid(True)
        plt.show()

    def plot_altitude_over_time(self):
        """
        Plot the estimated altitude over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['estimated_altitude'])
        plt.title('Estimated Altitude Over Time')
        plt.xlabel('Time')
        plt.ylabel('Altitude (m)')
        plt.grid(True)
        plt.show()

    def analyze_weather_patterns(self):
        """
        Analyze and plot weather patterns.
        """
        # calculated pressure changes
        self.df['pressure_change'] = self.df['pres'].diff()

        # plotted pressure changes
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['pressure_change'])
        plt.title('Pressure Changes Over Time')
        plt.xlabel('Time')
        plt.ylabel('Pressure Change (hPa)')
        plt.grid(True)
        plt.show()

        # identified significant pressure changes
        significant_change = 1.0  # hPa
        significant_changes = self.df[abs(self.df['pressure_change']) > significant_change]
        
        print("Significant Pressure Changes:")
        for _, row in significant_changes.iterrows():
            print(f"Time: {row['timestamp']}, Change: {row['pressure_change']:.2f} hPa")

    def run_analysis(self):
        """
        Run all analysis methods and print statistics.
        """
        print("Running Pressure Sensor Analysis...")
        
        # plotted pressure over time
        self.plot_pressure_over_time()
        
        # plotted estimated altitude over time
        self.plot_altitude_over_time()
        
        # analyzed weather patterns
        self.analyze_weather_patterns()
        
        # printed some interesting statistics
        print("\nPressure Statistics:")
        print(f"Average Pressure: {self.df['pres'].mean():.2f} hPa")
        print(f"Max Pressure: {self.df['pres'].max():.2f} hPa")
        print(f"Min Pressure: {self.df['pres'].min():.2f} hPa")
        
        print("\nAltitude Statistics:")
        print(f"Average Estimated Altitude: {self.df['estimated_altitude'].mean():.2f} m")
        print(f"Max Estimated Altitude: {self.df['estimated_altitude'].max():.2f} m")
        print(f"Min Estimated Altitude: {self.df['estimated_altitude'].min():.2f} m")

        print("\nPressure Sensor Data Analysis Completed!")