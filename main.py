from py200_1_1 import Glass, GlassDefaultArg, GlassDefaultListArg


def main():
    glass1 = Glass(500, 100)
    glass2 = Glass(400, 50)

    print(glass1.capacity_volume, glass2.capacity_volume)

    glass1.capacity_volume = 200

    print(glass1.capacity_volume, glass2.capacity_volume)


if __name__ == '__main__':
    main()
