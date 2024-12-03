In this task, you will go through the required steps for creating a new local Git repository. We will test whether you know how to `init` a repository, `add` files to the index, and `commit` change sets. In contrast to many other tasks, you are not going to write Python code this time. Instead, you will be writing a *shell script*. On your interactive command line, you enter git commands one by one. Here, you simply add all the commands to a file `script.sh`, which will then execute them one after the other for you.

**Important**: Assume that the `script.sh` will be executed in your current working folder (i.e., the *current working directory* will be the `task` folder, *not* the parent folder containing the `task` folder, and you will initialize the repository in the current working directory).

Perform the following steps (make sure you get the string components exactly right):

* Initialize a Git repository in the current folder.
* Create a new file `a.txt` with the content `aaa` (You can achieve this on the command line via `printf "aaa" > a.txt`).
* Create a new file `b.txt` with the content `bbb`.
* Add both files to the Git index.
* Commit the current index and use the commit message `Add files a.txt and b.txt` (since ACCESS grading is non-interactive, use the `-m` parameter to pass the commit message when committing).
* *Append* the text `b2` in a new line to `b.txt` (You can achieve this via `printf "\nb2" >> b.txt`, please note the `\n` and the `>>`)
* Add and commit your changes using the message `Add second line to b.txt`.

The grading will only consider the current state of the index and the history of your newly created repository, so feel free to add further `printf` commands to analyze what's happening. However, we **strongly recommend** that you to experiment with the different commands *locally on your machine* and to inspect their effects in a graphical tool. Solve the exercise locally, then copy the commands you used into ACCESS for submission.

**Note:** If you do not have a working Git installation on your machine that you can use from the command line, please [install a current version](https://git-scm.com/downloads). As Git internally represents the history in a tree, you may also want to use a graphical client like [SourceTree](https://www.sourcetreeapp.com/), [Git Extensions](https://gitextensions.github.io/), or the minimalistic [Gitk](https://git-scm.com/docs/gitk) to inspect the current state of the repository.

**Note:** After executing the script, your index should be clean and there should be no changed files in your working directory.

**Note:** Your scripts cannot access the internet and may timeout if you try.

