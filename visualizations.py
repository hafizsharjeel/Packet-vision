import matplotlib.pyplot as plt
import pandas as pd

def plot_packet_count(df):
    """Plot the count of packets per protocol."""
    try:
        protocol_counts = df["Protocol"].value_counts()
        fig, ax = plt.subplots()
        protocol_counts.plot(kind="bar", ax=ax, color="skyblue")
        ax.set_title("Packet Count by Protocol")
        ax.set_xlabel("Protocol")
        ax.set_ylabel("Count")
        return fig
    except Exception as e:
        print(f"Error generating packet count plot: {e}")
        return None

def visualize_traffic(df):
    """Visualize traffic over time."""
    try:
        df["Time"] = pd.to_datetime(df["Time"])
        df.set_index("Time", inplace=True)
        fig, ax = plt.subplots()
        df["Length"].plot(ax=ax, kind="line", color="green", legend=True)
        ax.set_title("Traffic Over Time")
        ax.set_xlabel("Time")
        ax.set_ylabel("Packet Length")
        return fig
    except Exception as e:
        print(f"Error generating traffic visualization: {e}")
        return None
