import argparse
from packet_capturer import capture_packets, save_packets, packets_to_dataframe
from visualizations import plot_packet_count, visualize_traffic
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description="Packet Vision CLI")
    parser.add_argument("--capture", action="store_true", help="Capture live packets")
    parser.add_argument("--analyze", action="store_true", help="Analyze a .pcap file")
    parser.add_argument("--interface", type=str, help="Network interface for live capture")
    parser.add_argument("--count", type=int, default=100, help="Number of packets to capture")
    parser.add_argument("--output", type=str, help="File to save captured packets")
    parser.add_argument("--input", type=str, help="Input .pcap file for analysis")

    args = parser.parse_args()

    if args.capture:
        if not args.interface:
            print("Error: --interface is required for live capture.")
            return
        try:
            packets = capture_packets(interface=args.interface, count=args.count)
            print(f"Captured {len(packets)} packets.")
            if args.output:
                save_packets(packets, args.output)
                print(f"Packets saved to {args.output}.")
            else:
                print("Packets not saved. Use --output to specify a file.")
        except Exception as e:
            print(f"Error during packet capture: {e}")

    if args.analyze:
        if not args.input:
            print("Error: --input is required for analysis.")
            return
        try:
            df = packets_to_dataframe(args.input)
            print("Packets loaded successfully.")
            print(df.head())  # Display the first few rows of the DataFrame
            
            # Visualization
            print("Generating visualizations...")
            fig1 = plot_packet_count(df)
            fig2 = visualize_traffic(df)
            
            # Save visualizations as images
            fig1.savefig("protocol_count.png")
            fig2.savefig("traffic_over_time.png")
            print("Visualizations saved: protocol_count.png, traffic_over_time.png.")
            
            plt.show()
        except Exception as e:
            print(f"Error during packet analysis: {e}")

if __name__ == "__main__":
    main()
