from os import system
from pathlib import Path


# here i user firefox as the main browser for me. you can change 
# as you wish

class commands:
    def shop(self, cmdList):
        try:
            site1 = "https://www.amazon.in/s?k="
            site2 = "https://www.flipkart.com/search?q="
            query = "+".join(cmdList[2:])
            system(f"start firefox {site1}{query}")
            system(f"start firefox {site2}{query}")
        except Exception:
            print("error")
    # randomly typing anyword after '!' , if its not a keyword 
    # it will be searched in google
    def search(self, cmdList):
        try:
            query = "+".join(cmdList[1:])
            system(f"start firefox https://www.google.com/search?q={query}")
        except Exception:
            print("error")

    def dirSite(self, var):
        try:
            system(f"start firefox {var}")
        except Exception:
            pass

    def preDefSite(self, cmdList):
        try:
            var = cmdList[1]
            if var.__contains__("dis"):
                site = "https://discordapp.com/channels/@me/"
            elif var.__contains__("red"):
                site = "reddit.com"
            elif var == "fb" or var == "facebook":
                site = "facebook.com"
            elif var == "jio":
                site = "192.168.1.1"
                try:
                    if cmdList[2] == "login":
                        site = "https://www.jio.com/JioWebApp/index.html?root=login#"
                except Exception:
                    pass
            elif var in ["mal", "myanimelist"]:
                site = "myanimelist.net"
                if len(cmdList) > 2:
                    if cmdList[2] in ["watch", "watchlist"]:
                        site = "https://myanimelist.net/animelist/Shishere?status=1"
                    elif cmdList[2] in ["comp", "completed"]:
                        site = "https://myanimelist.net/animelist/Shishere?status=2"
                    elif cmdList[2] in ["profile", "prof"]:
                        site = "https://myanimelist.net/profile/Shishere"
                    else:
                        query = "+".join(cmdList[2:])
                        system(
                            f"start firefox https://myanimelist.net/search/all?q={query}"
                        )
                        return
            elif var in ["mdl", "mydramalist"]:
                site = "mydramalist.com/"
                if len(cmdList) > 2:
                    if cmdList[2] in ["watch", "watchlist"]:
                        site = "https://mydramalist.com/dramalist/7509375"
                    else:
                        query = "+".join(cmdList[2:])
                        system(
                            f"start firefox https://mydramalist.com/search?q={query}"
                        )
                        return
            elif var in ["ka", "kissanime"]:
                if len(cmdList) > 2:
                    query = "%20".join(cmdList[2:])
                    system(f"start firefox https://kissanime.ru/Search/Anime/{query}")
                    return
                site = "https://kissanime.ru/"
            elif var in ["kd", "kissasian"]:
                if len(cmdList) > 2:
                    query = "-".join(cmdList[2:])
                    system(f"start firefox https://kissasian.sh/Search/Drama/{query}")
                    return
                site = "https://kissasian.sh/"
            elif var == "drive":
                site = "https://drive.google.com/drive/u/0"
                try:
                    if cmdList[2] == "1":
                        site = "https://drive.google.com/drive/u/1"
                except Exception:
                    pass
            elif var.__contains__("git"):
                site = "https://github.com/Shishere007"
                if len(cmdList) > 2:
                    site = f"https://github.com/{cmdList[2]}"
            elif var.__contains__("mail"):
                site = "https://mail.google.com/mail/u/0/"
                try:
                    if cmdList[2] == "1":
                        site = "https://mail.google.com/mail/u/1/"
                except Exception:
                    pass
            elif var in ["youtube", "yt"]:
                site = "https://www.youtube.com/"
                if len(cmdList) > 2:
                    search_item = "+".join(cmdList[2:])
                    site = f"https://www.youtube.com/results?search_query={search_item}"
            elif var == "steam":
                site = "https://store.steampowered.com/"
                if len(cmdList) > 2:
                    search_item = "+".join(cmdList[2:])
                    site = f"https://store.steampowered.com/search/?term={search_item}"
            elif var in ["paytm"]:
                site = "https://paytm.com/"
                if " ".join(cmdList).__contains__("re"):
                    site = "https://paytm.com/recharge"
            elif var in ["megasync", "mega"]:
                site = "https://mega.nz/"
            elif var in ["contacts", "cont"]:
                site = "https://contacts.google.com/"
            system(f"start firefox {site}")
        except Exception as e:
            print(e)

    def help(self):
        print(
            """
        Commands:-
        -> ! [sitecode] \t\t Visit pre-defined site
        -> ! adl {1,2,3} [name] \t Direct to anime download site
        -> ! [keyword] \t\t\t Searches keyword in google
        -> ! shop [item] \t\t Searches item in amazon nd flipkart 
        """
        )


class commandCall:
    def __init__(self):
        # typing any of the following commands after '!' as the user input
        # firefox will be opned with the website linked to the keyword
        # if you are adding new keyword , you will also need to update
        # site details for opening the site function 'preDefSite'
        self.commandList = [
            "github",
            "git",
            "discord",
            "dis",
            "mal",
            "myanimelist",
            "mdl",
            "mydramalist",
            "fb",
            "reddit",
            "facebook",
            "red",
            "ka",
            "kissanime",
            "kd",
            "kissasian",
            "drive",
            "mail",
            "youtube",
            "yt",
            "steam",
        ]
        self.class_call = commands()

    def broswerCommand(self, cmd):
        var = cmd.split()[1]
        try:
            if cmd.__contains__("shop"):
                self.class_call.shop(cmd.split())
            elif var in self.commandList:
                self.class_call.preDefSite(cmd.split())
            elif var == "help":
                self.class_call.help()
            # if the user input after '!' is website containing '.com','.net'
            # it will be directly loaded as a website
            # use '__contain__()' function to add more domain
            elif var.__contains__(".com") or var.__contains__(".net"):
                self.class_call.dirSite(var)
            else:
                self.class_call.search(cmd.split())
        except Exception:
            print("syntax error")


if __name__ == "__main__":
    pass
