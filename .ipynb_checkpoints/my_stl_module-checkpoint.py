"""Module to analyse the content of a "tiny paper"."""

import math
import matplotlib.pyplot as plt


class Vertex:
    """Class of vertex."""

    def __init__(self, x: float, y: float, z: float):
        """Initializes Vertex instance with its coordonates."""
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass


class Facet:
    """Class of facet, a triangle of vertices."""

    def __init__(self, v1: Vertex, v2: Vertex, v3: Vertex):
        """Initializes Facet instance with its vertices."""
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def normal_unit_vector(self):
        """Return 3D-coordinates of normal unit vector of vetex."""
        pass

    def export_ascii(self):
        """Returns STL format ascii string of vetex."""
        pass

    def intersection_with_plan(self, a, b, c, d):
        """
        Returns list of intersection point between facet edges and plan

        The plan equation is:

        .. math::
           ax + by + cz = d

        Returns
        -------
        list of tuples
            List of intersection points, Each point is represented with
            a 3-uple coordinates. Length of list could be 0, 1 or 2.

        """

        def k_denominator(a, b, c, d, x_A, y_A, z_A, x_B, y_B, z_B):
            """
            Calculates denominator of parameter k.

            k is given with the following equation

            .. math::
               k = \frac{d - a x_A - b y_A - c z_A}
                        {a(x_B - x_A) + b(y_B - y_A) + c(z_B - z_A)}

            Returns
            -------
            float
                Denominator of k.

            """
            pass

        pass


class Solid:
    """Class of solid represented with triangle facets."""

    def __init__(self, name="", file_name=""):
        """Initializes Solid instance."""
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def add_facet(self, facet: Facet):
        """Adds a facet to solid."""
        pass

    def add_facet_list(self, facet_list):
        """Adds a list of facet to solid."""
        pass

    def bounding_box(self):
        """
        Returns the bounding box of the solid.

        Returns
        -------
        x_min : float
            Minimun x-coordinate of the solid.
        x_max : float
            Maximun x-coordinate of the solid.
        y_min : float
            Minimun y-coordinate of the solid.
        y_max : float
            Maximun x-coordinate of the solid.
        z_min : float
            Minimun z-coordinate of the solid.
        z_max : float
            Maximun y-coordinate of the solid.

        """
        pass

    def get_all_facets(self):
        """Returns list of all facets of the solid."""
        pass

    def intersection_with_plan(self, a, b, c, d):
        """
        Returns list of line segments point between solid and plan

        The plan equation is:

        .. math::
           ax + by + cz = d

        Returns
        -------
        line_segments_list : list of inner lists
            Inner lists are 3 couples of coordinates
            (x-coordinates, y-coordinates, z-coordinates).
            Each couple gives coordinates of the two points
            which endings line segment that is intersection
            a solid facet with plan

        """
        # x_min, x_max, y_min, y_max, z_min, z_max = self.bounding_box()
        pass

    def extract(self, x_min, x_max, y_min, y_max, z_min, z_max):
        """Returns the part of solid into a given box."""
        pass

    def export_ascii(self, file_name):
        """Write solid into a STL ascii file."""
        pass

    def import_ascii(self, file_name):
        """Initialize solid with content of a STL ascii file."""
        pass


def cube_case_study():
    """Studies the case of a cube."""
    pass


def sphere_poly12_case_study():
    """Studies the case of a teapot."""
    pass


def chess_pawn_case_study():
    """Studies the case of a chess_pawn."""
    pass


def teapot_case_study():
    """Studies the case of a teapot."""
    pass


def main(case_name="chess_pawn"):
    """Run a study case, default "chess_pawn"."""
    match case_name:  # cube, chess_pawn, teapot
        case "cube":
            cube_case_study()
        case "sphere_poly12":
            sphere_poly12_case_study()
        case "chess_pawn":
            chess_pawn_case_study()
        case "teapot":
            teapot_case_study()
        case "all":
            cube_case_study()
            sphere_poly12_case_study()
            chess_pawn_case_study()
            teapot_case_study()


if __name__ == "__main__":
    # case_name: cube, sphere_poly12, chess_pawn, teapot
    main(case_name="all")
