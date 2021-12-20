from ota_update.main.ota_updater import OTAUpdater


 def download_and_install_update_if_available():
     o = OTAUpdater('https://github.com/edblagg/hello-world.git')
     o.install_update_if_available_after_boot('OUTATIME', '2712271227')


 def start():
     # This program prints Hello, world!
     print('Hello, world!')


 def boot():
     download_and_install_update_if_available()
     start()


 boot()


