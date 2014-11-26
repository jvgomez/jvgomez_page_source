Title: O(n) Fast Marching Methods: Implementation and Comparison
Category: Theses
Status: hidden

[TOC]

## Author
- Pablo Muñóz
- __Score__: 8.4/10

## Objective
There are many different Fast Marching Method (FMM) versions. Some of them are O(n log n) (with n as the number of cells of the map). Others are O(n). Altuogh the literature includes some comparisons among different methods, there is not a exahustive comparison including all of the algorithms.

In this project, the 6 different versions known (all we were able to find) are implemented, impartially, and exahustively compared.

## Results
<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/pmunoz1.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Time comparison for a 2D grid with start in the center.</p>
</div>
<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/pmunoz2.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Time comparison for a 3D grid with start in the center.</p>
</div>
<div class="figure align-center" style="width: 100%; height: auto;">
<img src="{filename}/images/theses/pmunoz3.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">Example of one of the FMM versions solving a maze. </p>
</div>

## Documentation and Source
- [Report (spanish)]({filename}/files/works/theses/pmunoz_report.pdf)
- [Source](http://github.com/jvgomez/fastmarching)
