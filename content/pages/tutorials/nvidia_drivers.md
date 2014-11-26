Title: How to install NVIDIA drivers in Ubuntu
Category: Tutorials
Status: hidden

First of all download the driver you need from the official website. Then log out and press `CTRL+ALT+F1` (to go to a virtual terminal, this is mandatory) and type the next sequence of commands:

	:::bash
    $ sudo /etc/init.d/gdm stop (for GNOME or the equivalent on KDE)
    $ cd <drivers_path>
    $ sudo sh <driver_filename>
    $ sudo aptitude install nvidia-glx linux-restricted-common
    $ sudo nvidia-xconfig
    $ sudo /etc/init.d/gdm start

Since I'm not a Linux expert I can't say exactly if the `linux-restricted-common` package is mandatory (I think it is included in Ubuntu, the same with `nvidia-glx`), but well... just type it and nothing will go wrong.

__UPDATE:__ This works properly, but in some cases the driver cna break and you Ubuntu will return to its original appearance. Although all the programs will remain installed, in the graphic interface you won't probably see any program installed after Ubuntu. I still don't know how to fix this or why it is.