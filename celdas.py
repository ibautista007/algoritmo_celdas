class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        #Creacion de la secuencia de repeticion
        while N>0:

            #Se crea arreglo donde se almacenara respues y se agrega el primer valor para la primera celda en la fila
            resu=[]
            resu.append(0)
             
            #usamos el forma para movernos dentro del arreglo
            for i in range (1,7):
                #se evalua las referencia de las celdas y se guarda en variable temporal
                temp =1 if cells[i-1] == cells[i+1] else 0
                #se guarda los resultados en el nuevo arreglo de respuesta
                resu.append(temp)
                #Avanzar al siguiente punto del arreglo
                i += 1
            #agregar el ultimo valor de la fila    
            resu.append(0)
            #guardar todo la informacion en la variable de resultado que mostraremos...usaremos de nuevo cells, pero este paso se puede omitir
            cells = resu
            #Se hace reduce los valores para evitar repetir los ciclos y mejorar el codigo
            N=(N-1)%14
                        
        return cells;
                       
        
        
