from ids_core.notifications.email_notifier import send_email

def analyze_packet(packet):
    # Logic to analyze the packet and determine if it's malicious
    is_malicious = False  # Replace with actual detection logic

    if is_malicious:
        notify_user(packet)

def notify_user(packet):
    recipient_email = "user@example.com"  # Replace with actual recipient email
    subject = "Malicious Packet Detected"
    message = f"A malicious packet was detected: {packet}"
    send_email(recipient_email, subject, message)