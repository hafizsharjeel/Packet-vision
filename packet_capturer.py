from scapy.all import sniff, wrpcap
import pandas as pd

# List to store captured packets
packets_list = []

def packet_handler(packet):
    """Callback function to handle each captured packet."""
    global packets_list
    packets_list.append(packet)
    print(packet.summary())  # Print a summary for live updates

def capture_packets(interface="eth0", count=100):
    """Capture packets from the specified interface."""
    global packets_list
    packets_list = []  # Clear previous packets
    sniff(iface=interface, prn=packet_handler, count=count, store=True)
    return packets_list

def save_packets(filename="captured_packets.pcap"):
    """Save captured packets to a file."""
    if packets_list:
        wrpcap(filename, packets_list)
        return filename
    else:
        raise ValueError("No packets to save!")

def packets_to_dataframe(packets):
    data = []
    for packet in packets:
        # Extract transport layer protocol if available
        protocol = None
        if packet.haslayer("IP"):
            protocol = packet["IP"].proto  # Extract protocol number
            protocol_map = {6: "TCP", 17: "UDP", 1: "ICMP"}
            protocol = protocol_map.get(protocol, "Other")  # Map number to protocol name

        # Add packet details to the data list
        data.append({
            "Time": packet.time,
            "Source": packet[0][1].src if hasattr(packet[0][1], "src") else "N/A",
            "Destination": packet[0][1].dst if hasattr(packet[0][1], "dst") else "N/A",
            "Protocol": protocol if protocol else packet[0].name,
            "Length": len(packet),
        })

    return pd.DataFrame(data)

