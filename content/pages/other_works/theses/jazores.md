Title: Floor segmentation using Delta-E divergence
Category: Theses
Status: hidden

[TOC]

## Author
- Javier Azores

## Objective
The objetive is to use a RGB-D camera. Detect the floor _close_ to the camera with the 3D data and then learn color patterns in order to analyze the rest of the RGB information. The final effect is like if the 3D camera range was increased.

This project is a continuation of the [Jose Pardeiro's Bachelor Thesis]({filename}/pages/other_works/theses/jpardeiro.md). In this case, the floor color is analyzed using the Delta-E divergence measure (insetad of the Mahalanobis distance). The main algorithm change also a bit. Now, neighborhoods are considered when labelling the ground. This improves the results of the floor segmentation and estimation.

## Results
<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/jazores1.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Results for differnt parameters. Green: labelled as floor by 3D data. Blue: estimated as floor by the algorithm.</p>
</div>

## Documentation and Source
- [Report (spanish)]({filename}/files/works/theses/jazores_report.pdf)
- [Source](https://github.com/jvgomez/FloorReconstruction): The code will be added to that repository, but it is not ready yet.[]({filename}/jazores/code)
