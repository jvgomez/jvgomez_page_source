Title: Path planning benchmarking in MoveIt!
Category: Theses
Status: hidden

[TOC]

## Author
- Miguel Mora
- __Score__: 9.8/10

## Objective

<div class="figure align-center" style="width: 33%; height: auto;">
<img src="{filename}/images/theses/mmora2.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Example of one of the paths planned.</p>
</div>

Path planning consists on looking for a set of states along the time for a given system (a robot, a manipulator, a car...) which will drive this system from an initial point towards a goal point. In robotics, there are dozens of different algorithms. Some of them provide optimal paths in terms of length, other in smoothnes, clearance to closest obstacles, etc.

Benchmarking refers to the process of running the same tests in different algorithms (or systems, devices or whatever) so that a set of metrics can be measure and it can be evaluated how a product (or service) behaves under determined circumstances.

The [MoveIt! project](http://moveit.ros.org/), based on [ROS](http://www.ros.org/ ROS), is a software that aims to ease the reserach tasks in robotics platforms relative to mobile manipulation. Among its capabilities, benchmarking for path planning algorithms can be found. However, since MoveIt! is under constant development and the documentation (as always in software) is a bit outdated with respect the software.

This project improves the documentation for the MoveIt! benchmarking capability and includes solutions for the problems found along the way..

## Results

{% youtube afa3ppj4uak 400 400 %} {% youtube kl4WAn7JcUs 400 400 %}

<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/mmora1.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Many poses tested on Manfred robo.</p>
</div>


## Documentation and Source
- [Report (spanish)]({filename}/files/works/theses/mmora_report.pdf)
