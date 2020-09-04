from py200_1_1 import Glass, GlassDefaultArg, GlassDefaultListArg, GlassAddRemove


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


def main4():
    gar = GlassAddRemove(500,0)

    gar.add_water(200)

    print(gar)

    print('over', gar.remove_water(300))

    print('over', gar.add_water(200))
    print('over', gar.add_water(600))


if __name__ == '__main__':
    main4()
