def get_list_of_wagons(*args):
    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    x,y,z,*rest=each_wagons_id
    each_wagons_id=*rest,x,y
    *newlist,=z,*missing_wagons,*each_wagons_id
    return newlist

#print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))
def add_missing_stops(route,**kwargs):
    return {**route,"stops":list(kwargs.values())}

def extend_route_information(route, more_route_information):
    return {**route,**more_route_information}

def fix_wagon_deposit(wagons_rows):
    [*first_row], [*second_row], [*third_row] = zip(*wagons_rows)
    
    return [first_row, second_row, third_row]

