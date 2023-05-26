#ifndef RANDOM
#define RANDOM

#include "inttypes.h"

typedef struct XorshiftState {
    uint64_t x[2];
} XorshiftState;

void setXorshiftState(uint64_t first, uint64_t second);
uint64_t xorshift();
// Random between 0 and 1 not including 1
double xorshiftDouble();

double normalDistribution(double center, double deviation);

#endif