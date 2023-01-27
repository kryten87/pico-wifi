# pico-wifi
A proof of concept project to enable dynamic setting of Raspberry Pi Pico W wireless configuration.

## Description
Some wireless IoT devices, like the Amazon Echo, allow you to dynamically set the WiFi credentials the first time you power the device. Here's how they work:

1. The device starts up in WiFi access point mode with a unique and identifiable SSID.
2. You connect to that SSID with your phone.
3. You then use the mobile app for the IoT product to give the device the SSID/Passphrase for your WiFi network.
4. The device then restarts and connects to the SSID with the passphrase you just gave it.

I would like to develop a library to do this on a Raspberry Pi Pico W device. I'm imagining the following:

1. Pico W starts up
2. If there is no SSID/passphrase stored in non-volatile storage<sup>1</sup>, then enter *set up* mode
    * Calculate a random SSID name which is still identifiable (eg. `My_Pico_5732`<sup>2</sup>)
    * start up a web server on a known address (192.168.0.1 perhaps<sup>3</sup>)
    * serve a simple form which asks for SSID & passphrase. It should also have a "save" button (and possibly a "reset" button<sup>4</sup>)
    * handle form submissions by storing SSID/passphrase and restarting the device <sup>5</sup>
3. If there **IS** an SSID/passphrase in storage, then
    * attempt to connect to the WiFi network
        * after a certain number of failures, alert the user<sup>6</sup>, wait a while, and retry
    * once connected, enter normal operations (whatever that might be)

Notes:
<sup>1</sup> I need to determine how the Pico can store values in non-volatile storage (or if it can).

<sup>2</sup> The prefix for this SSID name can be set at build time from configuration.

<sup>3</sup> The IP address can also be configured at build time.

<sup>4</sup> I'm not sure how to handle factory resets - might be better done via a hardware button.

<sup>5</sup> Also need to figure out how to reset the device in software

<sup>6</sup> Basic idea for alerting the user of error conditions: flash the onboard LED. It would be better to somehow make this configurable.

## Roadmap

**MVP**: start up in AP mode, serve web page, store credentials, restart and connect
