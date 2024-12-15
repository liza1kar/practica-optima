# Log Monitoring Service

## Description
A console-based Python application that monitors system log files, detects errors, and sends email notifications.

## Features
- Parse log files for errors (error, critical, failed).
- Send email notifications using SMTP.
- Save detected errors to an SQLite database.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd log_monitoring_project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Update the `config.json` file with your SMTP settings.

## Usage

```bash
python main.py --log /path/to/logfile.log --email recipient@example.com
```

## License
MIT License
