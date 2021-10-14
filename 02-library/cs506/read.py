def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """ 

    l=[]

    with open(csv_file_path, 'r') as f:
    lines = f.readlines()
    for line in lines:
        l.append([x for x in line.split(",") if x != '\n'])


    return l 
    

