def generate_report(data):
    """Generates a text-based report from the provided data.
    
    Args:
        data (dict): A dictionary containing report data.
    
    Returns:
        str: A formatted text report.
    """
    report_lines = []
    for key, value in data.items():
        report_lines.append(f"{key}: {value}")
    return '\n'.join(report_lines)


def save_report_to_file(report, file_path):
    """Saves the generated report to a text file.
    
    Args:
        report (str): The report to save.
        file_path (str): The file path where the report will be saved.
    """
    with open(file_path, 'w') as file:
        file.write(report)