from scapy.all import sniff
from datetime import datetime
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Generate a timestamped log filename
log_filename = f"logs/sniffer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def packet_callback(packet):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    proto = packet.name
    src = packet[0].src if hasattr(packet[0], 'src') else 'N/A'
    dst = packet[0].dst if hasattr(packet[0], 'dst') else 'N/A'
    summary = packet.summary()

    log_line = f"[{timestamp}] {proto} | {src} -> {dst} | {summary}"
    print(log_line)

    # Write to timestamped log file
    with open(log_filename, "a", encoding="utf-8") as f:
        f.write(log_line + "\n")

# Sniff for 10 seconds then stop
print("Sniffing packets for 10 seconds...")
sniff(prn=packet_callback, store=False, timeout=10)
print(f"Sniffing complete. Logs saved to: {log_filename}")