 from ota_update.main.ota_updater import OTAUpdater


 def download_and_install_update_if_available():
     o = OTAUpdater('https://github.com/DouglasBahr/Lapras-Box')
     o.download_and_install_update_if_available('HOME-286C', 'tubscat1')


 def start():
     # your custom code goes here. Something like this: ...
     # from main.x import YourProject
     # project = YourProject()
     # ...

    import Lapris_func
    
    blink_pin(12)
    
 def boot():
     download_and_install_update_if_available()
     start()


 boot()