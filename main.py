from pathlib import Path
from statistics.console_register import ConsoleRegister

if __name__ == '__main__':
    file_path = Path(__file__).parent / 'files'
    console_register = ConsoleRegister(file_path)
    console_register.show_menu()
