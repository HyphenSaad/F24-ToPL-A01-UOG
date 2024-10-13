from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
from .GNSS_GPS_Calculator import GNSS_GPS_Calculator

class GNSS_GPS_Analyzer:
    """
    A class to analyze GNSS/GPS data from a CSV file.
    """

    def __init__(self, csv_file_path: str):
        """
        Initialize the GNSS_GPS_Analyzer object.

        Args:
            csv_file_path (str): Path to the CSV file containing GPS data.
        """
        self.df = pd.read_csv(csv_file_path)
        self.df['timestamp'] = pd.to_datetime(self.df['index'], unit='s')
        self.df['total_speed'] = self.df.apply(lambda row: GNSS_GPS_Calculator.calculate_total_speed(row['speed'], row['bearing']), axis=1)
        
        self.df['distance'] = self.df.apply(lambda row: GNSS_GPS_Calculator.calculate_distance(
            row['latit'], row['long'],
            self.df.iloc[0]['latit'], self.df.iloc[0]['long']
        ), axis=1)

    def plot_location_tracking(self):
        """
        Plot the GPS location tracking on a map.
        """
        # calculated center latitude and longitude
        center_lat = self.df['latit'].mean()
        center_lon = self.df['long'].mean()
        m = folium.Map(location=[center_lat, center_lon], zoom_start=13)

        # added markers for start and end points
        folium.Marker([self.df['latit'].iloc[0], self.df['long'].iloc[0]], popup='Start').add_to(m)
        folium.Marker([self.df['latit'].iloc[-1], self.df['long'].iloc[-1]], popup='End').add_to(m)

        # created a list of [lat, lon] pairs
        locations = self.df[['latit', 'long']].values.tolist()

        # added a heatmap layer
        HeatMap(locations).add_to(m)

        # added a polyline to show the exact path
        folium.PolyLine(locations, color="red", weight=2.5, opacity=1).add_to(m)

        # saved the map
        filename = f'gps_location_tracking_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
        m.save(filename)
        print(f"Map Saved As '{filename}'. Open This File in a Web Browser to View the Map.")

    def plot_altitude_changes(self):
        """
        Plot altitude changes over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['altitude'])
        plt.title('Altitude Changes Over Time')
        plt.xlabel('Time')
        plt.ylabel('Altitude (m)')
        plt.grid(True)
        plt.show()

    def plot_3d_movement(self):
        """
        Plot 3D movement visualization.
        """
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        scatter = ax.scatter(self.df['long'], self.df['latit'], self.df['altitude'], c=self.df['timestamp'], cmap='viridis')
        plt.colorbar(scatter, label='Time')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.set_zlabel('Altitude (m)')
        plt.title('3D Movement Visualization')
        plt.show()

    def plot_speed_distribution(self):
        """
        Plot speed distribution.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(self.df['speed'], kde=True)
        plt.title('Speed Distribution')
        plt.xlabel('Speed (m/s)')
        plt.ylabel('Frequency')
        plt.show()

    def plot_satellites_usage(self):
        """
        Plot satellite usage over time.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['timestamp'], self.df['sat_in_view'], label='Satellites in View')
        plt.plot(self.df['timestamp'], self.df['sat_in_use'], label='Satellites in Use')
        plt.title('Satellite Usage Over Time')
        plt.xlabel('Time')
        plt.ylabel('Number of Satellites')
        plt.legend()
        plt.grid(True)
        plt.show()

    def run_analysis(self):
        """
        Run a comprehensive analysis of the GPS data.
        """
        print("Running GPS Data Analysis...")
        
        self.plot_location_tracking()
        self.plot_altitude_changes()
        self.plot_3d_movement()
        self.plot_speed_distribution()
        self.plot_satellites_usage()
        
        print("\nGPS Statistics:")
        print(f"Total Distance Traveled: {self.df['distance'].iloc[-1]:.2f} meters")
        print(f"Average Speed: {self.df['speed'].mean():.2f} m/s")
        print(f"Maximum Speed: {self.df['speed'].max():.2f} m/s")
        print(f"Average Altitude: {self.df['altitude'].mean():.2f} meters")
        print(f"Altitude Range: {self.df['altitude'].max() - self.df['altitude'].min():.2f} meters")
        print(f"Average Satellites in Use: {self.df['sat_in_use'].mean():.2f}")
        
        print("\nGPS Data Analysis Completed!")