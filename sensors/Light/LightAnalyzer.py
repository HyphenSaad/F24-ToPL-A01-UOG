import pandas as pd
import matplotlib.pyplot as plt

class LightAnalyzer:
    """
    A class to analyze light sensor data from a CSV file.

    Attributes:
        df (pd.DataFrame): DataFrame containing the light sensor data.

    Methods:
        plot_light_over_time(): Plot light intensity over time.
        plot_day_night_detection(): Plot day/night detection over time.
        analyze_light_patterns(): Analyze and plot light intensity patterns.
        run_analysis(): Run all analysis methods and print statistics.
    """

    def __init__(self, csv_file_path: str):
        """
        Initialize the LightAnalyzer with data from a CSV file.

        Args:
            csv_file_path (str): Path to the CSV file containing light sensor data.
        """
        self.df = pd.read_csv(csv_file_path)
        self.df['timestamp'] = pd.to_datetime(self.df['index'], unit='s')

    def plot_light_over_time(self):
        """
        Plot light intensity over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['light'])
        plt.title('Ambient Light Levels Over Time')
        plt.xlabel('Time')
        plt.ylabel('Light Intensity')
        plt.grid(True)
        plt.show()

    def plot_day_night_detection(self):
        """
        Plot day/night detection over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['light'], color='gray', alpha=0.5)
        plt.fill_between(self.df['timestamp'], self.df['light'], where=self.df['day_night'] == 'Day', color='yellow', alpha=0.3, label='Day')
        plt.fill_between(self.df['timestamp'], self.df['light'], where=self.df['day_night'] == 'Night', color='blue', alpha=0.3, label='Night')
        plt.title('Day/Night Detection')
        plt.xlabel('Time')
        plt.ylabel('Light Intensity')
        plt.legend()
        plt.grid(True)
        plt.show()

    def analyze_light_patterns(self):
        """
        Analyze and plot light intensity patterns.
        """
        # calculated rolling average
        window_size = 10  # Adjust as needed
        self.df['rolling_avg'] = self.df['light'].rolling(window=window_size).mean()

        # plotted rolling average
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['light'], label='Raw Light')
        plt.plot(self.df['timestamp'], self.df['rolling_avg'], label=f'{window_size}-point Rolling Average', color='red')
        plt.title('Light Intensity Patterns')
        plt.xlabel('Time')
        plt.ylabel('Light Intensity')
        plt.legend()
        plt.grid(True)
        plt.show()

    def run_analysis(self):
        """
        Run all analysis methods and print statistics.
        """
        print("Running Light Sensor Analysis...")
        
        self.plot_light_over_time()
        self.plot_day_night_detection()
        self.analyze_light_patterns()
        
        print("\nLight Statistics:")
        print(f"Average Light Intensity: {self.df['light'].mean():.2f}")
        print(f"Maximum Light Intensity: {self.df['light'].max():.2f}")
        print(f"Minimum Light Intensity: {self.df['light'].min():.2f}")
        
        day_count = (self.df['day_night'] == 'Day').sum()
        night_count = (self.df['day_night'] == 'Night').sum()
        print(f"\nDay/Night Distribution:")
        print(f"Day: {day_count} samples ({day_count/len(self.df)*100:.2f}%)")
        print(f"Night: {night_count} samples ({night_count/len(self.df)*100:.2f}%)")

        print("\nLight Sensor Data Analysis Completed!")