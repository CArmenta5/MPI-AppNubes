from mpi4py import MPI
comm = MPI.COMM_WORLD
r = comm.Get_rank()
if r == 0:
        dic = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': 'Apps en la nube' }
        comm.send(dic, dest=1)
        s = comm.recv(source=1)
        print "Nodo %d nos ha mandado un diccionario: %s" % (r, s)
elif r == 1:
        dic = {'nombre' : 'Raul', 'edad' : 22, 'cursos': 'Vision para robots' }
        comm.send(dic, dest=0)
        s = comm.recv(source=0)
        print "Nodo %d nos ha mandado un diccionario: %s" % (r, s)
        