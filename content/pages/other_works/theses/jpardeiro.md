Title: Walkable ground learning and estimation
Category: Theses
Status: hidden

[TOC]

## Author
- Jose Pardeiro
- __Score__: 10/10
- __Sept. 10th 2013__: An extension of this work has been accepted in the [1st Iberian Robotics Conference ROBOT2013](http://www.car.upm-csic.es/robot2013/).

## Objective
The objective is to implement and adapt an algorithm which is able to detect the walkable ground next to the robot. From its colour characteristics, models of ground are learnt. Later, with an RGB camera the environment of the robot is analyzed in order to estimate ground with the same color characteristics.

The results are that we are able to estimate walkable ground in places which are farther away from the Kinect that its depth range (approximately 6-7 meters). Moreover, we have tested the algorithm in shiny grounds, reducing the depth range to 2 metres (because the rest of the range was lost due to reflections).

Results pictures shows the original RGB image, the walkable ground detected using depth information from the Kinect, and the final result of the algorithm, estimating the rest of the corridor (light blue) within an area of interest automatically computed (green lines).

## Results

{% youtube Ozho3YuLc_8 400 400 %}

<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/jpardeiro1.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">From left to right: Initial image, floor detected with 3D data, floor detection improved with RGB data.</p>
</div>

<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/jpardeiro2.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Red is real ground, obtained with the Kinect camera and the blue points are estimated ground.</p>
</div>

## Documentation and Source
- [Report (spanish)]({filename}/files/works/theses/jpardeiro_report.pdf)
- [Source code](https://github.com/jvgomez/FloorReconstruction)
- [Paper]({filename}/files/pubs/ROBOT2013_floor.pdf): J. Pardeiro, J.V. Gómez, D. Álvarez and L. Moreno, __Learning-based Floor Segmentation and Reconstruction__, Iberian Robotics Conference (ROBOT2013). Madrid, Spain. November, 2013.