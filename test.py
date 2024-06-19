import spidev

# Initialize SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device (CS) 0

# Set SPI speed and mode
spi.max_speed_hz = 1_000_000
spi.mode = 0

# Function to write and read data
def spi_write_read(data_to_send):
    # Write data to SPI and read the response
    response = spi.xfer(data_to_send)
    return response

# Test data
data = [0x00, 0x00, 0x00, 0x00, 0x00]
#data = [0x04, 0x00]

# Send and receive data
print("Sending data:", data)
response = spi_write_read(data)[::-1]
print("Received data:", end="")
for i in bytearray(response):
    print(f" {hex(i)} ", end="")
print()

# Close SPI connection
spi.close()