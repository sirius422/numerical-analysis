import numpy as np


class Gauss():
    def __init__(self, a, b):
        self.comatrix = a
        self.augmatrix = np.hstack((a, b))
        self.width = self.augmatrix.shape[1]
        self.length = self.augmatrix.shape[0]

    def swap(self, r1, r2):
        for x in range(0, self.width):
            self.augmatrix[r1][x], self.augmatrix[r2][x] = self.augmatrix[r2][x], self.augmatrix[r1][x]

    def rowadd(self, m, row1, row2):
        for i in range(0, self.width):
            row2[i] -= row1[i] * m

    def check(self):
        rank1 = np.linalg.matrix_rank(self.comatrix)
        rank2 = np.linalg.matrix_rank(self.augmatrix)
        print("The rank of coefficient matrix is {}\nThe rank of augmented matrix is {}".format(rank1, rank2))
        if rank1 != rank2:
            print("No solution")
            return
        if rank1 == rank2 < self.length:
            print("Infinite solutions")
            return
        if rank1 == rank2 == self.length:
            print("Only 1 solution")
            self.arrange()

    def arrange(self):
        k = 0
        while k < self.width:
            absmatrix = np.fabs(self.augmatrix)  # find the row contain the largest elements and
            for i in range(k, self.length):
                for j in range(k + i, self.length):
                    if absmatrix[i][k] < absmatrix[j][k]:
                        self.swap(i, j)
            column = self.augmatrix[k:, k]  # calculate the m coefficient then transform the matrix
            for index, row in enumerate(column[1:]):
                m = row / column[0]
                self.rowadd(m, self.augmatrix[k, :], self.augmatrix[index + k + 1, :])
            k += 1  # move to the next row
        self.cal()

    def cal(self):
        result = np.array([None] * self.length)
        for i in range(self.length - 1, -1, -1):
            temp = 0
            for n in list(range(self.length - 1, i, -1)):
                temp = temp + result[n] * self.augmatrix[i][n]
            result[i] = (self.augmatrix[i][self.width - 1] - temp) / self.augmatrix[i][i]
        print(result.reshape(self.length, 1))

    def calculate(self):
        self.check()


if __name__ == '__main__':
    matrixA = np.array(
        ([3, -1, 4],
         [-1, 2, -2],
         [2, -3, -2]
         ))
    matrixB = np.array([7, -1, 0]).reshape(3, 1)
    gauss = Gauss(matrixA, matrixB)
    gauss.calculate()
