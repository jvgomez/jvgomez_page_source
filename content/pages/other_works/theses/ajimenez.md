Title: Centralized Control for Robot Fleets
Category: Theses
Status: hidden

[TOC]

## Author
- Adrián Jiménez
- __Score__: 9.4/10

## Objective
The objective is to design a system involving artificial intelligence (AI) and robotics for experimental purposes in path planning. In an experimental environment and through a web cam be able to identify and localize a fleet of robots as well as control it by radiofrequency communication. The initial problem is reduced to one where the robot sees the rest of the objects as obstacles. These obstacles can be passive like a wall or active like other robot of the fleet, but it does not matter the nature of the obstacle itself because when doing path planning we will have to avoid both of them.

Concretely, the robots are labeled with colors and a webcam is used to identify their poses (positions and orientations). Also, the serial communication is also implemented.


## Results

{% youtube zz9dKCVFLJg 400 400 %} {% youtube L4XBJ6ynhR0 400 400 %}
{% youtube QEk42Ov_9gg 400 400 %} {% youtube -dKB3Z0Js10 400 400 %}

<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/ajimenez1.png" style="width: 38%; height: auto;"/>
<img src="{filename}/images/theses/ajimenez2.png" style="width: 61%; height: auto;"/>
<p></p>
<p class="caption">Left - Open source robots employed. Right - Color calibration procedure. </p>
</div>

<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/ajimenez3.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Real position and surface of the robots identified. </p>
</div>

## Documentation and Source
- [Report (spanish)]({filename}/files/works/theses/ajimenez_report.pdf)
- [Abstract (english)]({filename}/files/works/theses/ajimenez_abstract.pdf)
- [Presentation (spanish)]({filename}/files/works/theses/ajimenez_presentation.zip)
- [Source code]({filename}/files/works/theses/ajimenez.zip)
- [Printable robot 3D CAD models](http://www.thingiverse.com/thing:18264)