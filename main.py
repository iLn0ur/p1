from py200_1_1 import Glass, GlassDefaultArg, GlassDefaultListArg


def main():
    glass1 = Glass(500, 100)
    glass2 = Glass(400, 50)

    print(glass1)

    glass1.capacity_volume = 200

    print(glass1)

def main2():
    gda = GlassDefaultArg()
    gda2 = GlassDefaultArg(200)

    print(gda, gda2)


def main3():
    gdla = GlassDefaultListArg(500)

    gdla1 = GlassDefaultListArg(500,[200])

    print(gdla, gdla1)

    gdla.occupied_volume.append(115)

    print(gdla, gdla1)


if __name__ == '__main__':
    main3()
