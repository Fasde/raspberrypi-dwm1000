import spidev
import time

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)  # (bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 300_000
spi.mode = 0

def send_spi_data(data):
    resp = spi.xfer(data)
    return resp

try:
    while True:
        data_to_send = [0x00] * 8  # Example data
        print(f"Sent: {data_to_send} |", end="")
        response = send_spi_data(data_to_send)
        print(f"Received: {response}")
        time.sleep(1)
except KeyboardInterrupt:
    spi.close()
