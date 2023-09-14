from yaml import load, dump
import sys

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper



with open(f'{sys.argv[1]}.yaml', encoding='utf-8') as f:
    zadani = load(f.read(), Loader)

sablona_zacatek = '''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
  </head>
  <body><div class=".container-fluid mx-auto w-100 p-3">
  <h1 style="text-align: center">Horniny kolem nás</h1>
    <h3 class="text-muted" style="text-align: center">Vojtěch Čečka</h3>
    
    <p>Horniny jsou heterogenní směsi minerálů. Dělíme je na vyvřelé, usazené a přeměněné. Vyvřelé horniny najdeme, jak na po vrchu a mělko pod povrchem, tak hluboko pod zemí (v tzv. plutonech). Jedná se o ztuhlé magma. Usazené horniny najdeme na povrchu, protože vznikají rozmělněním jiných hornin na drobné částice a jejich následným usazením. Přeměněné horniny vznikají přeměnou jiných hornin za vysokého tlaku a teploty. Najdeme je převážně v hloubce, neboť na povrchu dostatečně vysoký tlak a teplotu není.</p> \n

  <div class="row">'''

sablona_konec = '''  </div>
  
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
  </body>
</html>'''

output = ''
output += sablona_zacatek

for i,zaznam in enumerate(zadani):
    karta_output = '<div class="card m-2 border border-2 col p-0">'
    
    try:
        karta_output += f"<img src=\"{zaznam['image']}\" class=\"card-img-top\">"
    except KeyError:
        pass
    
    try:
        karta_output += f"<div class=\"card-header\">{zaznam['name']}</div>"
    except KeyError:
        pass
    
    karta_output += '<div class="card-body row">'
    
    try:
        karta_output += f"<img src=\"{zaznam['image_left']}\" class=\"col-sm-4\">"
        karta_output += '<dl class=\"col-sm-8\">'
    except KeyError:
        karta_output += '<dl class=\"col\">'
    

    for polozka in zaznam:
        if polozka in ('name', 'image', 'image_left'):
            continue
        
        karta_output += f"<dt>{polozka}</dt><dd>{zaznam[polozka]}</dd>"

    karta_output += '</dl></div></div>'
    
    if i % 2:
        karta_output += '</div><div class="row">'

    output += karta_output + '\n'

output += sablona_konec

with open(f'{sys.argv[1]}.html', 'w', encoding='utf-8') as f:
    f.write(output)
