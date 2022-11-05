import os,openpyxl
path = os.getcwd()+'/uploads/input.xlsx'

def import_data(path):
    table = openpyxl.load_workbook(path)
    sheet = table.active

    obj_list = []

    for row in sheet.iter_rows():
        obj = {
            'location':row[0].value,
            'rooms_count':row[1].value,
            'segment': row[2].value,
            'floors': row[3].value,
            'walls': row[4].value,
            'floor_number': row[5].value,
            'square': row[6].value,
            'kitchen': row[7].value,
            'balcony': row[8].value,
            'from_metro': row[9].value,
            'wall_decoration': row[10].value
        }
        obj_list.append(obj)

        return obj_list