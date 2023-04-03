import winreg
access_registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)

keys = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\PYP')
buildtmp = (list(winreg.EnumValue(keys, 0))[1])
venvtmp = (list(winreg.EnumValue(keys, 1))[1])