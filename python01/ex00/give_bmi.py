import numpy as np
import matplotlib.pyplot as plt

def give_bmi(height, weight) -> list:
    height_np = np.array(height)
    weight_np = np.array(weight)
    
    result = weight_np / (height_np ** 2)
    
    return (result.tolist())


def apply_limit(bmi, limit: int) -> list:
    return [True if result >= limit else False for result in bmi]


height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# x = np.linspace(0, 2*np.pi, 100)
# print("x == ", x)
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()

