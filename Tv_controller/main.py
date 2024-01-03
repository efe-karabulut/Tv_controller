class Tv:
    def __init__(
        self,
        status="closed",
        volume=0,
        channel=["Fox", "Euro News", "BBC", "MTV"],
        currentChannel="Fox",
        channelNumber=0,
    ):
        self.status = status
        self.volume = volume
        self.channel = channel
        self.currentChannel = currentChannel
        self.channelNumber = channelNumber

    def tvOpen(self):
        if self.status == "opened":
            print("it's already opened.")
        else:
            self.status = "opened"
            print("Tv is", self.status)

    def tvClose(self):
        if self.status == "closed":
            print("it's already closed.")
        else:
            self.status = "closed"
            print("Tv is", self.status)

    def tvVolumeUp(self):
        if self.status == "opened":
            if self.volume == 10:
                print("Max volume!")

            else:
                self.volume += 1
                print("Volume:", self.volume)
        else:
            print("turn on the TV first ")

    def tvVolumeDown(self):
        if self.status == "opened":
            if self.volume != 0:
                self.volume -= 1
                print("Volume:", self.volume)
            else:
                print("Min Volume!")
        else:
            print("turn on the TV first ")

    def channelUp(self):
        if self.status == "opened":
            try:
                self.channelNumber += 1
                newChannel = self.channel[self.channelNumber]
                self.currentChannel = newChannel
                return self.currentChannel
            except IndexError:
                self.channelNumber = 0
                newChannel = self.channel[self.channelNumber]
                self.currentChannel = newChannel
                return self.currentChannel
        else:
            print("turn on the TV first ")

    def channelDown(self):
        if self.status == "opened":
            try:
                self.channelNumber -= 1
                newChannel = self.channel[self.channelNumber]
                self.currentChannel = newChannel
                return self.currentChannel
            except IndexError:
                self.channelNumber = len(self.channel) - 1
                newChannel = self.channel[self.channelNumber]
                self.currentChannel = newChannel
                return self.currentChannel
        else:
            print("turn on the TV first ")


tv = Tv()


info = print(
    """
    *******************
    Tv Controller
    a-) Open The TV(1)
    b-) Close The TV(2)
    c-) Volume Up(3)
    d-) Volume Down(4)
    e-) Channel Up(5)
    f-) Channel Down(6)
    
    İnfo: For exit press "q"    
    *******************
    """
)

while True:
    user = input("Please enter the number of the transaction you want to make: ")
    if user == "q":
        print("Tv app is closing...")
        break
    else:
        if user == "1":
            tv.tvOpen()
        elif user == "2":
            tv.tvClose()
        elif user == "3":
            tv.tvVolumeUp()
        elif user == "4":
            tv.tvVolumeDown()
        elif user == "5":
            print("Your Location:", tv.channelUp())
        elif user == "6":
            print("Your Location:", tv.channelDown())
        else:
            print("Please enter a valid number")
