# Computational Geometry
The task is to implement Graham's scan algorithm in the file convex_hull.py, with the following functions:

a. findBottomLeft – Given a list of Point objects (the class is defined in mainTrain), it should return the bottom-leftmost point. If there are multiple such points, return the leftmost among them.

b. sortCCW – Given a list of points, it should sort them in counterclockwise order based on the angle formed in function a'.

c. isLeftTurn – Given three points, imagine moving from the first to the second and now heading towards the third. If a left turn is required, return True; otherwise, return False.

d. grahamScan – Given a list of all points, return (using the above helper functions) a list of points representing the minimal convex hull in O(n log n) time.

The test checks the helper functions for a simple case and the algorithm for 50 random points. Afterward, an additional check is performed for 50 more random points, removing one point for each outside the returned convex hull (a total of 50 points removed).

At the end of the downloaded mainTrain, there is a plot for the graph. 
