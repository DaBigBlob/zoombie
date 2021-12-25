#this python file is written only for windows; do not use in posix systems
import sys, os
if os.name != "nt":
    print("This version is only meant for Microsoft Windows. Visit https://github.com/DaBigBlob/zoombie for help. Quit.")
    sys.exit()
try:

    import time #requests
    from datetime import datetime
    version = "V10.4"

    def caldatetime(date,time):
        if date == 'today':
            tempdate = datetime.now().strftime('%d/%m/%Y')
        else:
            tempdate = date
        if time == 'now':
            temptime = datetime.now().strftime('%I:%M%p')
        else:
            temptime = time
        return f"{tempdate};{temptime}"

    from colorama import init, Fore, Style
    init() #colorama init
    RD = Style.DIM+Fore.RED
    RB = Style.BRIGHT+Fore.RED
    GD = Style.DIM+Fore.GREEN
    GB = Style.BRIGHT+Fore.GREEN
    Y = Style.BRIGHT+Fore.YELLOW
    BDD = Style.DIM+Fore.MAGENTA
    BD = Style.DIM+Fore.BLUE
    BB = Style.BRIGHT+Fore.BLUE
    M = Style.BRIGHT+Fore.MAGENTA
    CD = Style.DIM+Fore.CYAN
    CB = Style.BRIGHT+Fore.CYAN
    WB = Style.BRIGHT+Fore.WHITE
    WD = Style.DIM+Fore.WHITE
    WDD = Style.BRIGHT+Fore.BLACK
    RST = Fore.RESET+Style.RESET_ALL

    os.system('cls')
    print(f"""
{WD}▒███████▒ ▒█████   ▒█████   ███▄ ▄███▓ ▄▄▄▄    ██▓▓█████ 
▒ ▒ ▒ ▄▀░▒██▒  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓██▒▓█   ▀ 
░ ▒ ▄▀▒░ ▒██░  ██▒▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██▒▒███   
  ▄▀▒   ░▒██   ██░▒██   ██░▒██    ▒██ ▒██░█▀  ░██░▒▓█  ▄ 
▒███████▒░ ████▓▒░░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░██░░▒████▒
░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░▓  ░{GB+version+WD}░
░░▒ ▒ ░ ▒  ░ ▒ ▒░   ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ▒ ░ ░ ░  ░
░ ░ ░ ░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░      ░    ░    ░  ▒ ░   ░   
  ░ ░        ░ ░      ░ ░         ░    ░       ░     ░  ░
░                                           ░             
{RD}████{RB}████{GD}████{GB}████{Y}████{BDD}████{BD}████{BB}████{M}████{CD}████{CB}████{WDD}████{WD}████{WB}████
{RD}████{RB}████{GD}████{GB}████{Y}████{BDD}████{BD}████{BB}████{M}████{CD}████{CB}████{WDD}████{WD}████{WB}████
    """)

    if os.path.exists('zoom-meetings.txt'):
        meetings = open('zoom-meetings.txt', 'r').readlines()
        datetimes = []
        links = []
        comments = []
        print(f"{RD}[*]{GD}Reading 'zoom-meetings.txt' file...")
        for row in meetings:
            rowArr = row.replace('\n','').replace('\t','').split(';;')
            if len(rowArr) < 4: #fill missing cells with ""
                for d in range(4-len(rowArr)):
                    rowArr.append("")
            datetimes.append(caldatetime(rowArr[0].strip(),rowArr[1].strip()))
            links.append(rowArr[2].strip())
            comments.append(rowArr[3])
        print(f"{M}DATE{' '*8}{CB}TIME{' '*5}{' '*(51)}{M}LINK  {CB}COMMENT")
        for k in range(len(meetings)-1): #the table
            print(f"{CB}{datetimes[k+1].split(';')[0].ljust(10, ' ')[:10]}  {M}{datetimes[k+1].split(';')[1].ljust(7, ' ')[:7]}  {CB}...{links[k+1].rjust(63, ' ')[-52:]}  {M}{comments[k+1]}")
        print(f"{RD}[#]{GD}Done.\n")
        print(f"{RB}[*]{GB}Starting on {CB}{datetime.now().strftime('%d/%m/%Y')}{GB} at {CB}{datetime.now().strftime('%S')}{GB} second(s) past {CB}{datetime.now().strftime('%I:%M%p')}{GB}...")

        def lessGo(index):
            link = links[index]
            domain = link.split('/')[3]
            mID = link.split('/')[-1].split('?')[0]
            pswd = link.split('/')[-1].split('=')[1]
            os.system(f'start zoommtg://{domain}/join?action=join"&"confno={mID}"&"pwd={pswd} /HIGH')
            print(f"{GB}[!]{RB}STARTING MEETING...\n{'█'*(len(link)+10)}\n██ {GB}DATE: {M}{datetimes[index].split(';')[0]}{RB}\n██ {GB}TIME: {M}{datetimes[index].split(';')[1]}{RB}\n██ {GB}COMMENT: {M}{comments[index]}{RB}\n██ {GB}MEETING ID: {M}{mID}{RB}\n██ {GB}LINK: {M}{link}{RB}\n{'█'*(len(link)+10)}\n{GB}[#]{RB}DONE.")

        print('\n')
        #begin de loup
        while True:
            dt = datetime.now().strftime('%d/%m/%Y;%I:%M%p')
            if dt in datetimes:
                lessGo(datetimes.index(dt))
                print('\n')
            print(f"{M}[{CB}{datetime.now().strftime('%d/%m/%Y-%I:%M%p')}{M}]{GB}Waiting for the next meeting...", end='\r')
            time.sleep(60)
                    
            
    else:
        print(RB+"'zoom-meetings.txt' does not exist in this directory. Visit https://github.com/DaBigBlob/zoombie for help. Quit.")
        sys.exit()
except:
    print("\n\nSee ya!  o/")
    sys.exit()
