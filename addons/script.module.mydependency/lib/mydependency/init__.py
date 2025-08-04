from mydependency import hello_world
import xbmcgui

msg = hello_world()
xbmcgui.Dialog().ok("Dependency Test", msg)
