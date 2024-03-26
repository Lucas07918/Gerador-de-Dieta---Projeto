from flask import Flask, render_template, redirect, request, flash, send_from_directory
import json
import random
import math

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LALA'

@app.route('/')
def page1():
    return render_template('calculo.html')

@app.route('/calculoTop', methods=['POST'])
def calculoTop():
    altura = int(request.form.get('altura'))
    idade = int(request.form.get('idade'))
    atividade = float(request.form.get('atividade'))
    peso = int(request.form.get('peso'))
    sexo = int(request.form.get('sexo'))
    objetivo = int(request.form.get('objetivo'))
    velocidade = int(request.form.get('velocidade'))

    if objetivo == 1:
        pesoAlcancar = 0
    else:
        pesoAlcancar = int(request.form.get('pesoAlcancar'))


    if sexo == 1:
        tmb = (88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)) * atividade
    else:
        tmb = (447.593  + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)) * atividade
    
    if objetivo == 1:
        kcalPDia = math.ceil(tmb)
        tempo = 0
    elif objetivo == 2:
        necessario = (pesoAlcancar - peso) * 7000
        tempo = necessario / velocidade
        kcalPDia = math.ceil((velocidade / 7) + tmb)
    elif objetivo == 3:
        necessario = (peso - pesoAlcancar) * 7000
        tempo = necessario / velocidade
        kcalPDia = math.ceil(tmb - (velocidade / 7))
    
    info = [
        {
            'kcalNecessarias': kcalPDia,
            'tempo': tempo
        }
    ]
    with open('./JSON/inputValue.json', 'w') as gravarTemp:
        json.dump(info, gravarTemp, indent=4)
    return redirect('/gerarTodos')

@app.route('/gerarTodos')
def gerarTodos():
    with open('./JSON/inputValue.json', 'r') as valueTemp:
        values = json.load(valueTemp)
    for i in values:
        qtdCalorias = i.get('kcalNecessarias')
    qtdCafe = 0.2 * qtdCalorias
    with open('./JSON/cafeConjuntos.json', 'r', encoding='utf-8') as alimentosTemp:
        alimentos = json.load(alimentosTemp)
        grupo = random.sample(alimentos, 1) 
    var = []
    for i in grupo:
        conjuntos = i.get('conjuntos')
        for i in conjuntos:
           caloriaMax = int(i.get('calorias'))
           if caloriaMax < qtdCafe:
               item = i.get('item')
               for i in item:
                   conjunto = i.get('conjunto')
                   var.append(conjunto)
    resultado = random.sample(var, 1)
    cardapioNovos = []
    cardapioNovos = resultado[0]    
    with open('./JSON/cafeDaManhaDieta.json', 'w', encoding='utf-8') as gravarTemp:
        json.dump(cardapioNovos, gravarTemp, indent=4)

    with open('./JSON/inputValue.json', 'r') as valueTemp:
        values = json.load(valueTemp)
    for i in values:
        qtdCalorias = i.get('kcalNecessarias')
    qtdCafe = 0.4 * qtdCalorias
    with open('./JSON/almocoConjuntos.json', 'r', encoding='utf-8') as alimentosTemp:
        alimentos = json.load(alimentosTemp)
        grupo = random.sample(alimentos, 1)
    var = []
    for i in grupo:
        conjuntos = i.get('conjuntos')
        for i in conjuntos:
           caloriaMax = int(i.get('calorias'))
           if caloriaMax < qtdCafe:
               item = i.get('item')
               for i in item:
                   conjunto = i.get('conjunto')
                   var.append(conjunto)
    resultado = random.sample(var, 1)
    cardapioNovos = []
    cardapioNovos = resultado[0]
    with open('./JSON/almocoDieta.json', 'w', encoding='utf-8') as gravarTemp:
        json.dump(cardapioNovos, gravarTemp, indent=4)

    with open('./JSON/inputValue.json', 'r') as valueTemp:
        values = json.load(valueTemp)
    for i in values:
        qtdCalorias = i.get('kcalNecessarias')
    qtdCafe = 0.4 * qtdCalorias
    with open('./JSON/jantarConjuntos.json', 'r', encoding='utf-8') as alimentosTemp:
        alimentos = json.load(alimentosTemp)
        grupo = random.sample(alimentos, 1)
    var = []
    for i in grupo:
        conjuntos = i.get('conjuntos')
        for i in conjuntos:
           caloriaMax = int(i.get('calorias'))
           if caloriaMax < qtdCafe:
               item = i.get('item')
               for i in item:
                   conjunto = i.get('conjunto')
                   var.append(conjunto)
    resultado = random.sample(var, 1)
    cardapioNovos = []
    cardapioNovos = resultado[0] 
    with open('./JSON/jantarDieta.json', 'w', encoding='utf-8') as gravarTemp:
        json.dump(cardapioNovos, gravarTemp, indent=4)
    return redirect('/page2')

