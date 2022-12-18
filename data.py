import elfbars

bc5000ultra = elfbars.ELFBARBC5000ULTRA()
bc4000 = elfbars.ELFBARBC4000()
bc3000 = elfbars.ELFBARBC3000()
lux2000 = elfbars.ELFBAR2000LUX()
lux1500 = elfbars.ELFBAR1500LUX()


def callback_data(callback):
    if callback == f'{bc5000ultra.name}g':
        return bc5000ultra.gusturi
    elif callback == f'{bc4000.name}g':
        return bc4000.gusturi
    elif callback == f'{bc3000.name}g':
        return bc3000.gusturi
    elif callback == f'{lux2000.name}g':
        return lux2000.gusturi
    elif callback == f'{lux1500.name}g':
        return lux1500.gusturi

    if callback == f'{bc5000ultra.name}p':
        return bc5000ultra.price
    elif callback == f'{bc4000.name}p':
        return bc4000.price
    elif callback == f'{bc3000.name}p':
        return bc3000.price
    elif callback == f'{lux2000.name}p':
        return lux2000.price
    elif callback == f'{lux1500.name}p':
        return lux1500.price

    if callback == f'{bc5000ultra.name}gd':
        return bc5000ultra.gusturi_disponibile
    elif callback == f'{bc4000.name}gd':
        return bc4000.gusturi_disponibile
    elif callback == f'{bc3000.name}gd':
        return bc3000.gusturi_disponibile
    elif callback == f'{lux2000.name}gd':
        return lux2000.gusturi_disponibile
    elif callback == f'{lux1500.name}gd':
        return lux1500.gusturi_disponibile

def elfbar_photo(elfbar_name):
    if elfbar_name == bc5000ultra.name:
        photo = open('photo/BC5000ULTRA.png','br')
        return photo
    elif elfbar_name == bc4000.name:
        photo = open('photo/BC4000.png','br')
        return photo
    elif elfbar_name == bc3000.name:
        photo = open('photo/BC3000.png','br')
        return photo
    elif elfbar_name == lux2000.name:
        photo = open('photo/2000LUX.png','br')
        return photo
    elif elfbar_name == lux1500.name:
        photo = open('photo/1500LUX.png','br')
        return photo
