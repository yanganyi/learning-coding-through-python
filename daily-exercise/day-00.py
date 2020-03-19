a = ' '
b = '*'

def _print_a_row(width, count):
    x = int((width - count) / 2)
    y = a * x
    z = b * count
    print(y+z+y)

def draw_an_arrow(n):
    width = (n-1) * 2 + 1

    # top
    for row in range(1,2*n+1,2):
        _print_a_row(width,row)

    # middle
    for i in range(n):
        _print_a_row(width,1)

    # bottom
    for row in range(2*n-1,0,-2):
        _print_a_row(width,row)

def draw_an_christmas_tree(n):
    width = (n-1) * 2 + 1

    # top
    for row in range(1,2*n+1,2):
        _print_a_row(width,row)

    # middle
    for i in range(n):
        _print_a_row(width,1)


draw_an_arrow(5)
draw_an_christmas_tree(5)



# ORIGINAL CODE by Ron
#
# a = ' '
# b = '*'
#
# def top(btm_row,n):
#     for row in range(1,2*n+1,2):
#         x = (btm_row - row) / 2
#         x = int(x)
#         y = x * a
#         z = b * row
#         print(y+z+y)
#
# def middle(btm_row,n):
#     for i in range(n):
#         y = int((btm_row - 1) / 2) * a
#         z = y + b + y
#         print(z)
#
# def bottom(btm_row,n):
#     for row in range(2*n-1,0,-2):
#         x = (btm_row - row) / 2
#         x = int(x)
#         y = x * a
#         z = b * row
#         print(y+z+y)
#
# def draw_an_arrow(n):
#     btm_row = (n-1) * 2 + 1
#     top(btm_row,n)
#     middle(btm_row,n)
#     bottom(btm_row,n)
#
# draw_an_arrow(5)