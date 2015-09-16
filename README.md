Ubuntu-AutoSuspend
====

Usage
---

- Turn you phones bluetooth on
- run `./script.py [MAC-ADDR] &`
- when the phone is visible the `there.sh`-File will be executed;
- when the phone is not visible the `away.sh`-File will be executed.

Working-Principle
---

Write down the Bluetooth-Mac-Address of your phone.

Enter the address into the programm.

Now the programm will ping your device; if your device cannot be found for a longer time, the programm will suspend the pc.


Install
---

###One-Liner

```bash
curl https://raw.githubusercontent.com/csicar/Ubuntu-AutoSuspend/master/install.sh | sh
```

###Manual
- Install bluez-python
- Add script.py to the autostart (/etc/rc.local or /etc/init.d/rc.local)
