def get_details_from_postal_code(postal_code: str):
    postal_code = postal_code.upper()
    return_list = []
    location = postal_code[1]
    province_dictionary = {'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island', 'E': 'New Brunswick',
                           'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec', 'K': 'Ontario'
        , 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario', 'R': 'Manitoba', 'S': 'Saskatchewan',
                           'T': 'Alberta', 'V': 'British Columbia', 'X': 'Nunavut or Northwest Territories',
                           'Y': 'Yukon', }
    if postal_code[0] in province_dictionary:
        return_list.append(province_dictionary[postal_code[0]])
    match location:
        case '0':
            return_list.append('rural')
        case _:
            return_list.append('urban')
    return return_list