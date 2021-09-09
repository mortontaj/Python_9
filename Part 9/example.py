import webbrowser
#
# webbrowser.open("http://www.python.org/", new=1)
#
# help(webbrowser)

# chrome = webbrowser.get(using='/usr/bin/google-chrome %s').open_new_tab("https://www.python.org/")

windows = webbrowser.get(using='windows-default')
windows.open('http://www.python.org/')
