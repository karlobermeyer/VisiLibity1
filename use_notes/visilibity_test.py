'''VisiLibity Python example by Ramiro C. of UNC, Argentina.
'''

from __future__ import print_function
import visilibity as vis

# Used to plot the example
import pylab as p

# Used in the create_cone function
import math


def testVisilibity():

    # Define an epsilon value (should be != 0.0)
    epsilon = 0.0000001

    # Define the points which will be the outer boundary of the environment
    # Must be COUNTER-CLOCK-WISE(ccw)
    p1 = vis.Point(0, 0)
    p2 = vis.Point(700, 0)
    p3 = vis.Point(700, 900)
    p4 = vis.Point(0, 900)

    # Load the values of the outer boundary polygon in order to draw it later
    wall_x = [p1.x(), p2.x(), p3.x(), p4.x(), p1.x()]
    wall_y = [p1.y(), p2.y(), p3.y(), p4.y(), p1.y()]

    # Outer boundary polygon must be COUNTER-CLOCK-WISE(ccw)
    # Create the outer boundary polygon
    walls = vis.Polygon([p1, p2, p3, p4])

    # Define the point of the "observer"
    observer = vis.Point(235,400)

    # Uncomment the following line in order to create a cone polygon
    #walls = create_cone((observer.x(), observer.y()), 500, 270, 30, quality= 3)

    # Walls should be in standard form
    print('Walls in standard form : ', walls.is_in_standard_form())

    # Now we define some holes for our environment. The holes must be inside
    # our outer boundary polygon. A hole blocks the observer vision, it works as
    # an obstacle in his vision sensor.

    # We define some point for a hole. You can add more points in order to get
    # the shape you want.
    # The smalles point should be first
    p2 = vis.Point(100, 300)
    p3 = vis.Point(100, 500)
    p4 = vis.Point(150, 500)
    p1 = vis.Point(150, 300)

    # Load the values of the hole polygon in order to draw it later
    hole_x = [p1.x(), p2.x(), p3.x(), p4.x(),p1.x()]
    hole_y = [p1.y(), p2.y(), p3.y(), p4.y(),p1.y()]

    # Note: The point of a hole must be in CLOCK-WISE(cw) order.
    # Create the hole polygon
    hole = vis.Polygon([p2, p3, p4, p1])

    # Check if the hole is in standard form
    print('Hole in standard form: ', hole.is_in_standard_form())

    # Define another point of a hole polygon
    # Remember: the list of points must be CLOCK-WISE(cw)
    p1 = vis.Point(300, 300)
    p2 = vis.Point(300, 500)
    p3 = vis.Point(400, 550)
    p4 = vis.Point(400, 300)

    # Load the values of the hole polygon in order to draw it later
    hole1_x = [p1.x(), p2.x(), p3.x(), p4.x(),p1.x()]
    hole1_y = [p1.y(), p2.y(), p3.y(), p4.y(),p1.y()]

    # Create the hole polygon
    hole1 = vis.Polygon([p1,p2,p3,p4])

    # Check if the hole is in standard form
    print('Hole in standard form: ', hole1.is_in_standard_form())

    # Define another point of a hole polygon
    # Remember: the list of points must be CLOCK-WISE(cw)
    p2 =vis.Point(90, 700)
    p3 =vis.Point(250, 750)
    p4 =vis.Point(220, 600)
    p1 =vis.Point(150, 600)

    # Load the values of the hole polygon in order to draw it later
    hole2_x = [p1.x(), p2.x(), p3.x(), p4.x(),p1.x()]
    hole2_y = [p1.y(), p2.y(), p3.y(), p4.y(),p1.y()]

    # Create the hole polygon
    hole2 = vis.Polygon([p2,p3,p4,p1])

    # Check if the hole is in standard form
    print('Hole in standard form: ', hole2.is_in_standard_form())

    # Define another point of a hole polygon
    # Remember: the list of points must be CLOCK-WISE(cw)
    p1 =vis.Point(330, 700)
    p2 =vis.Point(330, 800)
    p3 =vis.Point(530, 850)
    p4 =vis.Point(530, 790)

    # Load the values of the hole polygon in order to draw it later
    hole3_x = [p1.x(), p2.x(), p3.x(), p4.x(),p1.x()]
    hole3_y = [p1.y(), p2.y(), p3.y(), p4.y(),p1.y()]

    # Create the hole polygon
    hole3 = vis.Polygon([p1,p2,p3,p4])

    # Check if the hole is in standard form
    print('Hole in standard form: ', hole3.is_in_standard_form())

    # Define another point of a hole polygon
    # Remember: the list of points must be CLOCK-WISE(cw)
    p1 =vis.Point(230, 50)
    p2 =vis.Point(250, 90)
    p3 =vis.Point(390, 90)
    p4 =vis.Point(390, 50)

    # Load the values of the hole polygon in order to draw it later
    hole4_x = [p1.x(), p2.x(), p3.x(), p4.x(),p1.x()]
    hole4_y = [p1.y(), p2.y(), p3.y(), p4.y(),p1.y()]

    # Create the hole polygon
    hole4 = vis.Polygon([p1,p2,p3,p4])

    # Check if the hole is in standard form
    print('Hole in standard form: ', hole4.is_in_standard_form())

    # Create environment, wall will be the outer boundary because
    # is the first polygon in the list. The other polygons will be holes
    env = vis.Environment([walls, hole, hole2, hole1, hole3, hole4])

    # Check if the environment is valid
    print('Environment is valid : ', env.is_valid(epsilon))

    # Define another point, could be used to check if the observer see it, to
    # check the shortest path from one point to the other, etc.
    end = vis.Point(330, 525)

    # Define another point that the 'observer' will see
    end_visible = vis.Point(415, 45)

    # Necesary to generate the visibility polygon
    observer.snap_to_boundary_of(env, epsilon)
    observer.snap_to_vertices_of(env, epsilon)

    # Obtein the visibility polygon of the 'observer' in the environmente
    # previously define
    isovist = vis.Visibility_Polygon(observer, env, epsilon)

    # Uncomment the following line to obtein the visibility polygon
    # of 'end' in the environmente previously define
    #polygon_vis = vis.Visibility_Polygon(end, env, epsilon)

    # Obtein the shortest path from 'observer' to 'end' and 'end_visible'
    # in the environment previously define
    shortest_path = env.shortest_path(observer, end, epsilon)
    shortest_path1 = env.shortest_path(observer, end_visible, epsilon)

    # Print the length of the path
    print("Shortest Path length from observer to end: ", shortest_path.length())
    print("Shortest Path length from observer to end_visible: ", shortest_path1.length())

    # Check if 'observer' can see 'end', i.e., check if 'end' point is in
    # the visibility polygon of 'observer'
    print("Can observer see end? ", end._in(isovist, epsilon))

    print("Can observer see end_visible? ", end_visible._in(isovist, epsilon))

    # Print the point of the visibility polygon of 'observer' and save them
    # in two arrays in order to draw the polygon later
    point_x , point_y  = save_print(isovist)

    # Add the first point again because the function to draw, draw a line from
    # one point to the next one and to close the figure we need the last line
    # from the last point to the first one
    point_x.append(isovist[0].x())
    point_y.append(isovist[0].y())

    # Set the title
    p.title('VisiLibity Test')

    # Set the labels for the axis
    p.xlabel('X Position')
    p.ylabel('Y Position')

    # Plot the outer boundary with black color
    p.plot(wall_x, wall_y, 'black')

    # Plot the position of the observer with a green dot ('go')
    p.plot([observer.x()], [observer.y()], 'go')

    # Plot the position of 'end' with a green dot ('go')
    p.plot([end.x()],[end.y()], 'go')

    # Plot the position of 'end_visible' with a green dot ('go')
    p.plot([end_visible.x()],[end_visible.y()], 'go')

    # Plot the visibility polygon of 'observer'
    p.plot(point_x, point_y)

    # Plot the hole polygon with red color
    p.plot(hole_x, hole_y, 'r')

    # Plot the hole polygon with red color
    p.plot(hole1_x, hole1_y, 'r')

    # Plot the hole polygon with red color
    p.plot(hole2_x, hole2_y, 'r')

    # Plot the hole polygon with red color
    p.plot(hole3_x, hole3_y, 'r')

    # Plot the hole polygon with red color
    p.plot(hole4_x, hole4_y, 'r')

    # Example of a cone-shape polygon
    cone_point = vis.Point(440,420)
    cone = create_cone([cone_point.x(),cone_point.y()], 150, 0, 45, 3)
    cone_x, cone_y = save_print(cone)
    cone_x.append(cone_x[0])
    cone_y.append(cone_y[0])
    p.plot([cone_point.x()], [cone_point.y()], 'go')
    p.plot(cone_x, cone_y)

    # Show the plot
    p.show()


