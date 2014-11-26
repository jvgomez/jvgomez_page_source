Title: How to compress a RAR file into multiple parts
Category: Tutorials
Status: hidden

This is very useful when a big file is wanted to be separated into multiple smaller, compressed files. For that, all you should  do is to type in the terminal:

    :::bash
    $ sudo apt-get install rar
    $ rar a -m5 -v5M -R <name> <file_to_compress>

The options mean:

- `rar` - we are going to use Rar program.
- `a` - adding files.
- `-m5` - compression level (0-store (fast)...3-default...5-maximum(slow)).
- `v5M` - size of the parts: 5 Megabytes (-v5M), 3 Gigabytes (-v3G) and so on.
- `<name>` - name of the archive you are creating.
- `<file_to_compress>` - files or folder you wish to add to the archive.

[Source](http://www.ubuntu-unleashed.com/2008/05/howto-create-split-rar-files-in-ubuntu.html)