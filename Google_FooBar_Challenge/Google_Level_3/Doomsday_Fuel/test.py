import numpy as np



def steady_state_prop(p):
    dim = p.shape[0]
    q = (p-np.eye(dim))
    ones = np.ones(dim)
    q = np.c_[q,ones]
    QTQ = np.dot(q, q.T)
    bQT = np.ones(dim)
    return np.linalg.solve(QTQ,bQT)



#result is :
#array([0.38268793, 0.39863326, 0.21867882])

#Expected Result = (0.4,0.4,0.2)


if __name__ == "__main__":

    one_step_transition = np.array([[0.125     , 0.42857143, 0.75      ],
           [0.75      , 0.14285714, 0.25      ],
           [0.125     , 0.42857143, 0.        ]])

    steady_state_matrix = steady_state_prop(one_step_transition.transpose())

    print (steady_state_matrix)

    tobe = np.array(((0.4, 0.4, 0.2)))
    print(tobe)
    print(np.dot(one_step_transition.T, tobe))
    print()

    result = steady_state_prop(one_step_transition.T)
    print(result)
    print(np.dot(result, one_step_transition.T))
    print()
