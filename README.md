# Zyxel-supervisor
Retrieve supervisor and root password for the Zyxel VMG8825-T50. The supervisor account is far more privilliged than the admin account. With the root account you cannot login to the web interface.

Steps to follow:
1. Login to the device (with the default admin account) using Firefox.
2. In the Firefox, press F12 and go Storage. Take note of the Session key under cookies. Take note of the AesKey under Local Storage.
3. Run the script in fill in the IP, the Session key and the AesKey

Notice: you need to run this script from the same IP as from where you logged on to the device via Firefox

![image](https://user-images.githubusercontent.com/45763032/222258522-5450bbc5-e25b-455a-b8cf-94db18b4247d.png)

![image](https://user-images.githubusercontent.com/45763032/222258607-b9f5173b-8d23-4b75-8a72-2c98ff7733f0.png)

![image](https://user-images.githubusercontent.com/45763032/222258951-4174e7d9-669f-4e87-9fb5-c4ef9bd802e4.png)
