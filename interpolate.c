#include <stdio.h>
#include "./library/basic_structures.h"
#include "./library/polynomial.h"
#include "./library/interpolate.h"

int main() {
    int size = 5;
    Point points[size];
    points[0] = (Point) { 0, 1 };
    points[1] = (Point) { 1, 1.77412 };
    points[2] = (Point) { 2, 2.42501 };
    points[3] = (Point) { 5, 3.78075 };
    points[4] = (Point) { 10, 4.65182 };
    Polynomial polynomial = createPolynomial(size);
    fillPowers(&polynomial);
    lagrange(points, size, &polynomial);
    for(int i = 0; i < polynomial.numTerms; i++) {
        printf("%.9lf x^%d\n", polynomial.terms[i].coefficient, i);
    }
    for(int i = 0; i < size; i++) {
        printf("%.9lf, %.9lf\n", points[i].x, polynomialEvaluate(&polynomial, points[i].x));
    }
    deletePolynomial(&polynomial);
    return 0;
}