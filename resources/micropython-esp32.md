Some notes on how to get micropython running on your ESP32 board.

These instructions are generic and intended to work with most of the ESP32
boards, but - for documentation purposes - the specific dev board that we
have started with is the [DOIT ESP32 DEVKIT V1](https://makeradvisor.com/tools/esp32-dev-board-wi-fi-bluetooth/)

![DEVKIT V1](https://makeradvisor.com/wp-content/uploads/2017/10/esp32-board-bg.jpg)

* ensure you have enough power to run the ESP32 (you may need a better USB
  cable, or a second connection through the Vin/GND pins.  (If the red LED
  blinks then you probably have power problems)
* ensure you have a working serial connection
* * Install picocom ("sudo apt instll picocom")
* * determine which usb serial port your EPS32 has installed ("sudo dmesg")
* * connect with "sudo picocom -b 115200 /dev/ttyUSB7" (note to exit picocom
    you use Ctrl-A then Ctrl-X)
* * hit the "EN" button on your ESP32 and confirm that you see the bootup
    messages
* Install esptool (we need at least version 2.1)
* * check what version you can install "apt list esptool"
* * if your debian version is not new enough (currently Debian Buster is
    the oldest version with esptool 2.1) then you should install debian
    backports (see https://backports.debian.org/Instructions/) and then
    use "apt -t stretch-backports install esptool")
* * if you are using ubuntu, there may be a workaround
* * if you are using something else, we need to update these instructions
* Download micropython (http://micropython.org/download#esp32)
* follow the instructions on the download page to use esptool and flash
  micropython
* Connect with picocom again and confirm that you now have a python prompt
* Reset (again, with the "EN" button) and read the messages


# TODO
* udev name rules
* serial port permissions
* https://github.com/adafruit/ampy
* wifi section
