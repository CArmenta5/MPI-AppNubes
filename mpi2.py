from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
if r == 0:
    data ="Hola"
else:
    data = None
data = comm.bcast(data, root=0)  
    
if r == 0:
    print "Soy el nodo root - %d y les digo a por bcast -> %s" % (r, data)
else:
    print "Nodo - %d y recibi por bcast -> %s" % (r, data)