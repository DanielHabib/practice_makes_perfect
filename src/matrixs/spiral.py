"""
Print a clockwise Spiral of an array
"""


def spiral(M):
    top = 0
    bottom = len(M) - 1
    right = len(M[0]) - 1
    left = 0

    # while top != bottom and right != left:
    if True:
        # print top
        for value in M[left: right]:
            print(value[top])
        # print right
        for value in M[right][top: bottom]:
            print(value)
        # print bottom
        for value in M[left: right: -1]:
            print(value)
        # print left
        for value in M[left][top:bottom:-1]:
            print(value)

if __name__=='__main__':
    a = [
            [1,2,8],
            [3,4,9],
            [5,6,10]
        ]
    spiral(a)
