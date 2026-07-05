"""Week 2 Lab 4 starter: diary program.

Copy this file into your Week 2 working folder and save it as `diary.py`.
Complete the TODO sections.
"""

DIARY_FILE = "diary.txt"


def read_previous_entries():
    """Return the previous diary entries, or an empty string if there are none."""
    # TODO: use try/except FileNotFoundError and return the file contents.
    raise NotImplementedError("Complete read_previous_entries")


def add_entry(entry):
    """Append one entry to the diary file."""
    # TODO: open DIARY_FILE in append mode and write the entry plus a newline.
    raise NotImplementedError("Complete add_entry")


def main():
    previous_entries = read_previous_entries()

    if previous_entries:
        print("Previous entries:")
        print(previous_entries)
    else:
        print("No diary entries yet.")

    entry = input("Write today's entry: ").strip()

    if entry:
        add_entry(entry)
        print("Entry saved.")
    else:
        print("No entry written.")


if __name__ == "__main__":
    main()
