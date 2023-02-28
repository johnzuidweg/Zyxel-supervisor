# Zyxel-supervisor
Retrieve supervisor and root password for the Zyxel VMG8825-T50. The supervisor account is far more privilliged than the admin account. The root password cannot login to the web interface.

First, login to the device (with the default admin account) using Firefox.

In the Firefox, press F12 and go Storage. Take note of the Session key under cookies. Take note of the AesKey under Local Storage.

Notice: you need to run this script from the same IP as from where you started the browser
