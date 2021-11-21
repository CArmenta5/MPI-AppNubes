from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
if r == 0:
    print "Escribe el numero a calcular el factorial:"
    n = input()
    cont = 1
    for i in range(1,int(n/2)):
        cont *= i
    comm.send(cont, dest=1)
    comm.send(n, dest=1)
    cont = comm.recv(source=1)
    print "Nodo - %d, el factorial es: %d" % (r, cont)
else:
    cont = comm.recv(source=0)
    n = comm.recv(source=0)
    for i in range(int(n/2),n+1):
        cont *= i
    print "Nodo - %d, el factorial es: %d" % (r, cont)
    comm.send(cont, dest=0)