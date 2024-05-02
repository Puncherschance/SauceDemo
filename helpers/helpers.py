def convert_to_float(data):
    for i in range(len(data)):
        data[i] = float(data[i][1:])
    return data