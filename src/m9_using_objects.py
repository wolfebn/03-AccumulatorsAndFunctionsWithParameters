"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Bryan Wolfe.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()
def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # Done: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------

    window = rg.RoseWindow(400, 400)
    center_point = rg.Point(200, 200)
    center_point2 = rg.Point(100,100)
    rad = 14
    rad1 = 10
    circle1 = rg.Circle(center_point,rad)
    circle1.fill_color = 'green'
    circle2 = rg.Circle(center_point2, rad1)
    circle1.attach_to(window)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()
def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # Done: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(400, 400)
    center_point = rg.Point(200, 200)
    rad = 14
    circle1 = rg.Circle(center_point, rad)
    circle1.fill_color = 'blue'
    x1 = 50
    x2 = 75
    y1 = 50
    y2 = 100
    pt1 = rg.Point(x1, y1)
    pt2 = rg.Point(x2, y2)
    rect1 = rg.Rectangle(pt1, pt2)
    rect1.attach_to(window)
    circle1.attach_to(window)
    window.render()
    window.close_on_mouse_click()
    print(1)
    print(circle1.fill_color)
    print(center_point)
    print(200)
    print(200)
    print(1)
    print('none')
    centerx = (x1+x2)/2
    centery = (y1+y2)/2
    centerrect = rg.Point(centerx, centery)
    print(centerrect)
    print(centerx)
    print(centery)

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # Done: 4. Implement and test this function.
    window = rg.RoseWindow(400,400)
    pt1 = rg.Point(50,50)
    pt2 = rg.Point(100,100)
    pt3 = rg.Point(150, 150)
    pt4 = rg.Point(300, 150)

    line1 = rg.Line(pt1, pt2)
    line2 = rg.Line(pt3, pt4)
    line2.thickness = 5
    center = line2.get_midpoint()
    x = center.x
    y = center.y
    line1.attach_to(window)
    line2.attach_to(window)
    window.render()
    print(center)
    print(x)
    print(y)
    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
