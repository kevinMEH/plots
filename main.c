#include <stdio.h>
#include "./library/basic_structures.h"
#include "./library/polynomial.h"
#include "./library/interpolate.h"

int main() {
    Point points[6];
    points[0] = (Point) { -5, 12.0577 };
    points[1] = (Point) { -10, -2.40083 };
    points[2] = (Point) { -20, -4.83701 };
    points[3] = (Point) { -30, -1.46678 };
    points[4] = (Point) { -35, 0.625988 };
    points[5] = (Point) { -40, 2.86098 };
    Polynomial polynomial = createPolynomial(5);
    lagrange(points, 6, &polynomial);
    for(int i = 0; i < polynomial.numTerms; i++) {
        printf("%.9lf x^%d\n", polynomial.terms[i].coefficient, i);
    }
    deletePolynomial(&polynomial);
    return 0;
}