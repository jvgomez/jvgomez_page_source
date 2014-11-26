Title: n-Dimensional Gridmaps: Formulation and Implementation
Category: Other Works
Status: hidden

[TOC]

It all started in a cold winter morning, after spending 2 weeks trying to create a hierarchy of C++ classes to implement functions valid to any kind of grid map, it turned out that the best solution were to work with grid indices and forget about coordinates! This way we can parametrize everything. "There should be something on the Internet about this". After a few hours looking for how to extract neighbors of grids with number and size of dimensions not fixed I decided it was time to try it by myself...


<div class="figure align-right" style="width: 300px; height: auto;">
<img alt="ND gridmap formulation" src="{filename}/images/ndgridmap/ndgrid_handwriting.png" style="width: 100%; height: auto;"/>
<p></p>
<p class="caption">FM toolbox test output</p>
</div>


Grid maps are extensively used in many different algorithms. Among the different grid map types we are focusing on rectangular (or cubic) grid map with a priori unknown number of dimensions. We are detailing the main problems that arise when working with this type of data structure: extraction and validation of 4-connectivity neighbors for a given cell, conversion from index to coordinates (and vice-versa) and the mathematical generalization to n-dimensional grids. Also, we are detailing a generic implementation available as free software.

In this page I posted a document (and its sources) to understand the mathematical formulation and generalization of n-dimensional grid maps. Also a link to my implementation of a grid map of n dimension is provided. The main characteristics here are that it is easy to use.

### Downloads
- [Report with the detailed formulation]({filename}/files/works/ndneighbors/nd-neighbors.pdf)
- [Report and image sources]({filename}/files/works/ndneighbors/nd-neighbors.zip)

### Source code
- [Biicode block](https://www.biicode.com/jvgomez/ndgridmap): Recommended! Check out my [Path Planning tutorial]({filename}/pages/tutorials/fm_biicode.md) to learn how to use it.
- [Github repository](https://github.com/jvgomez/fastmarching/tree/master/ndgridmap): Included in my Fast Marching code.

### Generalized neighbors extraction
The formulation for a 2D grid are summarized in the following pixs. Hard to understand if the report has not been read:

For a 2D and 3D grids, neighbors are:

<div class="figure align-right" style="width: 100%; height: auto;">
<img alt="2D Neighbors" src="{filename}/images/ndgridmap/2dgrid.png" style="width: 42%; height:
auto;"/>
<img alt="3D Neighbors" src="{filename}/images/ndgridmap/3dgrid.png" style="width: 57%; height: auto;"/>
<p></p>
<p class="caption">Von-Neumann (4-connectivity) neighbors computation for 2D and 3D grids.</p>
</div>

Therefore, for a nD grid:

<div class="figure align-center" style="width: 50%; height: auto;">
<img alt="nD Neighbors" src="{filename}/images/ndgridmap/ndgrid.png" style="width: 100%; height:
auto;"/>
<p class="caption">Von-Neumann (4-connectivity) neighbors computation for nD grids.</p>
</div>

Obviously, not all the neighbors are valid since the cell queried can be in an edge or in a corner. In the full report it is described how to generalize the neighbors checking.
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<div class="figure align-right" style="width: 50%; height: auto;">
<img alt="Coordinates to index" src="{filename}/images/ndgridmap/coord2idx.png" style="width: 100%; height:
auto;"/>
<p class="caption">Von-Neumann (4-connectivity) coordinates to index conversion.</p>
</div>

### Helper functions
#### Conversion from Coordinates to Index

<br>
<br>
<br>

<div class="figure align-right" style="width: 50%; height: auto;">
<img alt="Index to coordinates" src="{filename}/images/ndgridmap/idx2coord.png" style="width: 100%; height:
auto;"/>
<p class="caption">Von-Neumann (4-connectivity) index to coordinates conversion.</p>
</div>

#### Conversion from Index to Coordinates