# ![Zoombie Ascii Logo](https://media.discordapp.net/attachments/840857306040500225/883298728155443230/carbon.png?width=844&height=490)

_Automatically joins zoom meetings directly (without opening browser and shit) on windows, linux(or solaris, or BSD) and mac._  
_Also looks better that the other shit out there._

---

## Dependencies (need to be installed if not already installed)

1. `xdg-open` for Linux (UNIX-like systems), `open` for Mac and `start` for Windows
2. `curl` (don't mind if windows)
3. Zoom

---

## Prerequisite (Windows only)
We need to get shell scripts working on you system first. \
\
Install [`Git Bash`](https://git-scm.com/downloads) (Comes along with Git) (Recommended). \
For help on installing Git Bash, check [this article](https://www.makeuseof.com/install-git-git-bash-windows/) or [this youtube video](https://www.youtube.com/watch?v=BMW7LiF_Oc4)\
_OR_\
Install [`MSys2`](https://msys2.org) (Not recommended, heavier on resources). \
\
\
NOTE: To launch the Git Bash terminal, search for "Git Bash" using your windows search and Open it from there.

---

> ### **ℹ All the file/directory names are Case-Sensitive from here on**
## Installation
1. Launch your terminal (linux/mac) or your Git Bash terminal (windows) (refer to the note in the Windows section).
2. Run
```sh
curl "https://raw.githubusercontent.com/DaBigBlob/zoombie/main/install" -s | sh
```
(copy and press ENTER or RETURN)

---

## Usage
1. Edit or add the required data to `zoom-meetings.txt` using your favourite text editor. (Details provided in the next section.)
2. Launch you terminal (linux/mac) or your Git Bash terminal (windows) (refer to the note in the Windows section)
3. Run
```sh
sh zoombie
```
(type and press ENTER or RETURN)

---

## Editing the `zoom-meetings.txt` file
FORMAT:
```
 <time,24-hours-format,HH:MM> <link-for-the-meeting> <topic-(no-numbers,no-spaces)(optional)>   ---each-field-separated-by-SINGLE-spaces
```
Use separate lines for separate meetings. \
EXAMPLE:
```
08:07 https://zoom.us/j/93559000000?pwd=bnlVVlJOdDMrM2JCdzRnd1samplexxxx Joe-Mama's-Birthday
17:20 https://zoom.us/j/94705000000?pwd=VE5KckdtVGpzWEgxZGlzcVsamplexxxx Pride-Party
```
---
