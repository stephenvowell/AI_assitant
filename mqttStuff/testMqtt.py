import socket

def check_mqtt_broker(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)  # 5 seconds timeout
    try:
        sock.connect((ip, port))
    except socket.error as e:
        print(f"Connection to {ip}:{port} failed: {e}")
        return False
    else:
        print(f"Connection to {ip}:{port} succeeded")
        return True
    finally:
        sock.close()

# Check the MQTT broker
check_mqtt_broker('192.168.1.19', 9001)