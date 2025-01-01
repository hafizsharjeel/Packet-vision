import pyshark
import pandas as pd

def capture_packets(interface, count):
    """Capture packets synchronously using PyShark."""
    try:
        capture = pyshark.LiveCapture(interface=interface)
        packets = []
        for i, packet in enumerate(capture.sniff_continuously(packet_count=count)):
            packets.append(packet)
        return packets
    except Exception as e:
        raise ValueError(f"Error during packet capture: {e}")

def save_packets(packets, filename="captured_packets.pcap"):
    """Save packets to a file."""
    try:
        with open(filename, "wb") as file:
            for packet in packets:
                file.write(bytes(packet))
        return filename
    except Exception as e:
        raise ValueError(f"Error saving packets: {e}")

def packets_to_dataframe(packets):
    """Convert packets to a DataFrame."""
    data = []
    for packet in packets:
        try:
            data.append({
                "Time": packet.sniff_time,
                "Source": packet.ip.src if hasattr(packet, "ip") else "N/A",
                "Destination": packet.ip.dst if hasattr(packet, "ip") else "N/A",
                "Protocol": packet.highest_layer,
                "Length": packet.length,
            })
        except AttributeError:
            continue
    return pd.DataFrame(data)
