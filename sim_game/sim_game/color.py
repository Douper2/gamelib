import variables

def process_colors(*args):
    result_colors = []
    
    for arg in args:
        if isinstance(arg, str):
            color_value = variables.color_dict.get(arg.lower())
            if color_value:
                result_colors.append(color_value)
            else:
                raise ValueError(f"Unknown color name: {arg}")
        elif isinstance(arg, int):
            if 0 <= arg <= 255:
                result_colors.append((arg, arg, arg))
            else:
                raise ValueError(f"Invalid grayscale value: {arg}")
        else:
            raise TypeError(f"Unsupported argument type: {type(arg)}")
    
    return result_colors