# VisiLibity v1

A C++ Library for Planar Visibility Computations

See also <https://karlobermeyer.github.io/VisiLibity1/>.



## Using

Source files are in `src/`. To use VisiLibity in your C++ program, you simply
need to place an `#include "visilibity.hpp"` directive at the beginning of your
program and link with `visilibity.cpp` when compiling. For details on
particular classes and methods, refer to the source code documentation page to
which there is a link on the project page
<https://karlobermeyer.github.io/VisiLibity1/>.

The files `main.cpp` and `makefile` (listed below) provide an elementary example
of a C++ program which uses VisiLibity.  Once compiled (`make main`), this
program provides a text interface which will
1. read an environment and guard locations from files given as command line
   arguments,
2. check the geometric validity of these inputs (edges of the environment do not
   cross each other, guards are contained in the environment, etc.),
3. display environment and guards' data and statistics, and
4. compute and display the coordinates of a visibility polygon of a guard chosen
   by the user.

The environment representation and the guard locations can be read from any file
in the (human-readable) format demonstrated in
`example1.environment`,
`example2.environment`, and
`example1.guards`.

A Matlab MEX interface is provided in
`visibility_polygon_demo.m`,
`shortest_path_demo.m`,
`visibility_graph_demo.m`,
`in_environment.cpp`,
`visibility_polygon.cpp`,
`shortest_path.cpp`, and
`visibility_graph.cpp`.
First the files `in_environment.cpp`, `visibility_polygon.cpp`,
`shortest_path.cpp`, and `visibility_graph.cpp` should be compiled into MEX
files (see instructions at the heads of the files themselves). The scripts
`visibility_polygon_demo.m` and `shortest_path_demo.m` can be used to display a
graphical representation of the supplied environment files while the user
selects points with the mouse so that the visibility polygon of, resp. shortest
path between, points are displayed. The script `visibility_graph_demo.m` can be
used to display a graphical representation of an environment together with the
visibility graph of a set of points specified within the script.

For more details on the examples, see the file descriptions below and the
comments in the files themselves.



##  Index of files with brief descriptions

File: `./COPYING`
Description:  a copy of the GNU General Public License.

File: `./COPYING.LESSER`
Description:  a copy of the GNU Lesser General Public License.

File: `./src/visilibity.hpp`
Description: the VisiLibity header file.

File: `./src/visilibity.cpp`
Description: the VisiLibity implementation file.

File: `./src/main.cpp`
Description: an example program using VisiLibity.  After compiling with the
provided makefile (just type make in the `./src/` directory), and run the
program with the command line `./main example1.environment example.guards`.

File: `./src/makefile`
Description: a makefile for compiling `main.cpp` using g++.

File: `./src/example1.environment`
      `./src/example2.environment`
Description: an example of the human-readable files that VisiLibity uses to
store polygonal environments with holes.  You can use this as a template to
create your own `*.environment` files.  To read and write Environment files, use
the `Environment::read_from_file()` and `Environment::write_to_file()` methods.

File: `./src/example1.guards`
Description: an example of the human-readable files that VisiLibity uses to
store guard positions.  You can use this as a template to create your own
`*.guards` files. To read and write Guards files, use the
`Guards::read_from_file()` and `Guards::write_to_file()` methods.

File: `./src/visibility_polygon.cpp`
Description: MEX file source code to interface VisiLibity's visibility polygon
calculation with Matlab.

File: `./src/in_environment.cpp`
Description: MEX file source code to interface VisiLibity's Point-in-Environment
calculation with Matlab.

File: `./src/shortest_path.cpp`
Description: MEX file source code to interface VisiLibity's shortest path
through a polygon with holes calculation with Matlab.

File: `./src/visibility_graph.cpp`
Description: MEX file source code to interface VisiLibity's visibility graph
calculation, for a set of points in a polygonal environment with holes, with
Matlab.

File: `./src/visibility_polygon_demo.m`
Description: an example Matlab script which uses the the MEX files generated
from `visibility_polygon.cpp` an `in_environment.cpp` (these must be compiled
before running `visibility_polygon_demo.m`).

File: `./src/shortest_path_demo.m`
Description: an example Matlab script which uses the MEX files generated from
`shortest_path.cpp` and `in_environment.cpp` (these must be compiled before
running `shortest_path_demo.m`).

File: `./src/visibility_graph_demo.m`
Description: an example Matlab script which uses the MEX file generated from
`visibility_graph.cpp` (must be compiled before running
`visibility_graph_demo.m`).

File: `./src/read_vertices_from_file.m`
Description: a subroutine of `visibiity_polygon_demonstration.m` and
`shortest_path_demo.m` used to read a VisiLibity style Environment file into a
Matlab cell array.

## Testing
Testing frameworks are available for visibility polygon and shortest path
calculations.

### Visibility polygon calculation testing
TBD

### Shortest path calculation testing

The script `test_shortest_path.sh` will execute all the tests in the `shortest_path_tests` (by default) directory.

Every test requires three files:
1. `<name>.environment`: The environment in which to find a shortest path between two points. Specify this like any other environment file.
2. `<name>.guards`: The location of 2 (two) points in the environment and not in a hole. The first point is the start point and the second point is the end point. The test will calculate the shortest path between those points with respect to the environment defined in `<name>.environment`.
3. `<name>.result`: The vertices of the shortest path between the points defined in <name>.guards in the environment defined in `<name>.environment`.

The test passes when the path specified in the result file matches the path actually calculated by VisiLibity.

## License

VisiLibity:  A Floating-Point Visibility Algorithms Library Copyright (C) 2008
Karl J. Obermeyer (karl.obermeyer@gmail.com)

This file is part of VisiLibity v1.

VisiLibity v1 is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

VisiLibity v1 is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with VisiLibity v1.  If not, see  <http://www.gnu.org/licenses/>.
