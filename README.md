# Parallel-Computing-Floyd-Warshall
This assignment implements a parallel program with MPI that calculates all pairs shortest paths 
algorithm using the Floyd Warshall algorithm. The program will traverse 
an adjacency matrix and determine the shortest path between each pair of nodes.

The code uses the pseudocode from the examples provided in mpiPythonExamples.

It will display the last index of the input and output arrays, and fulfills the other requirements for the lab.
I had the same result in the last lab. 
## Instructions
Run: mpirun --oversubscribe -N <#threads> python floydwarshall.py
where <#threads> is the number of threads used.

## Issues encountered:
Encountered an issue where the array was initialized as type string, so the calculations were concatenating onto each other. This lead to an incorrect result with large numbers.

## How I overcame some problems:
Office hours

## Bugs in program:
Mpi will run through all parts of the code multiple times.

## How long it took me to complete this assignment:
4 hours

## Performance Measurements:
Serial: 0.22s


## Increasing # of Threads:
2 threads: 0.14s

4 threads: 0.19s

8 threads: 0.26s

## Observations:
I had the same result in the last lab. Running python floydwarshall.py without using mpi returns an average calculation time of 0.22s. By using mpi and running it with 2 threads, the time decreased by an average of 36%. Once we use 4 threads the time consumed by the program increased, and using 8 threads took much longer than the serial version. The same thing has happened in previous labs, I believe this is because the time for the system to allocate the threads and parse the matrix substantially increases the time after 4 threads.

## Output of cpuInfoDump.sh:
Intel(R) Core(TM) i7-7560U CPU @ 2.40GHz 4 -- 36 -- 216