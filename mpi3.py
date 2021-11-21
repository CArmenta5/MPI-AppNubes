from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
if r == 0:
    cont = 0
    for i in range(50):
        cont += i
    print "Nodo - %d -> %d" % (r, cont)
    comm.send(cont, dest=1)
    cont = comm.recv(source=1)
    print "Nodo - %d -> %d" % (r, cont)
else:
    cont = comm.recv(source=0)
    print "Nodo - %d -> %d" % (r, cont)
    for i in range(50,101):
        cont += i
    print "Nodo - %d -> %d" % (r, cont)
    comm.send(cont, dest=0)
