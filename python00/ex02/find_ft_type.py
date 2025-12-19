def all_thing_is_obj(object: any) -> int:
    type_dic = {
        list: 'List',
        tuple: 'Tuple',
        set: 'Set',
        dict: 'Dict',
        str:  f'{object} is in the kitchen'
    }
    
    obj_type = type(object)
    if obj_type not in type_dic.keys():
        print("Type not found")
    else:
        print(f"{type_dic[obj_type]} : {obj_type}")
    return 42