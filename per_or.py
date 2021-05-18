import xlrd
import openpyxl
import pandas as pd
def entrenar(theta, fac_ap, w1, w2, epochs, x1, x2, d, n_muestras):
    errores = True
    while errores:
        errores= False
        for i in range(n_muestras):
            z =( (x1[i] * w1) + (x2[i] * w2) ) - theta #aqui se calcula el valor de salida

            if z >= 0:
                z = 1
            else:
                z = 0

            if z != d[i]:
                error = True
                error = ( d[i] - z ) #aqui calculamos el error deseado
                theta = theta + (-(fac_ap * error))#aqui ajustamos theta o  umbral
                w1 = w1 + (x1[i] * error * fac_ap) #aqui ajustamos los pesos de la entrada numero 1
                w2 = w2 + (x2[i] * error * fac_ap) #aqui ajustamos los pesos de la entrada nuemro 2
                epochs +=1 # la epochs se aumentan en cuanto ingrese al error

    return w1, w2, epochs, theta


#ciclo principal
if __name__ == "__main__":
    archivo_excel = pd.read_excel("C:/Users/Diego/Desktop/perceptron_or/datos/datos_or.xlsx")#aqui leemos el archivo de donde vamos a sacar las comparaciones
    theta = 0.2 #este es nuestro umbral ya que esta definido como theta en la formula
    fac_ap= 0.2 #nuestro factor de aprendizaje siempre debe estar entre 0 y 1
    w1 = 0.5 #nuestra peso numero 1 con valor aleatorio
    w2 = 0.5 #nuestra peso numero 2 con valor aleatorio
    epochs = 0 #numero de veces que realiza un ajuste en los pesos
    x1 = archivo_excel["x1"]
    x2 = archivo_excel["x2"]
    d = archivo_excel["d"]
    n_muestras = len(d)
    w1, w2, epochs, theta = entrenar(theta, fac_ap, w1, w2, epochs, x1, x2, d, n_muestras)
    print("w1 = " + str(w1))
    print("w2 = " + str(w2))
    print("umbral(theta) = " + str(theta))
    print("epochs = " + str(epochs))
                
