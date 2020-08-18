from clientlib import UDPTEXTCLIENT

UTEXT = UDPTEXTCLIENT("clientconf.js")

while True:
    select = input("What do you want to do? M(Send MSG)/S(Scan for MSG)")
    if select.lower() == "m":
        msg = input("\nWhat should the msg be?: ")
        UTEXT.sendmsg(msg)
        UTEXT.messagehandler()

    elif select.lower() == "s":
        UTEXT.messagehandler()