@app.route('/page2')
def dieta():
    with open('./JSON/cafeDaManhaDieta.json', 'r', encoding='utf-8') as Temp:
        cafe = json.load(Temp)
    with open('./JSON/almocoDieta.json', 'r', encoding='utf-8') as Temp:
        almoco = json.load(Temp)
    with open('./JSON/jantarDieta.json', 'r', encoding='utf-8') as Temp:
        jantar = json.load(Temp)
    with open('./JSON/inputValue.json', 'r') as valueTemp:
        values = json.load(valueTemp)
    for i in values:
        calorias = i.get('kcalNecessarias')
        tempo = i.get('tempo')
    return render_template('dieta.html', cafe = cafe, almoco = almoco, jantar = jantar, calorias = calorias, tempo = tempo)

@app.route('/salvar')
def salvar():
    with open('./JSON/cafeDaManhaDieta.json', 'r', encoding='utf-8') as Temp:
        cafe = json.load(Temp)
    with open('./JSON/almocoDieta.json', 'r', encoding='utf-8') as Temp:
        almoco = json.load(Temp)
    with open('./JSON/jantarDieta.json', 'r', encoding='utf-8') as Temp:
        jantar = json.load(Temp)
    with open('./JSON/inputValue.json', 'r', encoding='utf-8') as inputTemp:
        inputvalue = json.load(inputTemp)

    with open('./JSON/Salvo/cafeDaManhaDietaSalvo.json', 'w', encoding='utf-8') as GravarCafeSalvo:
        json.dump(cafe, GravarCafeSalvo, indent=4)
    with open('./JSON/Salvo/almocoDietaSalvo.json', 'w', encoding='utf-8') as GravarAlmocoSalvo:
        json.dump(almoco, GravarAlmocoSalvo, indent=4)
    with open('./JSON/Salvo/jantarSalvo.json', 'w', encoding='utf-8') as GravarJantarSalvo:
        json.dump(jantar, GravarJantarSalvo, indent=4)
    with open('./JSON/Salvo/inputValueSalvo.json', 'w', encoding='utf-8') as GravarInputSalvo:
        json.dump(inputvalue, GravarInputSalvo, indent=4)

    return redirect('/DietaSalva')

@app.route('/DietaSalva')
def DietaSalva():
    with open('./JSON/Salvo/cafeDaManhaDietaSalvo.json', 'r', encoding='utf-8') as CafeTemp:
        cafeSalvo = json.load(CafeTemp)
    with open('./JSON/Salvo/almocoDietaSalvo.json', 'r', encoding='utf-8') as almocoTemp:
        almocoSalvo = json.load(almocoTemp)
    with open('./JSON/Salvo/jantarSalvo.json', 'r', encoding='utf-8') as jantarTemp:
        jantarSalvo = json.load(jantarTemp)
    with open('./JSON/Salvo/inputValueSalvo.json', 'r', encoding='utf-8') as inputSalvoTemp:
        inputvalueSalvo = json.load(inputSalvoTemp)

    for i in inputvalueSalvo:
        calorias = i.get('kcalNecessarias')
        tempo = i.get('tempo')

    return render_template("salvo.html", cafe = cafeSalvo, almoco = almocoSalvo, jantar = jantarSalvo, calorias = calorias, tempo = tempo)

