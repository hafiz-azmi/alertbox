import win32api

def alert(header, message):
    win32api.MessageBox(0, message, header)
