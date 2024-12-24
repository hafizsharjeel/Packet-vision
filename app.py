import streamlit as st
from scapy.all import sniff, get_if_list
import psutil
import pandas as pd
import matplotlib.pyplot as plt

from packet_capturer import capture_packets, save_packets, packets_to_dataframe
from visualizations import plot_packet_count, visualize_traffic

# Set up page config
st.set_page_config(
    page_title="Packet Vision",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Navigation Options
pages = ["Packet Vision", "About"]
selected_page = st.sidebar.radio("Navigation", pages)

if selected_page == "About":
    st.title("About Packet Vision")

    st.subheader("About me")
    st.write(
        "Hi, I’m Hafiz Sharjeel Shakeel, a Cybersecurity Penetration Tester and Ethical Hacker with a passion for creating secure tools and exploring advanced network traffic analysis techniques. This tool is designed to capture and analyze real-time network traffic, providing insights into packet-level communications for penetration testing, network security assessments, and advanced traffic visualization."
    
    )

    st.subheader("Introduction")
    st.write(
        "Packet Vision is a powerful tool designed to monitor and analyze network traffic in real-time. "
        "It is ideal for cybersecurity enthusiasts, penetration testers, and network administrators. "
        "This tool allows you to capture packets, visualize traffic trends, and gain insights into protocol-level communications."
    )

    st.subheader("How to Use")
    st.write("1. Select the 'Packet Vision' page from the sidebar.")
    st.write("2. Choose a network interface from the available list.")
    st.write("3. Adjust the slider to set the number of packets you want to capture.")
    st.write("4. Click 'Start Capture' to begin monitoring network traffic.")
    st.write("5. View captured packets in a table and visualize network activity using graphs.")
    st.write("6. Optionally, save captured packets to a file for later analysis.")

    st.subheader("Techniques Used")
    st.write("- **Packet Sniffing**: The tool uses Scapy to capture network packets directly from the selected interface.")
    st.write("- **Data Processing**: Captured packets are processed and displayed in tabular format using Pandas.")
    st.write("- **Visualization**: Matplotlib and Seaborn are used for creating visualizations of network traffic trends.")
    st.write("- **Real-Time Monitoring**: Psutil monitors network interface activity, providing live statistics.")

    st.subheader("Key Features")
    st.write("- Real-time packet capture and display.")
    st.write("- Protocol analysis to differentiate between TCP, UDP, and other protocols.")
    st.write("- Visual representation of traffic patterns over time.")
    st.write("- Option to save captured packets in PCAP format for further analysis in tools like Wireshark.")

else:
    # Packet Vision Page
    st.title("Packet Vision")


# Sidebar for Options
st.sidebar.header("Options")
st.sidebar.write("Monitor network activity and capture packets.")

# Get available interfaces
interfaces = get_if_list()
if not interfaces:
    st.error("No network interfaces found! Please check your network settings.")
else:
    # Network Activity Monitoring
    def get_interface_stats():
        """Retrieve real-time network stats for all interfaces."""
        stats = {}
        for interface in interfaces:
            counters = psutil.net_io_counters(pernic=True).get(interface)
            if counters:
                stats[interface] = {
                    "Packets Sent": counters.packets_sent,
                    "Packets Received": counters.packets_recv,
                    "Bytes Sent": counters.bytes_sent,
                    "Bytes Received": counters.bytes_recv,
                }
        return stats

    # Display network activity
    st.sidebar.subheader("Network Interface Activity")
    interface_stats = get_interface_stats()

    # Table of network stats
    stats_df = pd.DataFrame.from_dict(interface_stats, orient="index")
    if not stats_df.empty:
        st.sidebar.dataframe(stats_df)

    # Allow user to select an interface
    interface = st.sidebar.selectbox(
        "Select Network Interface (Based on Activity):", list(interface_stats.keys())
    )

    # User input for packet capture
    packet_count = st.sidebar.slider("Number of Packets to Capture:", 10, 500, 100)

    # Start Capture Button
    if st.sidebar.button("Start Capture"):
        with st.spinner("Capturing packets..."):
            try:
                # Capture packets
                packets = capture_packets(interface=interface, count=packet_count)
                st.success(f"Captured {len(packets)} packets!")
                df = packets_to_dataframe(packets)

                # Display packets as a table
                st.subheader("Captured Packets")
                if not df.empty:
                    st.dataframe(df)
                else:
                    st.warning("No packets captured.")

                # Visualize packet traffic
                if not df.empty:
                    st.subheader("Packet Traffic Visualization")
                    st.pyplot(plot_packet_count(df))
                    st.pyplot(visualize_traffic(df))

                # Save packets to file
                if st.button("Save Packets to File"):
                    file_path = save_packets(packets)
                    st.success(f"Packets saved to {file_path}!")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # Realtime Visualization
    st.subheader("Live Network Activity")
    if not stats_df.empty and "Packets Sent" in stats_df.columns and "Packets Received" in stats_df.columns:
        st.line_chart(stats_df[["Packets Sent", "Packets Received"]])
    else:
        st.warning("No data available for live network activity visualization.")
