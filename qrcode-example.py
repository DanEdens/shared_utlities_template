# Import the necessary modules
import qrcode

def generate_wifi_qr_code(ssid, security_type, password):
  # Create a QR code object
  qr = qrcode.QRCode()

  # Add the WiFi network's information to the QR code object
  qr.add_data(f"WIFI:S:{ssid};T:{security_type};P:{password};;")
  qr.make()

  # Return the generated QR code as an image
  return qr.make_image()

# Example usage
img = generate_wifi_qr_code("My WiFi Network", "WPA", "mywifipassword")
img.save("wifi-qr-code.png")
