from prettytable import PrettyTable

def matrix_print(matrix, top_side, left_side):
    mt = PrettyTable()
    mt.field_names = ["    ", top_side[0], top_side[1], top_side[2], top_side[3]]
    for i in range(4):
        mt.add_row([left_side[i], matrix[i][0], matrix[i][1], matrix[i][2], matrix[i][3]])
    print(mt)

def resolution_column(matrix):
    column = 0
    for i in range(3):
        if matrix[i][0] < 0:
            for j in range(1,3):
                if matrix[i][j] < 0:
                    column = j
                    return column
    for i in range(1,4):
        if matrix[3][i] > 0:
            column = i
            break
    return column    

def resolution_row(matrix):
    min = 6543
    row = -1
    column = resolution_column(matrix)
    for i in range(4):
        if matrix[i][column] != 0 and matrix[i][0]/matrix[i][column] < min and matrix[i][0]/matrix[i][column] > 0:
            row = i
            min = round(matrix[i][0]/matrix[i][column], 3)
    return row

def transformation_jordan(matrix, row, column):
    new_matrix = [[0 for _ in range(4)] for _ in range(4)]
    if row != -1:
        for i in range(4):
            for j in range(4):
                if i != row and j != column:
                    new_matrix[i][j] = round(matrix[i][j] - (matrix[i][column]*matrix[row][j]/matrix[row][column]), 2)
                new_matrix[i][column] = round((-1)*(matrix[i][column]/matrix[row][column]), 2)
                new_matrix[row][j] = round(matrix[row][j]/matrix[row][column], 2)
        new_matrix[row][column] = round(1/matrix[row][column], 2)
    return new_matrix

def check(matrix, verification_matrix, left_side):
    vec_tmp = []
    X1 = matrix[left_side.index('X1')][0]
    X2 = matrix[left_side.index('X2')][0]
    X3 = matrix[left_side.index('X3')][0]
    for i in range(4):
        vec_tmp.append(verification_matrix[i][0] - (verification_matrix[i][1] * X1 + verification_matrix[i][2] * X2 + verification_matrix[i][3] * X3))
        if i < 3:
            print('???????????????? ???????????????? : '+ str(i+1))
            print(str(verification_matrix[i][0]) +' - (' +str(verification_matrix[i][1])+' * ' + str(X1) + ' + '
                + str(verification_matrix[i][2])+' * ' + str(X2)+ ' + ' + str(verification_matrix[i][3])+' * '+ str(X3) + ') ' +
                '= ' +  str(abs(round(vec_tmp[i], 2))), end='')
            if round(vec_tmp[i], 2) >= 0:
                print(' >= 0')
            else:
                print('???????????????? ???? ????????????!')
        else:
            print('???????????????? ????????????????????:')
            print(str(verification_matrix[i][0]) +' - (' +str(verification_matrix[i][1])+' * ' + str(X1) + ' + '
                  + str(verification_matrix[i][2])+' * ' + str(X2)+ ' + ' + str(verification_matrix[i][3])+' * '+ str(X3) + ') ' +
                  '= ' + str(vec_tmp[i]), end='')
            if vec_tmp[i] == matrix[i][0]:
                print(' =', matrix[i][0],'???????????????????? ???????????????? ????????????\n???????????????? ??????????????\n??????????:\nX1 = '
                      +str(X1)+'; X2 = '+ str(X2) + '; X3 = ' + str(X3) + '; F = '+
                     str(abs(vec_tmp[3])))
            else:
                print("?????????????????? ???????????????? ???????????? ???? ??????????!")

def init_matrix_1(c, b, a):
    m = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if i == 3 and j > 0:
                m[i][j] = c[j - 1]
            if i > 2 and j == 0:
                m[i][j] = 0
            if i < 3 and j != 0:
                m[i][j] = a[i][j - 1]
            if i < 3 and j == 0:
                m[i][j] = b[i]
    return m

def main():
    top_side  = ['S','X1','X2','X3']
    left_side = ['X4','X5','X6',' F']
    c = [6, 8, 5]
    b = [3, 4, 5]
    a = [[4, 1, 1], [1, 3, 0], [0, 0.5, 3]]
    # ???? ????
    matrix = init_matrix_1(c, b, a)
    verification_matrix = matrix

    print('???????????????? ????????????????-??????????????:')
    matrix_print(matrix,top_side,left_side)
    while resolution_column(matrix) > 0:
        # ?????????? ?????????? ??????????????
        print('???????????????????? ????????????: ' + str(top_side[resolution_column(matrix)]), left_side[resolution_row(matrix)], sep=',')
        top_side[resolution_column(matrix)],left_side[resolution_row(matrix)] = left_side[resolution_row(matrix)],top_side[resolution_column(matrix)]
        matrix = transformation_jordan(matrix, resolution_row(matrix), resolution_column(matrix))
        matrix_print(matrix,top_side,left_side)

    check(matrix, verification_matrix, left_side)

if __name__ == '__main__':
    main()