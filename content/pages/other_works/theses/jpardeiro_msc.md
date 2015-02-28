Title: Integrating FM2 method in ROS and Turtlebot
Category: Theses
Status: hidden

[TOC]

## Author
- Jose Pardeiro
- __Score__: 10/10 proposed to get Honors

## Objective
The objective is to implement the Fast Marching Square (FM2) algorithm and its variations, namely FM2* and FM2Directional, and create the corresponding [ROS](http://www.ros.org/) nodes so that the algorithm can be run in the TurtleBot.

## Results

<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/jpardeiro_msc1.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Results of (from left to right): FM2, FM2* classic version, FM2* proposed version. Path comparisons (same path for all of them in this case).</p>
</div>

<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/jpardeiro_msc2.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Time comparison among the 3 different FM2 versions. The FM2* proposed version is always faster.</p>
</div>

<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/jpardeiro_msc3.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Results of the proposed FM2Directional, which solves the main problem of FM2: non-intuitive paths in open spaces.</p>
</div>

{% youtube Xs5cTYe7duo 400 400 %} {% youtube XvpwdF5Fe7Y 400 400 %}

## Documentation and Source
- [Report (spanish)]({filename}/files/works/theses/jpardeiro_msc_report.pdf)
- [Presentation (spanish)]({filename}/files/works/theses/jpardeiro_msc_presentation.pdf)
- [Fast Marching ROS Node](https://github.com/jpardeiro/fastmarching_node)
- [TurtleBot - FM Node](https://github.com/jpardeiro/turtlebot_fm)
- [Last Fast Marching Code](https://github.com/jvgomez/fastmarching)