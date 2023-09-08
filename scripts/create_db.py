import sys
import os.path

parent = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent)

from models.event import Event


def main():
    Event.create_table(if_not_exists=True).run_sync()


if __name__ == "__main__":
    main()
