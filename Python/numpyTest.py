import numpy as np
from numpy.linalg import *

def main():
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    np_lst = np.array(lst, dtype=np.float)

    print(np_lst.shape)
    print(np_lst.ndim)
    print(np_lst.dtype)
    print(np_lst.itemsize)
    print(np_lst.size)

    # 2 Some Arrays
    print(np.zeros([2, 4]))
    print(np.ones([3, 5]))
    print('Rand:')
    print(np.random.rand(2, 4))
    print(np.random.rand())

    print('RandInt:')
    print(np.random.randint(1, 10, 3))
    print('Choise:')
    print(np.random.choice([10, 20, 30, 5, 25]))

    print('Distribute:')
    print(np.random.beta(1, 10, 100))

    # 3 Array Opes
    print('Array Opes:')
    print(np.arange(1, 11))
    print(np.arange(1, 11).reshape([2, 5]))
    print(np.arange(1, 11).reshape([2, -1]))

    print('Array mathematical fuc:')
    lst = np.arange(1, 11)
    print('exp:')
    print(np.exp(lst))  # 自然指数
    print('exp2:')
    print(np.exp2(lst))
    print('sqrt')
    print(np.sqrt(lst))
    print('sin')
    print(np.sin(lst))
    print('log')
    print(np.log(lst))

    lst = np.array([
        [[1, 2, 3, 4], [4, 5, 6, 7]],
        [[7, 8, 9, 10], [10, 11, 12, 13]],
        [[14, 15, 16, 17], [18, 19, 20, 21]]
    ])
    print(lst.sum())
    print(lst.sum(axis=0))
    print(lst.sum(axis=1))
    print(lst.sum(axis=2))

    print(lst.max())
    print(lst.max(axis=1))
    print(lst.min(axis=0))

    lst1 = np.array([10,20,30,40])
    lst2 = np.array([5,4,3,2])
    print('Add:')
    print(lst1 + lst2)
    print('Sub:')
    print(lst1 - lst2)
    print('Mul:')
    print(lst1 * lst2)
    print('Div:')
    print(lst1 / lst2)
    print('Square:')
    print(lst1 ** 2)
    print('Dot Product')
    print(np.dot(lst1.reshape(2,2),lst2.reshape(2,2)))

    print('Cancatenate')
    print(np.concatenate((lst1,lst2),axis=0))
    print('vstack')
    print(np.vstack((lst1,lst2)))
    print('hstack')
    print(np.hstack((lst1,lst2)))
    print('split')
    print(np.split(lst1,2))
    print(np.split(lst1,4))
    print(np.copy(lst1))

    #liner from numpy.linalg import *
    print('liner')
    print(np.eye(3))
    lst = np.array([
        [1,2],
        [3,4]
    ])
    print('Inverse')
    print(inv(lst))
    print('Transpose')
    print(lst.transpose())
    print('Det:')
    print(det(lst))
    print('eig')
    print(eig(lst))

    y=np.array([[5.],[7.]])
    print('Solve')
    print(solve(lst,y))

    #5 Others
    print('FFT:')
    print(np.fft.fft(np.array([1,1,1,1,1,1,1])))
    print('Coef:')
    print(np.corrcoef([1,0,1],[0,2,1]))
    print('Poly:')
    print(np.poly1d([2,1,3]))



if __name__ == '__main__':
    main()
