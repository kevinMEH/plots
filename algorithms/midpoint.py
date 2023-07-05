import numpy as np

def midpointRecordEveryStep(start, startValue, startDerivative, end, stepSize, derivativeFunction):
    result = [ startValue ]
    while start < end:
        startDerivative = derivativeFunction(start + stepSize/2, startValue + stepSize/2 * derivativeFunction(start, startValue, stepSize, startDerivative), stepSize, startDerivative)
        start += stepSize
        startValue += stepSize * startDerivative
        result.append(startValue)
    return np.asarray(result)