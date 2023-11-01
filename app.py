from pathlib import Path
from functions import browse, show_files
import sys

PATH_DEFAULT='files'
path_work=PATH_DEFAULT

print('Navegador de arquivos\n')



if len(sys.argv) > 1:
    path_work_temp = sys.argv[1]

    if path_work_temp != '':
        p =Path (path_work_temp)
        if  p.exists() and p.is_dir():
            path_work= path_work_temp


print('A busca foi começada...\n')
tree = browse(Path(path_work))

show_files(tree)
print('\nA busca foi concluida com sucesso!')



