Title: Solving issues with GLIBCXX and libstdc++
Category: Tutorials
Status: hidden

## UPDATE
A simple workaround seems to be yo use

    :::bash
    $ locate libstdc++.so

And in Matlab:

	:::matlab
    >> LD_PRELOAD='path/to/libstdc++.so'

More info [here](https://github.com/kyamagu/mexopencv/issues/45).

<dl class="section note"><dt>Note</dt><dd>All this was done in Ubuntu 12.04 64 bits.</dd></dl>

## Problem

When using Matlab and external programs or mex compiled functions it can occur that:

    <span style="color:#ff0000">
    <path to matlab> /MATLAB/R2011a/sys/os/glnx86/libstdc++.so.6: version `GLIBCXX_3.4.15' not found (    required by <whatsoever>)
    </span>

This problem comes from the GCC program. It seems that this library `libstdc++.so.6` is compiled but not installed when installing GCC ([link](http://stackoverflow.com/questions/5216399/usr-lib-libstdc-so-6-version-glibcxx-3-4-15-not-found)).

Another problem could be that the version of `libstdc++.so.6` is so old so your version of `GLIBCXX` is older that the one you are required.

The simplest solution is to check where is linked the following file ([link](http://judsonsnotes.com/notes/index.php?option=com_content&view=article&id=611:matlab-running-external-programs&catid=57:programming&Itemid=81)):

    <path to matlab> /MATLAB/R2011a/sys/os/glnx86/libstdc++.so.6

By using the locate command:

    :::bash
    $ sudo updatedb
    $ locate libstdc++.so.6

And it will return something like:

    :::bash
    libstdc++.so.6 -> libstdc++.so.6.0.10

So now you have information enough to _update_ the link you the libstdc\++.so.6 by creating a symbolic link:

    :::bash
     $ ln -sf  /usr/lib/i386-linux-gnu/libstdc++.so.6.0.16 /usr/local/MATLAB/R2011a/sys/os/glnx86/libstdc++.so.6

### UPDATE!
When solving the previous error, the same error appeared but in another folder, so just recreate the symbolic link with the proper folder and in will work without doing all the following stuff (don't care about versions, I was doing this in other pc):

    :::bash
    $ sudo ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.16 /usr/local/MATLAB/R2012a/bin/glnxa64/libstdc++.so.6

This solution could fix the problem of running external programs from Matlab, such as GNUplot.

My case was much harder: I was using mex files, and those mex files were compiling OK but when running the `mex64a` files MATLAB was not able to find that library. Eventhough MATLAB includes that library within its files...

Before testing every solution, be sure to close Matlab and open it again.

You can try the following things:

- Update symbolic links ([link](http://buildall.wordpress.com/2011/04/21/glibcxx_3-4-15-not-found-after-install-gcc-4-6/)):

        :::bash
        $ sudo cp gcc/build/x86_64-unknown-linux-gnu/libstdc++-v3/src/.libs/libstdc++.so.6.0.15 /usr/lib/
Note that `gcc/build/x86_64-unknown-linux-gnu/libstdc++-v3/src/.libs/libstdc++.so.6.0.15` is the trunk compiled from the GCC. You won't probably have that, but if you have `libstdc++.so.6.0.15` (or whatever) in other folder just change this folder. Recreate the symbolic links:

        :::bash
        $ sudo rm libstdc++.so libstdc++.so.6
        $ sudo ln -s libstdc++.so.6.0.15 libstdc++.so
        $ sudo ln -s libstdc++.so.6.0.15 libstdc++.so.6

- Get GCC code and compile it locally ([link](http://ehren.wordpress.com/2009/09/20/building-gcc-from-trunk/)) Before that, try to remove all the symbolic links previously done or already existing before the error, and revert all the stuff you have done until now. So, here we go!:
First install Subversion and get the code from the repository ([link](http://ehren.wordpress.com/2009/09/20/building-gcc-from-trunk/)):

        :::bash
        $ sudo apt-get install subversion
        $ svn checkout svn://gcc.gnu.org/svn/gcc/trunk srcdir
Check the repository [here](http://gcc.gnu.org/svn/gcc/) in case you rather prefer getting a branch than the trunk version. While downloading (it takes a long while), open a terminal and create the Makefile from the configure:

        :::bash
        $ cd srcdir
        $ ./configure --enable-checking=release --enable-languages=c,c++
These options are the one which worked from me. To make the compilation faster other options you can add are `--disable-libquadmath` if not using fortran, and `--disable-libmudflap` and `--disable-libitm` if you don't want to use those features. You can also speed up builds by using `--disable-bootstrap CFLAGS="-g3 -O0"` ([link](http://gcc.gnu.org/ml/gcc-help/2011-12/msg00068.html)).
After that, the output will probably look as follows:

        checking for correct version of gmp.h... no
        checking for the correct version of mpc.h... no
        configure: error: Building GCC requires GMP 4.2+ and MPFR 2.3.2+.
        Try the --with-gmp and/or --with-mpfr options to specify their locations.
        Copies of these libraries' source code can be found at their respective
        hosting sites as well as at ftp://gcc.gnu.org/pub/gcc/infrastructure/.
        See also http://gcc.gnu.org/install/prerequisites.html for additional info.
        If you obtained GMP and/or MPFR from a vendor distribution package, make
        sure that you have installed both the libraries and the header files.
        They may be located in separate packages.
So you will need to add the missing dependencies:

        :::bash
        $ sudo apt-get install libgmp3c2 libmpfr-dev
If you are working in a 64bits-machine, the compilation will probably fail if you do not write the following before start compiling ([link](http://ubuntuforums.org/showthread.php?t=1877944)):

        :::bash
        $ sudo apt-get install libc6-dev-i386 fastjar zip
Finally, we can compile:

        :::bash
		$ make
After 3-4 hours (in my case) you can run `sudo make install` if you want to use the latest version of GCC. I did:

        :::bash
        $ sudo make install
And everything was broken :) Don't worry. Since the new compiler is installed, it is going to be called by default when trying to compile something but it is not configured. Keep reading.
Both if you don't want to install GCC trunk version or you already did, to solve the initial problem, the final step is to copy the file we just compiled

		srcdir/x86_64-unknown-linux-gnu/libstdc++-v3/src/.libs/libstdc++.so.6.0.18
to `/usr/lib/` or any other folder such as `/usr/local/lib/` in my case (it could be installed there by another program). If copied to this folder, go to bashrc and include the following line:

        $ gedit ~/.bashrc
        $ LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib ; export LD_LIBRARY_PATH
        $ sudo gedit /etc/ld.so.conf
Then run

		:::bash
        $ sudo /sbin/ldconfig
Once again, generate the symbolic links:

        :::bash
        $ sudo ln -s libstdc++.so.6.0.18 libstdc++.so
        $ sudo ln -s libstdc++.so.6.0.18 libstdc++.so.6
After all this stuff, a lot of things have been done so it is probable that some symbolic links or .so files are messed up. Currently, all these commands worked for me but the state I left my computer is a mess (I have 3 different symbolic links for `libstdc++.so.6` and `libstdc++.so.5`) But so far, it works :)

Of course, the mex files of Matlab have to be compiled again.

Useful notes:

- With `$ ls -al` it is possible to see where it is a library pointing. There are other commands for this but I can't remember.