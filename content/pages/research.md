Title: Research
Category: Main

[TOC]

<dl class="section note"><dt>Note</dt><dd> Not all my research code is available. Just because I don't think it is worthy. Contact me if you are interested anyway.</dd></dl>

<div class="figure align-right" style="width: 200px; height: auto;">
<img alt="Path planning example" src="{filename}/images/pathplanning.png" style="width: 200px; height: auto;"/>
<p></p>
<p class="caption">Fast Marching in a triangulation.</p>
<!--
<p class="legend"> This is a legend</p>
-->
</div>

## Robotics and AI

Mainly I focus on two big fields: path planning (learning, multirobot planning...) and 3D point cloud processing/environment modeling.

### Path Planning
How would you tell a robot to go from one place to another? Or how to move its arms? What if it is an intelligent car?
There are several different path planning problems and I have explored some of them.

Most of my research is based in the __Fast Marching Method__ and a custom, very useful version: [__Fast Marching Square (FM2)__]({filename}/pages/research/fm2.md).

I am also investigating _sampling-based_ algorithms, focusing on the __Fast Marching Trees (FMT*)__. These algorithms are very fast but it is hard to ensure that they will provide an optimal solution. They work well in many dimensions, where other methods become really slow. In this case, my objective is twofold:
- Try to make the algorithm as fast a possible.
- Take into account kinematic (and dynamic) constrains.

The work in this area is done in close collaboration with [Marco Pavone's Autonomous Systems Lab](http://web.stanford.edu/~pavone/) from [Stanford University](http://stanford.edu/).

<div class="figure align-left" style="width: 100%; height: auto;">
<img alt="Path planning example" src="{filename}/images/fmt.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Fast Marching Trees in a 3D (position+orienation) scenario in OMPLapp.</p>
<!--
<p class="legend"> This is a legend</p>
-->
</div>

<br>
<br>

<div class="figure align-left" style="width: 200px; height: auto;">
<img alt="Path planning example" src="{filename}/images/missing.png" style="width: 200px; height: auto;"/>
<p></p>
<p class="caption">Fast Marching in a triangulation.</p>
<!--
<p class="legend"> This is a legend</p>
-->
</div>

### 3D Point Cloud Processing and Environment Modeling
I did not focus too much in this are. These are some small works I did to introduce myself in this fascinating world. Most of my work in this area is as a Bachelor's thesis advisor. However, my last goal is to combine environment modeling with sampling-based planners. The same datastructures and basic algorithms (KD-trees, Nearest-Neighbours, etc) are used in both fields, so there should be a way to get an advantage of this.

If you are interested, please check out the [Other Works]({filename}/pages/other_works.md) section to find more works in this area.


{% youtube n1OJ9bcBAIg 400 400 %} {% youtube RaVahqgE2-c 400 400 %}

### Some Fun
Some geeky stuff I developed during my Master's degree. An open-source hardware/software, 3D-printed minirobot which is able to follow a circuit (I won the class competition!) and an Arduino-based teleoperation framework (Arduino --WLAN--> PC --TCP/IP--> Servo)

{% youtube xKkJGlzjeCM 400 400 %} {% youtube PcBgaaDEmk0 400 400 %}

## SGPS
<div class="figure align-right" style="width: 250px; height: auto;">
<img alt="SGPS logo" src="{filename}/images/sgps.png" style="width: 250px; height: auto;"/>
</div>

__S__unlight intensity-based __G__lobal __P__ositioning __S__ystem. Find a way out to localize outdoor objects using energy efficient systems and algorithms. It is a continuation of my Bacherlor's thesis, collaborating with Frode Eika Sadness and Peyman Mirtaheri. Research based on the Frode's paper: _An energy efficient localization strategy for outdoor objects based on intelligent light-intensity sampling_.

I've created a Wiki in which all the code and useful information is uploaded to spread the idea and SGPS so everybody can research about it and get a real good system: [SGPS Project](http://sgpsproject.sourceforge.net/wiki)

This is a personal research which I carry out with some friends.