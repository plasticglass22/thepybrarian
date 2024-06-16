# Pybrarian

## Developer Note

Thank you for taking a look at Pybrarian! This is the first programming project I've seen through to an actual state of usability, so I'm very proud, despite its simplicity and lack of originality.

If you have any ideas for how to improve the program, please feel free to leave a comment. I'm hoping to become a better programmer, and greatly appreciate the guidance. You can even fork the project and submit upgrades if you like, but I'm still learning how pull requests work, so no promises.

Again, thank you. I hope you enjoy the program, and stay tuned for new versions in the future.

And yes, I know it's a bad pun. I don't care.

## Version History

v1.0 - 16 June 2024

## Purpose

Pybrarian recursively lists all the files in a directory and it's subdirectories. Pybrarian allows searching by substring in a filename, or by substring in a directory name with the `-d` flag.

## Installation

At time of publishing v1.0, the program must be run as a python3 script. Download the three requisite .py files: main.py, utils.py, aesth.py. Make sure these three files are all in the directory you wish to run the program. See *Usage* for how to run Pybrarian.

## Future

### Immediate next steps:

1. Bug fixes (I did my best but I'm sure there are more).
2. Package the program into an executable so the user won't have to copy 3 files into a working directory every time.

### Future plans:

1. For v2.0: Integrate an interactive TUI that allows the user to browse through their directories, kind of like Ranger.

## Usage

Return all items in a directory an subdirectories:
    python3 main.py

Search by substring in a filename:
    python3 main.py *searchterm*

Search by substring in a directory name:
    python3 main.py -d *searchterm*

## Credits

developer: plasticglass
project start: 5 June 2024
last updated: 16 June 2024