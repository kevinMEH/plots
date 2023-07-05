import numpy as np

def heunsRecordEveryStep(start, startValue, startDerivative, end, stepSize, derivativeFunction):
    result = [startValue]
    while start < end:
        start += stepSize
        eulerStepped = startValue + stepSize * startDerivative
        startValue += stepSize * (1/2) * (startDerivative + derivativeFunction(start, eulerStepped, stepSize, startDerivative))
        startDerivative = derivativeFunction(start, startValue, stepSize, startDerivative)
        result.append(startValue)
    return np.asarray(result)

def heunsRecord(start, startValue, startDerivative, end, steps, record, derivativeFunction):
    result = [startValue]
    stepSize = (end - start)/steps
    for i in range(1, steps + 1):
        start += stepSize
        eulerStepped = startValue + stepSize * startDerivative
        startValue += stepSize * (1/2) * (startDerivative + derivativeFunction(start, eulerStepped, stepSize, startDerivative))
        startDerivative = derivativeFunction(start, startValue, stepSize, startDerivative)
        if (i - 1)/steps >= len(result)/(record - 1):
            result.append(startValue)
    result.append(startValue)
    return np.asarray(result)