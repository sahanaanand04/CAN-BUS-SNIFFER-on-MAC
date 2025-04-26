import can
import logging
import time
import os

# Set up logging
logging.basicConfig(filename='can_bus_simulation.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def send_can_message(bus):
    """Send a CAN message"""
    for i in range(5):  # Send multiple messages for testing
        msg = can.Message(arbitration_id=0x123, data=[0x11, 0x22, 0x33, 0x44], is_extended_id=False)
        try:
            bus.send(msg)
            logging.info(f"Message sent on CAN bus: {msg}")
            print(f"Message sent on CAN bus: {msg}")
            time.sleep(1)  # Wait 1 second between sending messages
        except can.CanError:
            logging.error("Message failed to send")
            print("Message failed to send")

def monitor_can_messages(bus):
    """Monitor CAN messages on the CAN bus"""
    print("Monitoring messages on the CAN bus...")
    while True:
        try:
            message = bus.recv(timeout=10)  # Wait up to 10 seconds for a message
            if message:
                print(f"Received: {message}")
                logging.info(f"Received: {message}")
            else:
                print("No message received within timeout.")
        except KeyboardInterrupt:
            print("Exiting...")
            logging.info("Exiting...")
            break
        except Exception as e:
            print(f"Error occurred: {e}")
            logging.error(f"Error occurred: {e}")

def main():
    # Set up CAN bus using the USB-to-CAN adapter (e.g., socketcan interface)
    try:
        bus = can.Bus(interface='usbcan', channel='0', bitrate=500000)
    except can.CanError:
        print("Failed to initialize CAN bus")
        return

    # Send messages
    send_can_message(bus)

    # Monitor for incoming messages
    monitor_can_messages(bus)

    # Cleanup after exiting
    bus.shutdown()

if __name__ == "__main__":
    main()
