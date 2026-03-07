import math
def calculate_distance(point1, point2):
    dist =  math.sqrt ((point2[0]-point1[0])^2 + (point2[1] - point1[1])^2 + (point1[2] - point2[2])^2)
    return dist

def main():
    try:
        print("Enter coordinates x, y and z for Point 1:")
        x1 = int(input("x:"))
        y1 = int(input("y:"))
        z1 = int(input("z:"))
        point1 = (x1, y1, z1)

        print("Enter coordinates x, y and z for Point 2:")
        x2 = int(input("x:"))
        y2 = int(input("y:"))
        z2 = int(input("z:"))
        point2 = (x2, y2, z2)

        dist_result = calculate_distance(point1, point2)

        # Display the distance
        print("The distance between point1 and point2 is:", dist_result)



    except ValueError:
        print("try a better number")

if __name__ == "__main__":
    main()
