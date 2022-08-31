from numpy import pi, sqrt, nan
from numpy.random import rand
from constantes import g_, ρ_acero, mm_
import pandas as pd
 
class Circular(object):
    def __init__(self, D, Dint, color=rand(3)):
        super(Circular, self).__init__()
        self.D = D
        self.Dint = Dint
        self.color = color

    def area(self):
        return pi*(self.D**2 - self.Dint**2)/4

    def peso(self):
        return self.area()*ρ_acero*g_

    def inercia_xx(self):
        return pi*(self.D**4 - self.Dint**4)/4

    def inercia_yy(self):
        return self.inercia_xx()

    def nombre(self):
        return f"O{self.D*1e3:.0f}x{self.Dint*1e3:.0f}"

    def __str__(self):
        return f"Seccion Circular {self.nombre()}"

class SeccionICHA(object):
    def __init__(self, denominacion, base_datos='Perfiles ICHA.xlsx', debug=False, color=rand(3)):
        super(SeccionICHA, self).__init__()
        self.denominacion = denominacion
        self.color = color
        var = self.denominacion.split('x')
        perfil, d, HEAD = '', '', 11
        for i in range(len(var[0])):
            if var[0][i].isdigit() == False:
                perfil += var[0][i]
            else:
                d += (var[0][i:])
                break
        
        if var[0].count('.') > 0:
            d = float(d)
        else:
            d = int(d)
        
        if var[1].count('.') > 0:
            bf = float(var[1])
        else:
            bf = int(var[1])
            
        if perfil == 'W':
            planilla = ['HR']
        elif perfil =='[]':
            planilla = ['Cajon']
        elif perfil == 'O':
            planilla = ['Circulares Mayores']
            HEAD = 10
        elif perfil == 'o':
            planilla = ['Circulares Menores']
            HEAD = 10
        else:
            planilla = [f'{perfil}']
            
        self.data = pd.concat(pd.read_excel(base_datos, header=HEAD, sheet_name=planilla), ignore_index=True)
        datos, match, index = self.data.values.tolist(), False, False
        
        for i in range(len(datos)):
            if planilla[0] in ['H','PH','Cajon']:
                if var[2].count('.') > 0:
                    p = float(var[2])
                else:
                    p = int(var[2])
                if datos[i][0:6] == [perfil, d, '×', bf, '×', p]:
                    match, index = True, i
            elif planilla[0] == 'HR':
                if perfil == 'HR':
                    if var[2].count('.') > 0:
                        p = float(var[2])
                    else:
                        p = int(var[2])
                    if datos[i][4:10] == [perfil, d, '×', bf, '×', p]:
                        match, index = True, i
                else:
                    if datos[i][0:4] == [perfil, d, '×', bf]:
                        match, index = True, i
            elif planilla[0] == 'Circulares Mayores':
                if datos[i][0:2] == [d,bf]:
                    match, index = True, i
            else:
                if datos[i][1:3] == [d,bf]:
                    match, index = True, i
        self.perfil = perfil
        self.match = match
        self.index = index

    def area(self):
        df = (pd.DataFrame(self.data, columns=['A'])).values.tolist()
        return(df[self.index][0]*(mm_)**2)

    def peso(self):
        df = (pd.DataFrame(self.data, columns=['peso'])).values.tolist()
        return(df[self.index][0])

    def inercia_xx(self):
        if self.perfil =='O' or self.perfil == 'o':
            df = pd.DataFrame(self.data, columns=['I/10⁶']).values.tolist()
        else:
            df = pd.DataFrame(self.data, columns=['Ix/10⁶']).values.tolist()
        return(df[self.index][0])

    def inercia_yy(self):
        if self.perfil == 'O' or self.perfil == 'o':
            df = pd.DataFrame(self.data, columns=['I/10⁶']).values.tolist()
        else:
            df = pd.DataFrame(self.data, columns=['Iy/10⁶']).values.tolist()
        return(df[self.index][0])

    def nombre(self):
        return self.denominacion

    def __str__(self):
        if self.match == True:
            s = f'{self.denominacion} encontrada. A={self.area()} Ix={self.inercia_xx()} Iy={self.inercia_yy()}'
        else:
            s = f'Tipo de seccion {self.denominacion} no encontrada en base de datos.'
        s += f'\nSeccion ICHA  {self.denominacion}\n\tArea : {self.area()}\n\tpeso : {self.peso()}\n\tIxx : {self.inercia_xx()}\n\tIyy : {self.inercia_yy()}'
        return(s)
