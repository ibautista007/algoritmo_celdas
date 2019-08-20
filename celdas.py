class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        #tomar los valores para resolver el problema
        dias= N
        
        f=0
        while f < dias:
            #creamos un nuevo arreglo donde guardaremos la respuesta correcta
            
            resu=[]
            #no olvidar que estaremos poniendo en la primera y ultima posicion del
            #arreglo los valores 0
            resu.append(0)
            
            #iniciamos el proceso en la posicion 1 del arreglo, donde podremos movernos
            #a la derecha y a la izquierda.
            i = 1
            rango = 7
            
            #se evaluan las posiciones con un while
            while i < rango: 
                prev = cells[i-1]
                sigu = cells[i+1]
                #validamos los valores y el resultado se guarda en una varible temporal
                if prev == sigu:
                    temp=0
                else:
                    temp=1
                    
                #agregamos los resultados al nuevo arreglo
                resu.append(temp)
                i += 1
            
            #colocamos el valor de la ultima celda
            resu.append(0)
            cells = resu
            f+=1
                       
        
        return cells;
