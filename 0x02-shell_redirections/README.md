# 0x02. Shell, I/O Redirections And Filters
* This project is about input/output and Redirectons.

## Read or Watch
* shell, I/O Redirection
* Special Characters

## Man or Help:
* echo
* cat
* head
* tail
* find
* wc
* sort
* uniq
* grep
* tr
* rev
* cut
* passwd (5) (i.e, man 5 passwd)

## Objectives
### Shell, I/O Redirection

* What do the cammands head, tail, find, wc, sort, uniq, grep, tr, do?
* How to redirect standard output to a file
* How to get standard input from a file instead of the keyboard
* How to send the output from one program to the input of another program
* how to combine commands and filters with redirections

### Special Characters

* What are special characters
* Understand what do the white spaces, single quotes, double quotes, backlash, comment, pipe, command separator, tilde and how and when to use them.

### Other Man Pages
* How to display a line of text
* How to concatenate files and print on the standard output
* How to reverse a string
* How to remove sections from each line of files
* What is the /etc/passwd file and what is its format
* What is the /etc/shadow file and what is its format

## Tasks:

### 0. Hello World
 * This script prints "Hello, World", followed by a new line to the standard output.

### 1. Confused smiley
* Displays a confused smiley "(Ôo)'.

### 2. Let's display a file
* Displays the content of the /etc/passwd file

### 3. What about 2?
* Display the content of /etc/passwd and /etc/hosts

### 4. Last lines of a file
* Display the last lines of /etc/passwd

### 5. I'd prefer the first ones actually
* Display the 10 lines of /etc/passwd

### 6. Line #2
* Displays the third line of the file iacta.

### 7. It is a good file that cuts iron without making a noise
* Creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.

### 8. Save current state of directory
* Writes into the file ls_cwd_content the result of the command ls -la.
If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

### 9. Duplicate last line
* Duplicates the last line of the file iacta.

### 10. No more javascript
* Deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.

### 11. Don't just count your directories, make your directories count
* counts the number of directories and sub-directories in the current directory.

### 12. What's new
* Displays the 10 newest files in the current directory.

### 13. Being unique is better than being perfect
* Takes a list of words as input and prnts only words that appear exactly once.
* input format: One line, one word
* Output format: One line, one word
* Words should be sorted
	
### 14. It must be in that file
* Displays lines containing the pattern "root" from the file /etc/passwd

### 15. Count that word
* Displays the number of lines that's contained in the pattern "bin" in the file /etc/passwd

### 16. What's next?
* Displays lnes containing the pattern "root" and 3 lines after them in the file /etc/passwd.

### 17. I hate bins
* Displays all the lines in the file /etc/passwd that do not contain the pattern "bin"

### 18. Letters only please
* Displays all lines of the file /etc/ssh/sshd_config starting with a letter
* Including capital letters as well

### 19. A to Z
* Replaces all characters A and c from input Z and e respectively.

### 20. Without C, you would live in hiago
* Creates a script that removes all letters c and C from input.

### 21. esreveR
* This script reverse its input.

### 22. DJ Cut Killer
* Write a script that displays all users and their home directories, sorted by users.
* Based on the /etc/passed file

### 23. Empty casks make the most noise
* Finds all empty files and directories in the current directory and all sub-directories.
* Only the names of the files and directories should be displayed (not the entire path)
* Hidden files should be listed
* One file name per line
* The listing should end with a new line
* basename, grep, egrep, fgrep or rgrep are not to be used

### 24 A gif is worth ten thousand words
* Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

* Hidden files should be listed
* Only regular files (not directories) should be listed
* The names of the files should be displayed without their extensions
* The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
* One file name per line
* The listing should end with a new line
* basename, grep, egrep, fgrep or rgrep are not to be used
