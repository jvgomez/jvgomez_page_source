Title: Hokuyo-Dynamixel Coupling for 3D Mapping
Category: Other Works

[TOC]

<div class="figure align-center" style="width: 100%; height: auto;">
<img alt="Test3D" src="{filename}/images/3dmapping/me3d.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">FM toolbox test output</p>
</div>

<div class="figure align-right" style="width: 40%; height: auto;">
<img alt="Cloud" src="{filename}/images/3dmapping/cloudtv.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">3D point cloud visualization, TV was there recording!</p>
</div>

My 3D Mapping device is composed by a Hokuyo UTM30-LX (Top-URG) rangefinder and a Robotis Dynamixel EX-106+ motor. I rely on [ROS](http://www.ros.org/) in order to use both devices.  [Raúl Villajos]({filename}/pages/works/theses/rvillajos.md) did some specific ROS nodes.

{% youtube n1OJ9bcBAIg 400 400 %}

<div class="figure align-right" style="width: 40%; height: auto;">
<img alt="Coupled hardware" src="{filename}/images/3dmapping/coupled.jpg" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Hokuyo + Dynamixel coupled with a custom-designed 3D-printed piece.</p>
</div>

## Hokuyo - Dynamixel coupling
Following the OpenSource philosophy (both hardware and software) I've uploaded different versions of the coupling I've designed to attach the Hokuyo to the Dynamixel.It works very well and the data doesn't require software adjustments due to wrong dimensions (the rotation axis of the motor is _exactly_ the receiver point of the laser).

- [Download the sketch with the dimensions]({filename}/files/works/3dmapping/dimensions.zip).


<br>
<br>
<br>

### 3D Model - Pro version
Designed to be printed with a professional 3D printer (or a very good one).

- [Download source]({filename}/files/works/3dmapping/3dprint_pro.dwg)

<div class="figure align-center" style="width: 75%; height: auto;">
<img alt="3D Model" src="{filename}/images/3dmapping/3dprint_pro.png" style="width: 49%; height: auto;"/>
<img alt="Printed piece" src="{filename}/images/3dmapping/3dprint_pro_real.jpg" style="width: 49%; height: auto;"/>
<p></p>
<p class="caption">Coupling (model and real) built with a profressional 3D printer.</p>
</div>

<br><br><br><br>
<br><br><br><br>
<br><br><br><br>
<br><br><br>

### 3D Model - Simplified version
Perfect for low-cost 3D printers. Created with the extint Object Objected Mechanics Library.

- [View part in Thingiverse](http://www.thingiverse.com/thing:14842)
- [Download STL]({filename}/files/works/3dmapping/3dprint_simple.stl)

<div class="figure align-center" style="width: 75%; height: auto;">
<img alt="3D Model" src="{filename}/images/3dmapping/3dprint_simple.png" style="width: 47%; height: auto;"/>
<img alt="Printed piece" src="{filename}/images/3dmapping/3dprint_simple_real.jpg" style="width: 49%; height: auto;"/>
<p></p>
<p class="caption">Coupling (model and real) built with a low-cost, open source 3D printer.</p>
</div>

<br><br><br><br>
<br><br><br><br>
<br><br><br><br>
<br>

### 3D Model - Minimalist
Perfect to be manufactured with a metal sheet.

- [Download source]({filename}/files/works/3dmapping/metal_simple.dwg)

<div class="figure align-center" style="width: 75%; height: auto;">
<img alt="3D Model" src="{filename}/images/3dmapping/metal_simple.png" style="width: 49%; height: auto;"/>
<img alt="Metal piece" src="{filename}/images/3dmapping/metal_simple_real.jpg" style="width: 41%; height: auto;"/>
<p></p>
<p class="caption">Coupling (model and real) built with a metal sheet.</p>
</div>