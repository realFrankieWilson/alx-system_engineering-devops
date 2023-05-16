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
