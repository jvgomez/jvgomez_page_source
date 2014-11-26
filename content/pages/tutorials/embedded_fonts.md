Title: Solve embedded fonts issues when submitting papers (i.e. Paperplaza)
Category: Tutorials
Status: hidden

The idea is to run your pdf graphics through ghostscripts' pdfwrite device to get the fonts embedded (whatever that means):

    :::bash
    $ ps2pdf13 -dPDFSETTINGS=/prepress foo.pdf bar.pdf

or

	:::bash
	$ ps2pdf -dEmbedAllFonts=true foo.pdf bar.pdf

To check which fonts are embedded:

    :::bash
    $ pdffonts foo.pdf


[Souce](http://tug.org/pipermail/pdftex/2005-September/005997.html)