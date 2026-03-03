from datetime import datetime

class HRStaffAnalyzer:
    def __init__(self):
        self.current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        self.current_user = 'mantha88'

    def run(self):
        self.display_welcome_message()

    def display_welcome_message(self):
        print(f'Current Date and Time (UTC): {self.current_time}')
        print(f'Current User\'s Login: {self.current_user}')

if __name__ == '__main__':
    analyzer = HRStaffAnalyzer()
    analyzer.run()