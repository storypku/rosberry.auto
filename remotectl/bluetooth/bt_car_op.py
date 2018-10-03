# Uses Bluez for Linux
#
# sudo apt-get install bluez python-bluez
#
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/x232.html
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/c212.html
import time
import bluetooth


if __name__ == "__main__":
    port = 1
    target_bt = "00:1A:7D:DA:71:11"

    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((target_bt, port))
        while True:
            char = raw_input("Please input a character (q/Q for exit): ")
            print(char)
            if char == 'q' or char == 'Q':
                break
            sock.send(char)
    except KeyboardInterrupt:
        print("Ctrl-C entered, exiting...")
    except Exception as e:
        print ("Exception caught: {}".format(e))
    finally:
        sock.close()
    print("Done")
