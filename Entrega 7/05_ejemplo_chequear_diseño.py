from reticulado import Reticulado
from barra import Barra
from graficar3d import ver_reticulado_3d
from constantes import *
from math import sqrt
from secciones import SeccionICHA

NNodoss = 20
NNodos  = NNodoss*3-1

xo = 5.075777986710320100e+00*m_
yo = 4.281724747887941618e+01*m_

L_total = 117.48*m_
H_total = 19.18*m_
H_total = 0.*m_
H_max = 3.5*m_

B = 4.*m_

L = L_total/(NNodoss-1)

q = 400*kgf_/m_**2

F = B*L_total*q/2

#Inicializar modelo
ret = Reticulado()

#Nodos
Nodos = {}
for i in range(NNodos):
    if i%3 == 0:
        Nodos[i] = [xo+int(i/3)*L,0,yo]
    elif i%3 == 1:
        Nodos[i] = [xo+int(i/3)*L,B,yo]
    else:
        if int(i/3)*L+L/2 <= L_total/2:
            Nodos[i] = [xo+int(i/3)*L+L/2, B/2, yo+(int(i/3)*L+L/2)*H_max/(L_total/2)]
        else:
            Nodos[i] = [xo+int(i/3)*L+L/2, B/2, yo+(int(i/3)*L+L/2)*-H_max/(L_total/2)+2*H_max]

for i in range(len(Nodos)):
    ret.agregar_nodo(Nodos[i][0],Nodos[i][1],Nodos[i][2])
    
#Crear y agregar las barras
conecciones = []
for i in range(len(Nodos)):
    if i == NNodos-1:
        break
    if i%3 == 0:
        conecciones.append([i,i+1])
        if i < NNodos - 2:
            conecciones.append([i,i+2])
            conecciones.append([i,i+3])
            conecciones.append([i,i+4])
    elif i%3 == 1:
        conecciones.append([i,i+1])
        conecciones.append([i,i+2])
        conecciones.append([i,i+3])
    elif i%3 == 2:
        conecciones.append([i,i+1])
        conecciones.append([i,i+2])
        if i < NNodos - 3:
            conecciones.append([i,i+3])
            
seccion = SeccionICHA("o12.7x10.9", color="#A3500B")
seccion_chica = SeccionICHA("o88.9x82.9", color="#A3500B")
seccion1 = SeccionICHA("H600x300x157.5", color="#A3500B")
seccion2 = SeccionICHA("[]300x75x22.6", color="#A3500B")
seccion3 = SeccionICHA("o114.3x106.3", color="#A3500B")
seccion4 = SeccionICHA("H1000x350x264", color="#A3500B")
seccion5 = SeccionICHA("o114.3x104.3", color="#A3500B")
seccion6 = SeccionICHA("O160x150", color="#A3500B")
seccion7 = SeccionICHA("[]150x75x10.1", color="#A3500B")
seccion8 = SeccionICHA("H350x350x249.5", color="#A3500B")
seccion9 = SeccionICHA("o76.2x66.2", color="#A3500B") 
seccion10 = SeccionICHA("o114.3x104.3", color="#A3500B")
seccion11 = SeccionICHA("H450x450x234.9", color="#A3500B")
seccion12 = SeccionICHA("[]60x40x6.4", color="#A3500B") 
seccion13 = SeccionICHA("HR970x300x219.9", color="#A3500B")
seccion14 = SeccionICHA("H900x400x205.4", color="#A3500B")
seccion15 = SeccionICHA("H900x350x190.9", color="#A3500B")
seccion16 = SeccionICHA("H600x300x176", color="#A3500B")
seccion17 = SeccionICHA("[]300x75x17.1", color="#A3500B")
seccion18 = SeccionICHA("o114.3x109.3", color="#A3500B") 
seccion19 = SeccionICHA("H900x300x161.7", color="#A3500B")
seccion20 = SeccionICHA("[]200x70x23.3", color="#A3500B")
seccion21 = SeccionICHA("o101.6x93.6", color="#A3500B")
seccion22 = SeccionICHA("H400x250x146.7", color="#A3500B")
seccion23 = SeccionICHA("[]150x50x11.6", color="#A3500B")
seccion24 = SeccionICHA("[]200x200x29.9", color="#A3500B")
seccion25 = SeccionICHA("[]200x75x12.4", color="#A3500B")

