import numpy as np

def check_inner_product(A, x, y, z, lambda_=2):
    '''
    A, x, y, z: none zero vectors
    '''
    if not A.any() and not x.any() and not y.any() and z.any():
        print('Please provide non-zero vectors.')
        return
    is_symmetric = False
    is_positive_definite = False
    is_bilinear = False

    # beta(x, y) = x.T @ A @ y
    beta = lambda x, y: x.T @ A @ y

    # test symmetric, <x, y> == <y, x>
    if beta(x, y) == beta(y, x):
        is_symmetric = True


    # test positive definite, <x, x> > 0, if and only if <0, 0> = 0
    if beta(np.zeros_like(x), np.zeros_like(x)) == 0 and beta(x, x).any == False:  # x is non-zero, so is beta(x, x)
        for _ in range(1000):
            x_test = np.random.randint(-1000, 1000, x.shape)
            if _ % 50 == 0: print('.', end='')
            if beta(x_test, x_test) > 0:  # cannot be 0 if x is not a zero vector
                is_positive_definite = True
            else:
                is_positive_definite = False
                break


    # test bilinear:  <λx + y, z> =  λ<x, z> + <y, z> and <x, λy + z> =  λ<x, y> + <x, z> 
    if beta(lambda_ * x + y, z) == (lambda_ * beta(x, z) + beta(y, z)) and \
        beta(x, lambda_ * y + z) == lambda_ * beta(x,y) + beta(x, z):
        is_bilinear = True

    print()
    if is_symmetric:
        print("Symmetric")
    else:
        print('Not symmetric')
    if is_positive_definite:
        print('Positive definite')
    else:
        print('Not positive definite')
    if is_bilinear:
        print('Bilinear')
    else:
        print('Not bilinear')
    if is_symmetric and is_positive_definite and is_bilinear:
        print('An inner product')
    else:
        print('Not an inner product')
        
        
        
# quiz example
A = np.array([[2, -2], [-1, 4]])
x = np.array([1, 2])
y = np.array([-1, 3])
z = np.array([3, 2])
lambda_ = -2
check_inner_product(A, x, y, z, lambda_)
