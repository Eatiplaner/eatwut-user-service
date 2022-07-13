def convert_array_to_class(data, cls):
    new_data = []
    for i_data in data:
        new_data.append(cls(**i_data).save())
    return new_data
