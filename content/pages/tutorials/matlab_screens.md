Title: Java bug in Matlab when plotting with many monitors
Category: Tutorials
Status: hidden

When you have more than one monitor, usually Matlab throws an error related with Java when new figures appear in the monitor in which is not Matlab. To solve this, go to `<dir to Matlab>/toolbox/local`:

    :::bash
    $ sudo gedit matlabrc.m

Add to the end of the file:

	:::matlab
    % Needed to fix dual monitor setup:
    set(0,'DefaultFigureRenderer','OpenGL')
    set(0,'DefaultFigureRendererMode', 'manual')