@app.route('/gerarCafe')
def gerarCafe():
    with open('./JSON/inputValue.json', 'r') as valueTemp:
        values = json.load(valueTemp)
    for i in values:
        qtdCalorias = i.get('kcalNecessarias')
    qtdCafe = 0.2 * qtdCalorias
    with open('./JSON/cafeConjuntos.json', 'r', encoding='utf-8') as alimentosTemp:
        alimentos = json.load(alimentosTemp)
        grupo = random.sample(alimentos, 1) 
    var = []
    for i in grupo:
        conjuntos = i.get('conjuntos')
        for i in conjuntos:
           caloriaMax = int(i.get('calorias'))
           if caloriaMax < qtdCafe:
               item = i.get('item')
               for i in item:
                   conjunto = i.get('conjunto')
                   var.append(conjunto)
    resultado = random.sample(var, 1)
    cardapioNovos = []
    cardapioNovos = resultado[0]   
    with open('./JSON/cafeDaManhaDieta.json', 'w', encoding='utf-8') as gravarTemp:
        json.dump(cardapioNovos, gravarTemp, indent=4)
    return redirect('/page2')

@app.route('/gerarAlmoco')
def gerarAlmoco():
    with open('./JSON/inputValue.json', 'r') as valueTemp:
        values = json.load(valueTemp)
    for i in values:
        qtdCalorias = i.get('kcalNecessarias')
    qtdCafe = 0.4 * qtdCalorias
    with open('./JSON/almocoConjuntos.json', 'r', encoding='utf-8') as alimentosTemp:
        alimentos = json.load(alimentosTemp)
        grupo = random.sample(alimentos, 1)
    var = []
    for i in grupo:
        conjuntos = i.get('conjuntos')
        for i in conjuntos:
           caloriaMax = int(i.get('calorias'))
           if caloriaMax < qtdCafe:
               item = i.get('item')
               for i in item:
                   conjunto = i.get('conjunto')
                   var.append(conjunto)
    resultado = random.sample(var, 1)
    cardapioNovos = []
    cardapioNovos = resultado[0]    
    with open('./JSON/almocoDieta.json', 'w', encoding='utf-8') as gravarTemp:
        json.dump(cardapioNovos, gravarTemp, indent=4)
    return redirect('/page2')

@app.route('/gerarJantar')
def gerarJantar():
    with open('./JSON/inputValue.json', 'r') as valueTemp:
        values = json.load(valueTemp)
    for i in values:
        qtdCalorias = i.get('kcalNecessarias')
    qtdCafe = 0.4 * qtdCalorias
    with open('./JSON/jantarConjuntos.json', 'r', encoding='utf-8') as alimentosTemp:
        alimentos = json.load(alimentosTemp)
        grupo = random.sample(alimentos, 1)
    var = []
    for i in grupo:
        conjuntos = i.get('conjuntos')
        for i in conjuntos:
           caloriaMax = int(i.get('calorias'))
           if caloriaMax < qtdCafe:
               item = i.get('item')
               for i in item:
                   conjunto = i.get('conjunto')
                   var.append(conjunto)
    resultado = random.sample(var, 1)
    cardapioNovos = []
    cardapioNovos = resultado[0]    
    with open('./JSON/jantarDieta.json', 'w', encoding='utf-8') as gravarTemp:
        json.dump(cardapioNovos, gravarTemp, indent=4)
    return redirect('/page2')

if __name__ in "__main__":
    app.run(debug=True)