for i in range(len(conecciones)):
    if i == 0 or i == 189:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion))
    elif i == 1 or i == 4 or i == 187 or i == 188:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion1))
    elif i == 2 or i == 6 or i == 182 or i == 186:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion2))
    elif i == 3 or i == 5 or i == 183 or i == 185:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion3))
    elif i == 9 or i == 179:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion4))
    elif i == 10 or i == 180:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion5))
    elif i == 12 or i == 16 or i == 172 or i == 176:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion6))
    elif i == 13 or i == 15 or i == 62 or i == 66 or i == 122 or i == 126 or i == 173 or i == 175:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion7)) 
    elif i == 19 or i == 169:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion8))
    elif i == 20 or i == 80 or i == 110 or i == 170:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion9))
    elif i == 22 or i == 26 or i == 162 or i == 166:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion10))
    elif i == 29 or i == 159:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion11))
    elif i == 32 or i == 36 or i == 152 or i == 156:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion12))
    elif i == 39 or i == 149:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion13))
    elif i == 49 or i == 139:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion14))
    elif i == 59 or i == 129:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion15))
    elif i == 69 or i == 119:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion16))
    elif i == 72 or i == 76 or i == 112 or i == 116:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion17))
    elif i == 73 or i == 75 or i == 113 or i == 115:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion18))
    elif i == 79 or i == 109:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion19))
    elif i == 82 or i == 86 or i == 102 or i == 106:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion20))
    elif i == 83 or i == 85 or i == 103 or i == 105:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion21))
    elif i == 89 or i == 99:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion22))
    elif i == 90 or i == 100:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion23))
    elif i == 92 or i == 96:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion24))
    elif i == 93 or i == 95:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion25))
    else:
        ret.agregar_barra(Barra(conecciones[i][0],conecciones[i][1], seccion_chica)) 

#Crear restricciones (para nodos iniciales y finales)
for nodo in [0,1]:
	ret.agregar_restriccion(nodo, 0, 0)
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)

for nodo in [NNodos-2,NNodos-1]:
	ret.agregar_restriccion(nodo, 0, 0)
	ret.agregar_restriccion(nodo, 1, 0)
	ret.agregar_restriccion(nodo, 2, 0)
    
#Visualizar y comprobar las secciones
opciones_barras = {
    "ver_numeros_de_barras" : False,
	# "ver_secciones_en_barras": True,
	"color_barras_por_seccion": True,
}
ver_reticulado_3d(ret,opciones_barras=opciones_barras)

#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,-1.], factor_cargas=0.0)
ret.resolver_sistema()
f_D = ret.obtener_fuerzas()

#Agregar fuerzas tablero
for i in range(len(Nodos)):
    if Nodos[i][2] == yo:
        if i == 0 or i == 1 or i == NNodos -1 or i == NNodos -2:
            ret.agregar_fuerza(i, 2, -F/4)
        else:
            ret.agregar_fuerza(i, 2, -F/(2*(NNodoss-2)))
        
#Resolver el problema peso_propio
ret.ensamblar_sistema(factor_peso_propio=[0.,0.,0], factor_cargas=1.0)
ret.resolver_sistema()
f_L = ret.obtener_fuerzas()

#Visualizar f_L en el reticulado
opciones_nodos = {
    "ver_numeros_de_nodos": False,
	"usar_posicion_deformada": False,
}

opciones_barras = {
    "ver_numeros_de_barras" : False,
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":f_L
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Carga Viva")

#Visualizar f_L en el reticulado
opciones_nodos = {
    "ver_numeros_de_nodos": False,
	"usar_posicion_deformada": False,
}

opciones_barras = {
    "ver_numeros_de_barras" : False,
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":f_D
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Carga Muerta")

#Calcular carga ultima (con factores de mayoracion)
fu = 1.2*f_D + 1.6*f_L

#Visualizar combinacion en el reticulado
opciones_nodos = {
    "ver_numeros_de_nodos": False,
	"usar_posicion_deformada": False,
}

opciones_barras = {
    "ver_numeros_de_barras" : False,
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":fu
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="1.2D + 1.6L")

cumple = ret.chequear_diseño(fu, ϕ=0.9)

if cumple:
	print(":)  El reticulado cumple todos los requisitos")
else:
	print(":(  El reticulado NO cumple todos los requisitos")

#Calcular factor de utilizacion para las barras
factores_de_utilizacion = ret.obtener_factores_de_utilizacion(fu, ϕ=0.9)

#Visualizar FU en el reticulado
opciones_nodos = {
    "ver_numeros_de_nodos": False,
	"usar_posicion_deformada": False,
	 #"factor_amplificacion_deformada": 1,
}

opciones_barras = {
    "ver_numeros_de_barras" : False,
	"color_barras_por_dato": True,
	"ver_dato_en_barras" : True,
	"dato":factores_de_utilizacion
}

ver_reticulado_3d(ret, 
	opciones_nodos=opciones_nodos, 
	opciones_barras=opciones_barras,
	titulo="Factor Utilizacion")

ret.guardar("05_ejemplo_chequear_diseño.h5")