import argparse
from packet_capturer import capture_packets, save_packets, packets_to_dataframe
from visualizations import plot_packet_count, visualize_traffic

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
        packets = capture_packets(interface=args.interface, count=args.count)
        print(f"Captured {len(packets)} packets.")
        if args.output:
            save_packets(packets, args.output)
            print(f"Packets saved to {args.output}.")

    if args.analyze:
        if not args.input:
            print("Error: --input is required for analysis.")
            return
        # Load and analyze packets here...

if __name__ == "__main__":
    main()
