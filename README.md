# ![Zoombie Ascii Logo](https://user-images.githubusercontent.com/73036332/132017908-f3706ef6-e325-49d9-9f80-06df4ebfa523.png)

_Automatically joins zoom meetings directly (without opening browser and shit) on windows, linux(or solaris, or BSD) and mac._  
_Also looks better that the other shit out there._

---

## Screenshot(s)

# ![Zoombie Screenshot1](https://cdn.discordapp.com/attachments/900714987893456936/903350808005988412/zoombie.png)

---

## Dependencies (need to be installed if not already installed)

1. [`xdg-open`](https://linux.die.net/man/1/xdg-open) for Linux (UNIX-like systems), [`open`](https://scriptingosx.com/2017/02/the-macos-open-command/) for Mac and `start` for Windows
2. [`curl`](https://curl.se/download.html)
3. [`zoom client`](https://zoom.us/support/download)

---

## Prerequisite (Windows only)

We need to get shell scripts working on your system first.  
Install [`Git Bash`](https://git-scm.com/downloads) (Comes along with Git) (Recommended; easier to setup).  
For help on installing Git Bash, check [this article](https://www.makeuseof.com/install-git-git-bash-windows/) or [this youtube video](https://www.youtube.com/watch?v=BMW7LiF_Oc4)  
_OR_  
Install [`MSys2`](https://msys2.org) 
  
NOTE: To launch the Git Bash terminal, search for "Git Bash" using your windows search and open it from there.

---

> ### **ℹ All the file/directory names are Case-Sensitive from here on**

## Installation

1. Launch your terminal (linux/mac) or your Git Bash terminal (windows) (refer to the note in the Windows section).

2. Run

```sh
curl "https://raw.githubusercontent.com/DaBigBlob/zoombie/main/install" -s | sh
```

(copy, paste and press ENTER or RETURN) \
\
3. The above command will also tell you where your `zoom-meetings.txt` is stored. REMEMBER IT because you'll need to assess it frequently. uwu

---

## Usage

1. Edit or add the required data to `zoom-meetings.txt` using your favourite text editor. (Details provided in the next section.)

2. Launch your terminal (Linux/Mac) or your Git Bash terminal (Windows)

3. Run

```sh
sh zoombie
```

(type and press ENTER or RETURN)

---

## Editing the `zoom-meetings.txt` file
1. Navigate to the directory (folder) mentioned in the step `3` of the installation section.
2. Open the `zoom-meetings.txt` file and edit with your favourite text editor. (Notepad works too -\_-)
### ***Format***  

```txt
 <time in 12 hours of format HH:MM(AM/PM)> <link for the zoom meeting> <topic within double quotes (""), this parameter is optional>
```

> Each field is to be separated by **1 space** in between them.

_**Use separate lines for separate meetings.**_  

### ***Sample***  

```txt
08:07AM https://zoom.us/j/93559000000?pwd=bnlVVlJOdDMrM2JCdzRnd1samplexxxx "Joe-Mama's Birthday. But prolly not gonna join."
10:20PM https://zoom.us/j/94705000000?pwd=VE5KckdtVGpzWEgxZGlzcVsamplexxxx "Pride Party! Woo Hoo!"
```

---

## Precaution

`zoombie` wont work offline. \
and 
### ***DO NOT RUN MORE THAN 1 INSTANCE OF `zoombie` AT A TIME***  

---

## How to exit `zoombie` (note4noobs)
Generic keyboards: `CTRL`+`c` \
Apple keyboards: `⌘`+`c`

---

## How to upgrade `zoombie` to latest version
You don't have to. \
Everytime you run `zoombie`, it automatically fetches the latest version.

---
***Special thanks to contributor SpiderMath for adding Windows support.***
