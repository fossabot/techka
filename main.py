# main.py

from techka.cli.logo import logo
from techka.cli.cli_handler import CliHandler

def main():
    print(logo())
    cli_handler = CliHandler()
    cli_handler.execute()

if __name__ == "__main__":
    main()