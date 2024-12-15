import re

def parse_logs(log_file_path):
    """
    Function to parse the log file and search for errors.

    Args:
        log_file_path (str): Path to the log file.

    Returns:
        list: List of lines with found errors.
    """
    errors = []
    with open(log_file_path, "r") as file:
        for line in file:
            if re.search(r"(error|critical|failed)", line, re.IGNORECASE):
                errors.append(line.strip())
    return errors