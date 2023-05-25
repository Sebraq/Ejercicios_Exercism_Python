def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return tuple(coordinate)

def compare_records(azara_record,rui_record):
    coord=convert_coordinate(get_coordinate(azara_record))
    return coord in rui_record

def create_record(azara_record,rui_record):
    if compare_records(azara_record,rui_record):
        return azara_record+rui_record
    return "not a match"

def clean_up(combined_record_group):
    result=""
    for inner in combined_record_group:
        temp=(inner[0], inner[2], inner[3], inner[4])
        result += str(temp)+'\n'
    return result
