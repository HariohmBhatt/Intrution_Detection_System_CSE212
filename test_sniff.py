from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        print(f"Packet: {packet.summary()}")

print("Starting packet capture... (press Ctrl+C to stop)")
try:
    # Use store=False to avoid memory issues with many packets
    sniff(iface="wlp0s20f3", prn=packet_callback, store=False)
except KeyboardInterrupt:
    print("Stopped packet capture")