# Zyxel-supervisor
Retrieve supervisor and root password for the Zyxel VMG8825-T50. The supervisor account is far more privilliged than the admin account. With the root account you cannot login to the web interface.

Steps to follow:
1. Login to the device (with the default admin account) using Firefox.
2. In the Firefox, press F12 and go Storage. Take note of the Session key under cookies. Take note of the AesKey under Local Storage.
3. Run the script in fill in the IP, the Session key and the AesKey

Notice: you need to run this script from the same IP as from where you logged on to the device via Firefox
