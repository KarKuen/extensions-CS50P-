name = input('File name: ')

if '.' in name:
    name = name.split('.')[-1].lower().strip()
else:
    name = name.lower().strip()

match name:
    case 'gif':
        print('image/' + name)
    case 'jpg'|'jpeg':
        print('image/jpeg')
    case 'png':
        print('image/' + name)
    case 'pdf':
        print('application/' + name)
    case 'txt':
        print('text/plain')
    case 'zip':
        print('application/' + name)
    case _ :
        print('application/octet-stream')