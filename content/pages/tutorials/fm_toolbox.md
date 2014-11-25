Title: Fast Marching Toolbox Installation tutorial
Category: Tutorials
Status: hidden

[TOC]


## Get the toolbox
Here I provide the basic information to use the codes I provide based on this toolbox.
- http://www.mathworks.com/matlabcentral/fileexchange/6110-toolbox-fast-marching

<dl class="section note"><dt>Note</dt><dd> <b>DO NOT</b> save the Fast Marching toolbox into the Matlab's toolboxes path. It looks that it does not compile properly in this folder.</dd></dl>

#### More info
- [Gabriel Peyré's website](http://www.ceremade.dauphine.fr/~peyre/)
- [numerical tours](http://www.ceremade.dauphine.fr/~peyre/numerical-tour/tours/ numerical tours).


### System Prerequisites
- Set your [Matlab supported compiler](http://www.mathworks.es/support/compilers/R2013b/index.html?sec=win64).
- For Linux users, install `build-essential` package:

```
sudo apt-get install build-essential
```


## Compiling the toolbox
- Unzip it in the folder you want and set the Matlab workspace into that folder.
- Before compiling the mex functions, you will probably need to set up your compiler:

	```
    mex -setup
	```

And follow the instructions. Working with Ubuntu, the options were:

    The options files available for mex are:
    1: /usr/local/MATLAB/R2012b/bin/mexopts.sh :
        Template Options file for building gcc MEX-files
    0: Exit with no changes
In my case it wasn't necessary to configure anything. In Windows, this could be problematic... Google will help  you :)

- The next step is to run the compile_mex.m script. For that, just type the command:

    ```
    compile_mex
    ```

 But you will get the following errors:

<pre><span style="color:#ff0000">Error using mex (line 206)
Unable to complete successfully.
Error in compile_mex (line 7)
mex mex/anisotropic-fm//perform_front_propagation_anisotropic.cpp
</span></pre>

 To solve this error, open the compile_mex.m file and comment lines 7 and 8:

<pre><span style="color:#008000">% mex mex/anisotropic-fm//perform_front_propagation_anisotropic.cpp
% mex mex/anisotropic-fm-feth/fm2dAniso.cpp
</span></pre>

 And you will find that everything compiles OK now (although you will get many warnings, probably).

## Setting the Matlab's Path
The next step is to configure the path of Matlab. For that, you will need to include to your path the following folders:

    <path_to_toolbox>/toolbox_fast_marching/data
    <path_to_toolbox>/toolbox_fast_marching/
    <path_to_toolbox>/toolbox_fast_marching/toolbox

<div class="figure align-right" style="width: 200px; height: auto;">
<img alt="Fast Marching Method" src="{filename}/images/fmtestoutput.png" style="width: 200px; height: auto;"/>
<p></p>
<p class="caption">FM toolbox test output</p>
</div>

## Testing

Go to `<path_to_toolbox>/toolbox_fast_marching/tests` and run `test_fast_marching_2d.m` but applying changing line 28 to the following:

    end_points = end_points';

Now, it should work an provide an output something like (when clicking more or less in the center of the image):