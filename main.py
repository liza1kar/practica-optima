import argparse
from log_parser import parse_logs
from smtp_notifier import send_notification
from error_database import save_errors

def main():
    parser = argparse.ArgumentParser(description="Log Monitoring Service")
    parser.add_argument("--log", required=True, help="Path to the log file")
    parser.add_argument("--email", required=True, help="Recipient email for notifications")
    args = parser.parse_args()

    log_file_path = args.log
    recipient_email = args.email

    errors = parse_logs(log_file_path)
    if errors:
        send_notification(recipient_email, errors)
        save_errors(errors)
        print(f"Found {len(errors)} errors. Notification sent to {recipient_email}.")
    else:
        print("No errors found.")

if __name__ == "__main__":
    main()