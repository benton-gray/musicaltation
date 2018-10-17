# Lets Generate Musical Notes and Scales
import numpy as np


KEY_RANGE=7
NUM_SCALES=3
MIN_RAND=0
MAX_RAND=100000-1
scale_list = []
temp_list = []

print("## START OF EXECUTION ##", end="\n\n")

## Create Scale Object
for key in range(NUM_SCALES):
    scale_list.append(np.arange(KEY_RANGE))
    print(f"Creating Scale Key - Index: {key}")

print("\n\n")
print(f"Scalelist: {scale_list}", end='')
print(f" --- of type: {type(scale_list)}")

## Fill Scale Object Data (random)
for i,scale in enumerate(scale_list):
    # print(scale.tostring()) # Prints to Hex Representation, in Bytes Type
    randint=np.random.randint(MIN_RAND,MAX_RAND) ## TODO: This operation is the entrypoing for whatever it is
    print(type(scale.tostring()))
    print(type(scale))
    print(randint)
    print(i)
    print(scale_list[i])
    temp_list.append([num+1 * randint for num in scale_list[i]])
    print(temp_list)

