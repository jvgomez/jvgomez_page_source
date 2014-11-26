Title: Convert .ogv to .avi (high quality) with MEnconder
Category: Tutorials
Status: hidden

This one is easy, just typing in terminal one of these commands:

    :::bash
    $ mencoder input.ogv -ovc xvid -oac mp3lame -xvidencopts pass=1 -o output.avi

Or

    :::bash
    $ mencoder input.ogv -o output.avi -ovc lavc -oac mp3lame