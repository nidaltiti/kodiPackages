import xbmcplugin
import xbmcaddon
import xbmcgui
import sys

# Import your module (must be installed from repo automatically)
try:
    import mydependency  # replace with actual module name in lib folder
    xbmcgui.Dialog().notification("Dependency", "script.module.mydependency loaded successfully!")
except ImportError:
    xbmcgui.Dialog().notification("Dependency", "Failed to import mydependency")

# Show a simple item in Kodi video add-on
url = sys.argv[0]
handle = int(sys.argv[1])

li = xbmcgui.ListItem(label="Sample Video")
li.setInfo(type="video", infoLabels={"title": "Sample Video"})
li.setPath("https://www.example.com/video.mp4")

xbmcplugin.addDirectoryItem(handle, "https://www.example.com/video.mp4", li, False)
xbmcplugin.endOfDirectory(handle)
