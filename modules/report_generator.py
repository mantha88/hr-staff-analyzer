# Report Generator Module

"""
This module provides functions to generate text reports in a human-readable format.
"""

from datetime import datetime


def generate_report(data):
    """
    Generates a text report based on provided data.

    Parameters:
    data (dict): A dictionary containing the report data.

    Returns:
    str: A formatted report string.
    """
    report = []
    report.append(f"Report generated on: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    report.append('')

    for key, value in data.items():
        report.append(f'{key}: {value}')

    return '\n'.join(report)


if __name__ == '__main__':
    # Example usage
    sample_data = {
        'Title': 'Monthly Staff Performance',
        'Total Staff': 50,
        'Staff Present': 45,
        'Reports Submitted': 40
    }
    print(generate_report(sample_data))
