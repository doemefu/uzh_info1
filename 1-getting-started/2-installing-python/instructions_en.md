To make sure that you can follow the lecture and exercises, you need to have a local Python installation on your personal computer. This is even more relevant for the midterm and final exams, which you will need to solve on your own computer!

**Important**: It is required that you run the latest or previous-to-latest Python version at any given time during the lecture. To check which versions are permitted, go to [manual download](https://www.python.org/downloads/) and look at the latest release (for example, 3.11.5). You can use either this latest version, or the previous version (in this case, 3.10.13).

On Apple Mac OS and many Linux distributions, Python is usually installed already. To check, open a terminal ("Command Prompt" on Windows or "Terminal" on Mac - if you're using Linux, you know what to do) and type `python`. If there is no error, python is installed. **Important**: If you see that the python version shown on the first line of the command line output is **not** one of the latest versions, then you are running an old version of Python. If you see that it's an older version of Python 3, then install the latest version. If you see that it's Python 2, then try opening a new terminal and typing `python3`. If this produces the desired output, you are fine. In this case, for the rest of the semester, you must always run `python3` instead of `python`, in order to be running the correct version. If `python3` gives an error, you have to manually install Python 3. **When in doubt, just install the newest Python version anyway**.

On Microsoft Windows, you may need to download and install Python yourself, either from the Microsoft Store or via a [manual download](https://www.python.org/downloads/) and installation. Check first if Python is already installed, otherwise refer to [this page](https://wiki.python.org/moin/BeginnersGuide/Download) to learn how to install Python. Be sure that Python is "added to your PATH" if a choice is given during the installation. If you consider yourself an advanced user, consider using [WSL](https://learn.microsoft.com/en-us/windows/wsl/about).

Once the Python development environment is installed, you should be able to open a terminal and execute the command `python` or `python3` to launch an interactive Python shell. You can, for example, use it as a calculator:

![A Python Shell on Windows](resource/python.png "A Python Shell on Windows")

From the terminal, copy the output of running `python --version` into `script.py`, assigning it as a string to the variable `version`. Mind that depending on your machine, you may need to run `python3 --version` instead!

