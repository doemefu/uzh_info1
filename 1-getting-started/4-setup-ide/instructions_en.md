Like you saw in the previous task, Python programs are just plain text. This means that you can use any simple text editor (such as Notepad) to write Python programs. You then execute the programs from the command line, as you (hopefully) did with the `script.py` which printed "Hello, World!".

However, there are more complex applications which can provide varying degrees of aid when programming. Beyond the very basic text editors there are slightly more capable ones which, for example, provide [Syntax Highlighting](https://en.wikipedia.org/wiki/Syntax_highlighting). Furthermore, there exist so-called IDEs, short for "Integrated Development Environments", but they can be overwhelming in their complexity to novice programmers.

For the first few weeks of Informatics 1, we recommend that you set up and understand a programming environment consisting of the Command Prompt/Terminal and a simple but solid text editor with syntax highlighting. Here are some recommendations, although we encourage students to make their own choices:

 - [VS Code](https://code.visualstudio.com/) (cross-platform)
 - [Notepad++](https://notepad-plus-plus.org/) (Windows)
 - [Sublime Text](https://www.sublimetext.com/) (Mac, need to buy)
 - gedit, Kate, vim, etc. (Linux)

Using your editor of choice, paste the following code into a new file with a `.py` extension.

```python
from sys import version
print(version.splitlines()[0])
```

Then navigate to this file on the command line and execute the Python script, as described in the previous task. The terminal should contain some information about the installed Python runtime, please copy and paste your output into the solution box.

