import numpy as np
from scipy.linalg import solve
from barra import Barra
from constantes import g_, ρ_acero, E_acero
from secciones import SeccionICHA

class Reticulado(object):
    __NNodosInit__ = 100
    def __init__(self):
        super(Reticulado, self).__init__()
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.Ndimensiones = 3
        self.barras = []
        self.cargas = {}
        self.restricciones = {}

    def agregar_nodo(self, x, y, z=0):
        self.xyz.resize((self.Nnodos+1, 3))
        self.xyz[self.Nnodos,:] = [x,y,z]
        self.Nnodos += 1
        if z != 0:
            self.Ndimensiones = 3
            
    def agregar_barra(self, barra):
        self.barras.append(barra)

    def obtener_coordenada_nodal(self, n):
        posicion = n
        coordenadas = self.xyz[n]
        return(coordenadas)

    def calcular_peso_total(self):
        lista_barras = self.barras
        peso_total = 0
        for barra in lista_barras:
            peso_total += barra.calcular_peso(self)
        return(peso_total)

    def obtener_nodos(self):
        xy = self.xyz
        return(xy)

    def obtener_barras(self):
        lista_barras = self.barras
        return(lista_barras)

    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        if nodo not in self.restricciones:
            self.restricciones[nodo] = [[gdl, valor]]
        else:
            self.restricciones[nodo].append([gdl, valor])

    def agregar_fuerza(self, nodo, gdl, valor):
        if nodo not in self.cargas:
            self.cargas[nodo] = [[gdl, valor]]
        else:
            self.cargas[nodo].append([gdl, valor])

    def ensamblar_sistema(self, factor_peso_propio=0., factor_cargas=0.0):
        self.Ndof = self.Nnodos*self.Ndimensiones
        self.k = np.zeros((self.Ndof, self.Ndof), dtype=np.double)
        self.f = np.zeros((self.Ndof), dtype=np.double)
        self.u = np.zeros((self.Ndof), dtype=np.double)
        self.fpp = factor_peso_propio*2
        for i,b in enumerate(self.barras):
            ke, fe = b.obtener_rigidez(self), b.obtener_vector_de_cargas(self)
            n_i, n_j = b.obtener_conectividad()
            if self.Ndimensiones == 2:
                d = [2*n_i, 2*n_i+1, 2*n_j, 2*n_j+1]
            else:
                d = [3*n_i, 3*n_i+1, 3*n_i+2, 3*n_j, 3*n_j+1, 3*n_j+2]
            for i in range(2*self.Ndimensiones):
                p = d[i]
                for j in range(2*self.Ndimensiones):
                    q = d[j]
                    self.k[p,q] += ke[i,j]
                if factor_peso_propio != [0., 0., 0.]:
                    self.f[p] += fe[i]

    def resolver_sistema(self):
        doffree = np.arange(self.Ndof)
        dofconstrained = []
        for nodo in self.restricciones:
            for restriccion in self.restricciones[nodo]:
                dof, value = restriccion[0], restriccion[1]
                dofglobal = dof+nodo*self.Ndimensiones
                self.u[dofglobal] += value
                dofconstrained.append(dofglobal)
        dofconstrained = np.array(dofconstrained)
        doffree = np.setdiff1d(doffree, dofconstrained)
        for nodo in self.cargas:
            for carga in self.cargas[nodo]:
                dof, value = carga[0], carga[1]
                dofglobal = dof+nodo*self.Ndimensiones
                self.f[dofglobal] += value
        kff = self.k[np.ix_(doffree, doffree)]
        kfc = self.k[np.ix_(doffree, dofconstrained)]
        kcf = kfc.T
        kcc = self.k[np.ix_(dofconstrained, dofconstrained)]
        uf, uc = self.u[doffree], self.u[dofconstrained]
        ff, fc = self.f[doffree], self.f[dofconstrained]
        uf = solve(kff, ff-kfc@uc)
        self.u[doffree] = uf

    def obtener_desplazamiento_nodal(self, n):
        if self.Ndimensiones == 2:
            dof = [2*n, 2*n+1]
        else:
            dof = [3*n, 3*n+1, 3*n+2]
        return(self.u[dof])

    def obtener_fuerzas(self):
        fuerzas = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            fuerzas[i] = b.obtener_fuerza(self)
        return(fuerzas)
    
    def obtener_factores_de_utilizacion(self, f, ϕ=0.9):
        FU = np.zeros((len(self.barras)), dtype=np.double)
        for i,b in enumerate(self.barras):
            FU[i] = b.obtener_factor_utilizacion(f[i], ϕ)
        return(FU)

    #ARREGLAR
    def rediseñar(self, Fu, ϕ=0.9):
        for i,b in enumerate(self.barras):
            print(f'Rediseñar barra {i} y cambiarlo por {b.rediseñar(Fu[i], self, ϕ)}')

    def chequear_diseño(self, Fu, ϕ=0.9):
        cumple = True
        for i,b in enumerate(self.barras):
            if not b.chequear_diseño(Fu[i], self, ϕ):
                print(f"----> Barra {i} no cumple algun criterio. ")
                cumple = False
        return(cumple)

    def guardar(self, nombre):
        import h5py
        dataset = h5py.File(nombre, "w")
        
        #Nodos
        dataset["xyz"] = self.xyz

        barras = np.zeros((len(self.barras), 2), dtype = np.int32)
        secciones = dataset.create_dataset('secciones', shape=((len(self.barras)),1), dtype=h5py.string_dtype())
    
        #Barras y Secciones
        for i, b in enumerate(self.barras):
            barras[i, 0] = b.ni
            barras[i, 1] = b.nj
            secciones[i,0] = b.seccion.nombre()
        dataset["barras"] = barras
    
        #Restricciones
        Restricciones = sorted(self.restricciones.items())
        largo = 0
        for nodo in self.restricciones:
            for i in self.restricciones[nodo]:
                largo += 1
        restricciones = dataset.create_dataset("restricciones", shape=(largo,2), dtype= np.int32)
        restricciones_val = dataset.create_dataset("restricciones_val", shape=(largo,1), dtype= np.double)
       
        lista = []
        for nodo in Restricciones:
            gdl = []
            restr = []
            for i in nodo[1]:          
                gdl.append(int(i[0]))
                restr.append(int(i[1]))
            lista.append([nodo[0], gdl, restr])
        
        j = 0
        for nodo in lista:
            if len(nodo[1]) == 2:
                    restricciones[j, 0] = nodo[0]
                    restricciones[j, 1] = nodo[1][0]
                    restricciones[j+1, 0] = nodo[0]
                    restricciones[j+1, 1] = nodo[1][1]
                    restricciones_val[j, 0] = nodo[2][0]
                    restricciones_val[j+1, 0] = nodo[2][1]
                    j += 2
            else:
                    restricciones[j, 0] = nodo[0]
                    restricciones[j, 1] = nodo[1][0]
                    restricciones[j+1, 0] = nodo[0]
                    restricciones[j+1, 1] = nodo[1][1]
                    restricciones[j+2, 0] = nodo[0]
                    restricciones[j+2, 1] = nodo[1][2]
                    restricciones_val[j, 0] = nodo[2][0]
                    restricciones_val[j+1, 0] = nodo[2][1]
                    restricciones_val[j+2, 0] = nodo[2][2]
                    j += 3
        
        #Cargas
        Cargas = sorted(self.cargas.items())
        largo = 0
        for nodo in self.cargas:
            for i in self.cargas[nodo]:
                largo += 1
        cargas = dataset.create_dataset('cargas', shape=(largo,2), dtype= np.int32)
        cargas_val = dataset.create_dataset('cargas_val', shape=(largo,1), dtype = np.double)
        
        lista = []
        for nodo in Cargas:
            gdl = []
            carga_puntual = []
            for i in nodo[1]:          
                gdl.append(int(i[0]))
                carga_puntual.append(int(i[1]))
            lista.append([nodo[0], gdl, carga_puntual])
                
        for k,nodo in enumerate(lista):
            cargas[k, 0] = nodo[0]
            cargas[k, 1] = nodo[1][0]
            cargas_val[k, 0] = nodo[2][0]
        dataset.close()
        
    def abrir(self, archivo):
        import h5py
        fid = h5py.File(archivo, "r")
        barras = fid["barras"]
        cargas = fid["cargas"]
        cargas_val = fid["cargas_val"]
        restricciones = fid["restricciones"]
        restricciones_val = fid["restricciones_val"]
        secciones = fid["secciones"]
        xyz = fid["xyz"]
        
        #Barras y Secciones
        for i,b in enumerate(barras):
            self.agregar_barra(Barra(np.int32(b[0]),np.int32(b[1]),SeccionICHA(secciones[i][0]),color=np.random.rand(3)))

        #Cargas
        for i, c in enumerate(cargas):           
            self.agregar_fuerza(np.int32(c[0]),np.float32(c[1]),np.float32(cargas_val[i]))
        
        #Restricciones
        for i, r in enumerate(restricciones):           
            self.agregar_restriccion(np.int32(r[0]),np.int32(r[1]),np.int32(restricciones_val[i]))
            
        #Nodos
        for i in xyz:
            self.agregar_nodo(i[0],i[1],i[2])
        fid.close()

    def __str__(self):
        s = 'nodos:\n'
        for i in range(len(self.xyz)):
            s += f'{i} : ({self.obtener_coordenada_nodal(i)})\n'
        s += '\nbarras:\n'
        for i in range(len(self.barras)):
            s += f'{i} : {self.barras[i].ni,self.barras[i].nj}\n'
        s += '\nrestricciones:\n'
        for i in self.restricciones:
            s += f'{i} : {self.restricciones[i]}\n'
        s += '\ncargas:\n'
        for i in self.cargas:
            s += f'{i} : {self.cargas[i]}\n'
        s += '\ndesplazamientos:\n'
        t = self.u.reshape((-1,self.Ndimensiones))
        for i in range(self.Nnodos):
            if self.Ndimensiones == 2:
                s += f'{i} : ({t[i,0]}, {t[i,1]})\n'
            else:
                s += f'{i} : ({t[i,0]}, {t[i,1]}, {t[i,2]})\n'
        s += '\nfuerzas:\n'
        for i in range(len(Reticulado.obtener_fuerzas(self))):
            s += f'{i} : {Reticulado.obtener_fuerzas(self)[i]}\n'
        s += f'\nNdimensiones = {self.Ndimensiones}'
        return(s)