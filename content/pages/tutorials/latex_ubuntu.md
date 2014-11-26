Title: Manually install LaTeX packages in Ubuntu
Category: Tutorials
Status: hidden

The following four steps permit manual installation of packages on Debian/Ubuntu (and presumably other Linux) systems. If you have the sty file already, skip steps 1 and 2.

- Download the package from CTAN (e.g., _footmisc.zip_).
- Extract the files and place them in an appropriate directory (e.g. `/usr/local/share/texmf/tex/latex/footmisc/`). This location is preferable to the main installation tree (/usr/share/texmf-texlive/tex/latex/) as the files are more likely to be preserved during upgrades.
- Generate the `.sty` file by running latex on the appropriate source files (e.g., `$ latex footmisc.ins` and `$ latex footmisc.dtx`).
- Update the ls-R file in this source tree:

        :::bash
        $ cd /usr/local/share/texmf/
        $ sudo mktexlsr

Because `/usr/local/share/texmf/tex/` is not searched recursively by kpathsea (cf. `kpsepath tex`), the `ls -R` file at the root directory of this search path must be updated to make the system aware of the new package.

Souce](http://tex.stackexchange.com/questions/38978/how-can-i-manually-install-a-latex-package-debian-ubuntu-linux)

__Adding LaTex .sty files into the LaTeX Texlive installation in Ubuntu__

    :::bash
    $ sudo cp <package>.sty  /usr/share/texmf-texlive/tex/latex/base/
    $ sudo mktexlsr

[Souce](http://stackoverflow.com/questions/1911713/add-find-style-files-in-to-latex)