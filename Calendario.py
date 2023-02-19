#  Calendario
#  v1.0 Basica de consola
#  Copyright 2023 marcelo kacerovsky <marcelokacerovsky@marcelos-MacBook-Air.local>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
from time import localtime, time
import argparse


def anioBisiesto(anio) :
    """ Retorna si un año es bisiesto o no """
    if anio > 1582 :
        if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0) :
            return True
        else :
            return False
    else :
        return None


def diaDelMes(anio) :
    """ Retorna los dias del mes del año """
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mesesb = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if anioBisiesto(anio) :
        return mesesb
    else :
        return meses


def semanaAnio(anio) :
    """ Permite saber en que dia empieza el año """
    semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    aux = 6
    for i in range(1583, anio) :
        if anioBisiesto(i) :
            aux += 2
        else :
            aux += 1
    if aux % 7 == 0 :
        return 6
    if aux <= 7 :
        return aux - 1
    else :
        return (aux % 7) - 1


def mostrarCalendario(anio) :
    """ Muestra el calendario de un año especifico """
    SEMANA = ["L", "M", "M", "J", "V", "S", "D"]
    MONTH = ["   ENERO  ", " FEBRERO  ", "   MARZO  ", "   ABRIL  ", "   MAYO   ", "  JUNIO   ", "  JULIO   ", "  AGOSTO  ", "SEPTIEMBRE", " OCTUBRE  ", "NOVIEMBRE ", "DICIEMBRE "]
    aux = semanaAnio(anio)
    if anioBisiesto(anio) :
        mes = diaDelMes(anio)
    else :
        mes = diaDelMes(anio)
    print("+" + "----------------------------" * 3 + "+")
    print("|" + "                            " + "           " + str(anio) + "             " + "                            " + "|")
    print("+" + "----------------------------" * 3 + "+")
    calendario = []
    for m in range(len(mes)) :
        meses = []
        meses.append("+--------------------------+")
        meses.append("|        " + MONTH[m] + "        |")
        meses.append("+--------------------------+")

        fila = ""
        for s in range(7) :
            fila += "  " + SEMANA[s] + " "

        meses.append(fila), meses.append("")

        fila = ""
        for a in range(aux) :
            fila += "    "
        for d in range(1, mes[m] + 1) :
            if (d + aux) % 7 == 0 :
                if d <= 9 :
                    meses.append(fila + "  " + str(d) + " ")
                else :
                    meses.append(fila + " " + str(d) + " ")
                fila = ""
            else :
                if d <= 9 :
                    fila += "  " + str(d) + " "
                else :
                    fila += " " + str(d) + " "

        if fila != "" :
            if len(fila) < 29 :
                fila += (" " * (28 - len(fila)))
        else :
            fila = "                            "
        meses.append(fila)

        n = 11 - len(meses)
        if n != 0 :
            for i in range(n) :
                meses.append("                            ")

        calendario.append(meses)
        aux = (aux + mes[m])
        if aux > 35 :
            aux %= 7
        else :
            if aux == 35 :
                aux = 0
            else :
                aux %= 7

    for i in range(0, 12, 3) :
        for j in range(11) :
            print(calendario[i][j], calendario[i + 1][j], calendario[i +2][j])



def mostrar_mes(aaaa, mm, dd) :
    """ Muestra el mes actual """
    mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    SEMANA = ["L", "M", "M", "J", "V", "S", "D"]
    MONTH = ["   ENERO  ", " FEBRERO  ", "   MARZO  ", "   ABRIL  ", "   MAYO   ", "  JUNIO   ", "  JULIO   ", "  AGOSTO  ", "SEPTIEMBRE", " OCTUBRE  ", "NOVIEMBRE ", "DICIEMBRE "]
    aux = semanaAnio(aaaa)
    if anioBisiesto(aaaa) :
        mes[1] = 29

    print("+--------------------------+")
    print("|           " + str(aaaa) + "           |")
    print("+--------------------------+")
    # calcula el dia en el cual empieza el mes
    for m in range(mm - 1) :
        aux = (aux + mes[m])
        if aux > 35 :
            aux %= 7
        else :
            if aux == 35 :
                aux = 0
            else :
                aux %= 7  
    print("+--------------------------+")
    print("|        " + MONTH[mm - 1] + "        |")
    print("+--------------------------+")
    for s in range(7) :
        print("  " + SEMANA[s] + " ", end="")
    print("\n")
    for a in range(aux) :
        print("    ", end="")
    for d in range(1, mes[mm - 1] + 1) :
        if (d + aux) % 7 == 0 :
            if d <= 9 :
                print("  " + str(d))
            else :
                print(" " + str(d))
        else :
            if d <= 9 :
                print("  " + str(d) + " ", end="")
            else :
                print(" " + str(d) + " ", end="")
    print("\n\nEl dia de hoy es: " + str(dd))




if __name__ == "__main__" :
    parser = argparse.ArgumentParser(prog="Calendario", description="Muestra el calendario del año pasado por argumento y el mes actual")
    parser.version = "1.0"
    parser.add_argument("-v", "--version", action="version", help="Muestra la version del programa")
    parser_group = parser.add_mutually_exclusive_group()
    parser_group.add_argument("-m", "--mes", help="Mostrar el mes actual", action="store_const", const=tuple(localtime(time()))[:3])
    parser_group.add_argument("-a", "--anio", help="Mostar el calendario del año especifico desde 1583", type=int)

    args = parser.parse_args()

    if args.anio != None :
        mostrarCalendario(args.anio)
    elif args.mes != None :
        mostrar_mes(args.mes[0], args.mes[1], args.mes[2])