** start of main.py **

def adjacency_list_to_matrix(adj_list:dict):
    if not isinstance(adj_list,dict):
        raise ValueError('Enter Adj List in dict Type')
    n=len(adj_list)
    adj_matrix=[[0]*n for _ in range(n)]
    for i,neigbour in adj_list.items():
        for j in neigbour:
            adj_matrix[i][j]=1
    for row in adj_matrix:
        print(row)
    return adj_matrix
adj_list={
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2],
}
adjacency_list_to_matrix(adj_list)

    

** end of main.py **

