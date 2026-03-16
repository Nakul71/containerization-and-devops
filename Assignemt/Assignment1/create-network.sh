#!/bin/bash
# ─────────────────────────────────────────────────────────────
# Macvlan Network Creation Script
# ─────────────────────────────────────────────────────────────
#
# This script creates a macvlan Docker network that allows
# containers to appear as physical devices on the LAN.
#
# IMPORTANT: Adjust the following values to match YOUR network:
#   - subnet:  Your LAN subnet (e.g., 192.168.1.0/24)
#   - gateway: Your router/gateway IP (e.g., 192.168.1.1)
#   - ip-range: Range of IPs reserved for containers
#   - parent:  Your host's network interface (eth0, ens33, etc.)
#
# To find your interface name, run:
#   Linux:   ip link show
#   Windows: Get-NetAdapter (in PowerShell)
# ─────────────────────────────────────────────────────────────

# Remove existing network if it exists
docker network rm app_macvlan 2>/dev/null

# Create macvlan network
docker network create -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  --ip-range=192.168.1.48/28 \
  -o parent=eth0 \
  app_macvlan

echo ""
echo "Macvlan network 'app_macvlan' created successfully!"
echo ""
echo "Network details:"
docker network inspect app_macvlan --format '{{.Name}} | Driver: {{.Driver}} | Subnet: {{range .IPAM.Config}}{{.Subnet}}{{end}}'
echo ""
echo "Container IPs will be assigned from the 192.168.1.48/28 range"
echo "  - Database (student-db):  192.168.1.50"
echo "  - Backend  (student-api): 192.168.1.51"
echo ""
echo "NOTE (Host Isolation): With macvlan, the host machine"
echo "  CANNOT directly communicate with the containers using"
echo "  their macvlan IPs. This is a known Linux kernel limitation."
echo "  To reach containers from the host, create a macvlan"
echo "  sub-interface on the host:"
echo ""
echo "  sudo ip link add macvlan-shim link eth0 type macvlan mode bridge"
echo "  sudo ip addr add 192.168.1.49/32 dev macvlan-shim"
echo "  sudo ip link set macvlan-shim up"
echo "  sudo ip route add 192.168.1.48/28 dev macvlan-shim"
