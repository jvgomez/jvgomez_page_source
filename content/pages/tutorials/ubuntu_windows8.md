Title: Install Ubuntu together with Windows 8
Category: Tutorials
Status: hidden

I had many many troubles trying to install Ubuntu 12.04.3 LTS together with Windows 8. More or less, this is what I did:

- Clean Windows 8 installation in UEFI mode. Everything ok and easy here.
- Disable SecureBoot in the BIOS and set it to Legacy mode.
- For all the Ubuntu/Linux USB live creators I have used Linux Live USB: http://www.linuxliveusb.com/
- Install Ubuntu normally, creating the partitions manually with the wizard (boot partition, swap partition, etc). I followed this: http://askubuntu.com/a/228069

In my case a created a 100 MB partition for boot (logical, "reserver BIOS boot area")  And for swap 4GB, logical (swap area) partition (look this post http://askubuntu.com/a/49138 ). Lastly, the rest of the space a ext4 file system partition, Primary, with / as mounting point.

- After that, "Opertaing system not found" when booting.
- I recovered the boot with this: http://sourceforge.net/p/boot-repair-cd/home/Home/
- Follow the instructions there (recommended reparation). You will need any way to connect to the internet. In my case, an external WiFi dongle.

__NOTE__ It can happen that it says something like:

	:::bash
    Errors were encountered while processing:
    grub-efi-amd64
    grub-efi
    E: Sub-process /usr/bin/dpkg returned an error code (1)

A trick is given in https://bugs.launchpad.net/ubuntu/+source/grub2/+bug/1178534, concretely post 5: https://bugs.launchpad.net/ubuntu/+source/grub2/+bug/1178534/comments/5

- After that, set the BIOS in UEFI mode again and everything should work.
