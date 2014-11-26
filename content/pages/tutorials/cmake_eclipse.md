Title: How to configure a C/C++ project with Eclipse and CMake
Category: Tutorials
Status: hidden

[TOC]

I'm not an expert in CMake. Actually, I always programmed in Geany which is the most simple IDE and I run cmake . and make directly from the terminal or modifying a little bit the Geany configuration. Now, I'm starting to work with Eclipse (since is one of the most used environments for many many different programming languages). It was not easy to create a project which works with CMake (I want my programs to be as cross-platform as possible, so this was a requirement). The main reference site for this is the [CMake WikiSite](http://www.cmake.org/Wiki/CMake:Eclipse_UNIX_Tutorial).

I will explain here two types: the recommended method and the manual method.

## Changing the user name in Eclipse
I know this is not the correct place for this one, but it is just a small trick. The variable `${user}` in Eclipse takes the OS name, and this one is probably not the best for our templates. Just go to `eclipse.ini` (in the root folder of Eclipse) and add the following line:

    -Duser.name=<Insert name>

A brief example of my `eclipse.ini` (the necessary part, the .ini is larger):

	:::bash
    __openFile__
    -vmargs
    -Dosgi.requiredJavaVersion=1.6
    -XX:MaxPermSize=256m
    -Xms40m
    -Xmx384m
    -Duser.name=Javier V. Gómez

## Using CMake Eclipse CDT4

Starting with version 2.6.0 CMake includes a generator for Eclipse CDT 4.0 or newer. It works together with the Makefile generators (i.e. "Unix Makefiles", "MinGW Makefiles", "MSYS Makefiles", and maybe "NMake Makefiles"). This generator creates a set of `.project/.cproject` files that can be imported in Eclipse as an "Existing Eclipse project".

Note that CMake 2.4.x users may follow instructions provided [here](http://www.cmake.org/Wiki/CMake:Eclipse_UNIX_Tutorial) in order to setup an Eclipse+CMake usage _manually_.

Using the Eclipse CDT4 generator isn't different than using any other CMake generator.  It works for in-source and out-of-source builds.  In this example, we'll assume that the source tree of the project is `/home/eric/certi_src`.

Be sure to have a proper CMakeLists.txt file in the src directory.  For instance, if you get an error such as Undefined Reference when you import into Eclipse, make sure you have the `TARGET_LINK_LIBRARIES` set correctly.

	:::cmake
	TARGET_LINK_LIBRARIES(AwesomeProjectMain ITKCommon ITKIO ITKBasicFilters)

On Linux, these libraries may exist in the bin subdirectory under the ITK Root Directory with a `.a` extension.

Create a build directory, go there and run CMake (see below for commandline). Make sure you set your `CMAKE_BUILD_TYPE` to `Debug` if you want to debug your project with gdb inside of Eclipse CDT. This is not done automatically (especially when using `cmake-gui`)

	:::bash
    mkdir /home/eric/certi_build
    cd /home/eric/certi_build
    cmake -G"Eclipse CDT4 - Unix Makefiles" -D CMAKE_BUILD_TYPE=Debug ../certi_src

<dl class="section note"><dt>Important Note</dt><dd>Your project name should be different from your executable name and different from your build folder name. Otherwise, Eclipse will NOT pick up your executable as you build them.</dd></dl>

Since my build folder name is `certi_build`, a `CMakeLists.txt` file like below should work (notice the difference in project name and executable name)

	:::cmake
    PROJECT(AwesomeProject)
    ADD_EXECUTABLE(AwesomeProjectMain
      main.cpp
      util.h
      util.cpp
    )

You will now find two Eclipse files in your build tree:

    certi_build/.project
    certi_build/.cproject

Import the created project file into Eclipse
- Import project using Menu `File->Import`.
- Select `General->Existing projects into workspace`.
- Browse where your build tree is and select the root build tree directory. Keep "Copy projects into workspace" unchecked.
- You get a fully functional eclipse project.

You can edit your `CMakeLists.txt` file inside of Eclipse CDT, a plugin called [CMakeEd](http://www.cthing.com/CMakeEd.asp) can help you with this task. When you edit your `CMakeLists.txt` file, you are recommended to delete your project and reimport it.

### In-Source Builds

In-Source builds are fully supported by the Eclipse project generator.

### Out-Of-Source Builds

Eclipse has two issues with out-of-source builds, the project generator tries to work around them as best as it can. The details are described below.

#### Version Control Integration in Eclipse

Eclipse supports version control systems, e.g. cvs and svn, but for them to work, the project files must be at the root of the source tree. This is not the case with out-of-source builds.  The only way to get version control for your project in Eclipse is to have a separate project in the source tree for this purpose.  You can either create this project manually or tell CMake to create it for you when creating your project files:

    :::bash
	cmake -G"Eclipse CDT4 - Unix Makefiles" -DECLIPSE_CDT4_GENERATE_SOURCE_PROJECT=TRUE ../certi_src

This will create your normal project in the build tree and additionally an extra project in the source tree, we call it the _source-project_. In Eclipse you can then import this source-project the same way as you import the normal project. This way you'll have two (or more) projects, one for browsing the sources and doing version control, the other for building your project.

#### Accessing the Source and Advanced Editing Features

Eclipse has advanced support for editing C/C++ sources, including code navigation, autocompletion etc.
For that to work the sources must be inside the project (the additional source-project from above is not inside the project). The Eclipse project generator therefore creates a linked resource to the source tree in the Eclipse project. This makes the C/C++ features work.

This linked resource isn't created if the build directory is a subdirectory of the source directory because Eclipse __doesn't__ allow to load projects which have linked resources pointing to a parent directory. So we recommend to __create your build directories not as children, but as siblings__ to the source directory.  E.g.:

    /path/to/source
    /path/to/build

### Discussion about limitations

If you would like to monitor the changes to the EclipseCDT4 support, you can view the following links which contain the git history log for changes to the two main files:
- http://cmake.org/gitweb?p=cmake.git;a=blob;f=Source/cmExtraEclipseCDT4Generator.h;hb=HEADcmExtraEclipseCDT4Generator.h
- http://cmake.org/gitweb?p=cmake.git;a=blob;f=Source/cmExtraEclipseCDT4Generator.cxx;hb=HEADcmExtraEclipseCDT4Generator.cxx

Eclipse assumes project files (i.e. .project and .cproject) _must be at the root of the project tree_ __and__ a project may be handled by a versioning system (CVS, SVN, ...) if _the root project tree is_.

This assumption clashes with the fact that CMake generated files should _stay in the build tree_ whereas source files (which are usually those handled by a versioning system) reside _in the source tree_.

There has been a fair amount of discussion regarding this problem of the Eclipse CDT4 Generator:

- [Trouble with CMake + Eclipse + SVN/CVS](http://www.cmake.org/pipermail/cmake/2007-October/016956.html)
- [__Updated__ Eclipse CDT4 CMake Generator - Pre-Alpha version](http://www.cmake.org/pipermail/cmake/2007-August/015504.html)
- [ Partially Shared project using Eclipse CDT (cdt-dev ML)](http://dev.eclipse.org/mhonarc/lists/platform-cvs-dev/msg00462.html)

## Manual Method
### Create an Eclipse Project
Create an Eclipse [CDT (C/C++ Development Tooling) project](http://www.eclipse.org/cdt/) using the `File > New > C++ Project` command for your C++ project, or `File > New > C Project` for a C project.

Do not create the project using the [CMake Eclipse project generator](http://www.cmake.org/cmake/help/cmake-2-8-docs.html#gen:EclipseCDT4-UnixMakefiles).

### Create Eclipse Make Targets

The conventional approach to [using CMake with Eclipse](http://www.cmake.org/Wiki/CMake:Eclipse_UNIX_Tutorial) is to create an external tool in Eclipse. However, a `Make Target` is simpler, and because it is stored in the Eclipse `.project` file, you can check it into your version control system and it will work in every one of your working copies, on every computer.

Create a `Make Target` for each configuration that you want to build.  Here I assume that you have the usual Release and Debug configurations:

- Display the Make Target window using the `Window > Show View > Make Target` menu command. It should appear on the right, with the Outline window.
-  Select the folder for the project for which you want to add CMake.  CMake will run with this folder as its working directory.
-  Right click on the folder and select New from the context menu.  The Create Make Target dialog will appear.
    - Type `Target name CMake Release`
    - In Make target, deselect Same as the target name, and make sure that the Make target field is empty
    - In Build Command, deselect Use builder settings and set the Build command to `cmake -E chdir Release/ cmake -G "Unix Makefiles" ../ -DCMAKE_BUILD_TYPE:STRING=Release`
    - Click OK
- Repeat, this time for Target name CMake Debug, and Build command, `cmake -E chdir Debug/ cmake -G "Unix Makefiles" ../ -DCMAKE_BUILD_TYPE:STRING=Debug`
- Create the Release/ and Debug/ directories `mkdir Release Debug`

### Set Up the Eclipse CDT Builder

Next, set up the CDT builder to run the Makefiles that CMake builds.

- Right click on a CDT project.  In the context menu, select Properties.
    - On the left, select C/C++ Build
    - Set Configuration to Release
    - Choose the Builder Settings tab
    - Deselect Use default build command
    - Specify the Build command: `make -C ${ConfigName}`

- Deselect Generate Makefiles automatically
- Make the Build directory field blank

- Choose the Behavior tab
    - Select Build (Incremental build) and specify the target name all
    - Select Clean and specify the target name clean

- Set Configuration to Debug
    - Choose the Builder Settings tab
        - Set all values exactly the same as the Release configuration
    - Choose the Behavior tab
        - Set all values exactly the same as the Release configuration
    - Click OK

## Build the Project

Use CMake to generate an out-of-source GNU Make build system:

- In the Make Targets window, double click on CMake Release or CMake Debug to generate the GNU Make build system in Release/ or Debug/, respectively
- If necessary, edit your CMakeLists.txt control files
- Delete the contents of the corresponding build directory. For example: `rm -r Release/*` and repeat.

Actually, for minor edits to your `CMakeLists.txt` control files, you need not delete the build directory. However, I cannot tell you exactly what the threshold for _minor edits_ is.

Now, build the project the usual way with Eclipse:

- Select the configuration to build (Release of Debug) with the `Project > Build Configurations > Set Active` command
- Build with the `Project > Build Project` command
- Edit your source code files, and repeat

### Source
This information was directly taken from [CMake.org](http://www.cmake.org/Wiki/Eclipse_CDT4_Generator) and [Voom.net](http://www.voom.net/use-cmake-with-eclipse). Thank you for sharing with open-source license! This page pretends to be as a connection point for the author of this wiki (I'm just trying to avoid googling about it everytime I need this info :) )