import numpy as np
import pandas

def summary(array):
    print("min: "+str(min(array))+"\nmax: "+str(max(array))+"\nmean: "+str(sum(array)/len(array)))

if __name__ == '__main__':
    airplanes = []



    file = "pfile-51-0-1--I0-G0-n0.pddl"
    f = open(file, "r")
    lines = [line for line in f.readlines()]
    apn = lines[5].strip().split("(:objects ")[1].split(" ")
    cit = lines[6].strip().split(" ")
    tru = lines[7].strip().split(" ")
    loc = lines[8].strip().split(" ")
    obj = lines[9].strip().split(" ")

    airplanes.append(len(apn))
    airplanes.append(10)
    summary(airplanes)