def save_print(polygon):
    end_pos_x = []
    end_pos_y = []
    print 'Points of Polygon: '
    for i in range(polygon.n()):
        x = polygon[i].x()
        y = polygon[i].y()

        end_pos_x.append(x)
        end_pos_y.append(y)

        print x, y

    return end_pos_x, end_pos_y


# Desc: This function creates a cone-shape polygon. To do that it use
# five inputs(point, radius, angle, opening, resolution).
#   'point': is the vertex of the cone.
#   'radius': is the longitude from 'point' to any point in the arc.
#   'angle': is the direcction of the cone.
#   'resolution': is the number of degrees one point and the next in the arc.
# Return: The function returns a Polygon object with the shape of
#   a cone with the above characteristics.
def create_cone(point, radio, angle, opening, resolution=1):

    # Define the list for the points of the cone-shape polygon
    p=[]

    # The fisrt point will be the vertex of the cone
    p.append(vis.Point(point[0], point[1]))

    # Define the start and end of the arc
    start = angle - opening
    end = angle + opening

    for i in range(start, end, resolution):

        # Convert start angle from degrees to radians
        rad = math.radians(i)

        # Calculate the off-set of the first point of the arc
        x = radio*math.cos(rad)
        y = radio*math.sin(rad)

        # Add the off-set to the vertex point
        new_x = point[0] + x
        new_y = point[1] + y

        # Add the first point of the arc to the list
        p.append( vis.Point(new_x, new_y) )

    # Add the last point of the arc
    rad = math.radians(end)
    x = radio*math.cos(rad)
    y = radio*math.sin(rad)
    new_x = point[0] + x
    new_y = point[1] + y
    p.append( vis.Point(new_x, new_y) )

    return vis.Polygon(p)


if __name__ == "__main__":
    testVisilibity()
