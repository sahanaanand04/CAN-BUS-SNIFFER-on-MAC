#CAN Bus Sniffer for STM32

This project demonstrates how to interface an STM32 microcontroller with a CAN bus and implement a simple CAN bus sniffer. It provides code to capture CAN frames and interact with the bus using an STM32 device.

#Project Overview

The project consists of two parts:

1. STM32 CAN Sniffer Firmware: Code running on the STM32 microcontroller that reads and sends CAN frames.
2. CAN Bus Simulator: A Python script that simulates the sending and receiving of CAN messages on a virtual CAN interface (vcan0), which you can adapt for a physical CAN setup or a USB-to-CAN adapter.

#Table of Contents

1.Prerequisites
2.Setup Instructions
3.Project Structure
4.STM32 Firmware
5.Python CAN Simulator
6.Usage
7.Troubleshooting

#Prerequisites

#1. Hardware

- STM32 Development Board (e.g., STM32F407)
- USB-to-CAN Adapter or a CAN Transceiver (e.g., MCP2551)
- ST-Link Programmer/Debugger for flashing the STM32

#2. Software

- STM32CubeIDE, STMCube programmer, STMCube MX for STM32 development and flashing.
- OpenOCD for debugging.
- Python 3.x for CAN Bus simulation.
- python-can library to interface with CAN buses in Python.
- SocketCAN if using a Linux-based environment with virtual CAN interfaces.(vortual machine on mac)

#Installing Required Python Packages
pip install python-can or pip install python-can[peakcan]

#Setup Instructions

Step 1: STM32 Firmware Setup
Step 2: CAN Bus Simulation with Python
Step 3: Debugging and Flashing STM32
Step 4: Monitor CAN Traffic(python program)

#Project Structure

 CAN-Bus-Sniffer/

 ├── STM32_Firmware/
 
 │   ├── CANSniffer/
 
 │   │   ├── Src/
 
 │   │   ├── Inc/
 
 │   │   ├── CANSniffer.elf
 
 │   │   └── CANSniffer.bin

 ├── can_simulation.py

 └── README.md
