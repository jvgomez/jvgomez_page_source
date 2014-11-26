Title: How to erase old Linux Kernels (Debian based distros)
Category: Tutorials
Status: hidden

Type on terminal:

	:::bash
	$ dpkg --get-selections | grep linux-image

A list with all the kernels will appear. Here it is possible to find the names we have to use in the next command. It is possible to erase all the kernels except the last one. Just type:

	:::bash
	$ sudo aptitude purge <kernel>

Where `<kernel>` is the name of the kernel we want to erase (got from the previous command).

__NOTE:__ Do __NOT__ erase the `linux-image-generic`, it is necessary to update the kernel.

[Source](http://www.guia-ubuntu.org/index.php?title=Borrar_kernels_antiguos)