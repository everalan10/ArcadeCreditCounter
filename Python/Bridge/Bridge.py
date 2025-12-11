import serial
import time
import os

SERIAL_PORT = "COM3"
BAUDRATE = 9600
FILE_NAME = "credit.txt"

def write_credit(credit):
    texto = f"CREDIT {credit:03d}"  # CREDIT 001, 002, etc.
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write(texto)
    print("Updating:", texto)

def main():
    credit = 0

    print(f"Conectando a {SERIAL_PORT}...")
    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)

    # Wait for Arduino to reset.
    time.sleep(2)

    # Initialize credit file
    write_credit(credit)

    print("Listening for signals... Press Ctrl+C to exit.")
    try:
        while True:
            line = ser.readline().decode(errors="ignore").strip()
            if line == "1":
                credit += 1
                write_credit(credit)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        ser.close()

if __name__ == "__main__":
    main()
