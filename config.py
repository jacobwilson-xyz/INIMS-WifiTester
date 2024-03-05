import platform

# Webhook URL for POST Requests
webhookURL = "WebhookURL"
# Network SSID - Set automatically
ssid = "UniOfCam-IoT"
# Physical Building Location
location = "Room X00"
# Test Mode - Triggers a speedtest on boot
testMode = False
# Device Name
deviceName = "Unset"
# Device OS Name, 'Linux' or 'Windows' supported.
# systemPlatform = "Linux"
systemPlatform = platform.system()
# Which wlan to use for testing - For Linux
wlan = "wlan1"
# Display IP on startup for SSH Purposes (Linux).
displayDeviceIP = False
encodeDeviceIP = False
# Random UUID each session for better tracking of mutliple devices
uniqueIdentifer = str(uuid.uuid4())[:4]
