
# Probe, find and choose your Wi-Fi channels

If you live or work in a crowded space, it may be difficult to get a stable
Wi-Fi signal. The two most common
[802.11 frequencies](https://en.wikipedia.org/wiki/IEEE_802.11#Channels_and_frequencies)
are 2.4 GHz and 5 GHz, the former of which being the only frequency supported
by many older devices. That often makes it the most disputed frequency and is
very often subject to interference from nearby networks.

A trick that you'll soon
[find](https://www.howtogeek.com/197268/how-to-find-the-best-wi-fi-channel-for-your-router-on-any-operating-system/)
when searching for a solution on the internet is to configure your router to
use a less crowded channel. But that may not be so obvious, as the channels
have overlapping frequencies. Channels with non-overlapping frequencies are
just 1, 6 and 11, as seen on the following diagram:

![Depiction of Wi-Fi channels in the 2.4 GHz band](wifi-channels.svg)
(Image
[courtesy of](https://en.wikipedia.org/wiki/IEEE_802.11#/media/File:2.4_GHz_Wi-Fi_channels_(802.11b,g_WLAN).svg)
Michael Gauthier, KelleyCook and Whidou, CC-BY-SA 3.0)

If you don't want to install any app or additional software for the purpose of
choosing a Wi-Fi channel for you, you don't need to. On many GNU/Linux
distributions such as Ubuntu, just use the follwing on the command line:

```
$ sudo iwlist wlan0 scan | grep \(Channel
```

That will indeed display which channels each of your nearby networks is using.
However, when you have dozens of them around, it becomes extremely tedious and
time consuming to count them all by hand.

Here is where this script will be useful. Just run

```
$ sudo python3 scan-wifi.py
```

and you'll get a nice summary of which non-overlapping channels are most
occupied. Just pick the least used one and you're good to go. You could run it
without `sudo` (or root privileges), but you'll probably get only one result,
which is the Wi-Fi interface you are currently using. The operating system
requires privileges to access information about the other available Wi-Fi
networks. But the Python script is really short and simple (even shorter than
this explanation), so go ahead and take a look at it if you want. Maybe you'll
even find something to improve upon.

