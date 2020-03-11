#!/usr/bin/env python3

#Assignment: Floyd Warshall Algorithm
#Name: Jessica Redekop
#Professor: David Pruitt
#Due Date: Tue. Mar. 10, 2020
#Last Modified: Tue. Mar. 10, 2020

from mpi4py import MPI
import time

def readArray():
    
    #reads text matrix from file and converts to list
    mat = []
    with open('fwTest.txt', 'r') as f:
        for line in f:
            mat.append([int(i) for i in line.split()])
    return mat

def printMatrix(mat):
    print(mat[99])
    
def calculateShortestPath(mat):
    
    #MPI Code is from the provided mpiPythonExamples:
    
    # get the world communicator
    comm = MPI.COMM_WORLD
    #print(comm)

    # get our rank (process #)
    rank = comm.Get_rank()
    #print(rank)
    
    # get the size of the communicator in # processes
    size = comm.Get_size()
    #print(size)
    
    #rowsPerThread = rows/thread
    rpt = len(mat) / size
    tpr = size / len(mat)
    
    #start = rowspert * t#
    startRow = int(rpt * rank)
    #end = rowspert * (t#+1)
    endRow = int(rpt * (rank + 1))
    print(f'start row{startRow} end row {endRow}')
    
    for k in range(len(mat)):
        owner = tpr*k
        #print(owner)
        # broadcast message from root to everyone
        mat[k] = comm.bcast(mat[k],root=owner)
        for x in range(startRow,endRow):
            for y in range(len(mat)):
                mat[x][y] = min(mat[x][y], mat[x][k] + mat[k][y])
        #print(mat[0][99])
    
    # thread 0 sends the message
    if rank == 0:
        #print('not here')
        for k in range(endRow, len(mat)):
            owner = int(tpr*k)
            #print(k)
            #print(owner)
            #print(tpr)
            mat[k] = comm.recv(source=owner, tag=k)
    else:
        for k in range(startRow, endRow):
            #owner = int((comm.Get_size()/size)*k)
            comm.send(mat[k], dest= 0, tag=k)
            
    
    #comm.Disconnect()
    #comm.Free()
    
    return mat        
            
     
# read file into 2d list
mat = readArray()
#printMatrix(mat)

print('Input Matrix[99]:')
printMatrix(mat)

#starttime
start = time.time()

#implement Floyd Warshall algorithm
mat = calculateShortestPath(mat)
#print(mat[0][99])

#endtime
stop_time = time.time() - start

#prints list to check
print('Ouput Matrix[99]:')
printMatrix(mat)

print("time: ")
print("%s seconds" % stop_time)
print("\n")