nome = input(f"diga o alimnto:")
comidas = {
    {"nome" : "ovo frito", "calorias": "120kcal", "Carboidratos líquidos": "0.60g", "Proteínas": "7.80g" , "Sódio" : "83.00mg"},
    {"nome" : "ovo cusido", "calorias": "155", "carboiratos liquido": "0,27", "Carboidratos": "0.27g",     "Sódio": "65.70mg"},
    {"nome" : "ovo de codorna", "calorias" : "158", "Carboidratos líquidos" : "0.04g", "carboidratos" : "0.4g", "proteinas" : "13g", "sódio" : "141mg"},
    {"nome" : "macarrão", "calorias" : "371","carboidratros liquidos" : "31,97g","caeboidrato" : "33,95g","proteinas" : "13g","sodio" : "6mg"},
    {"nome" : "uva", "calorias" : "67", "carboidratos liquidos" : "0", "calorias" : "0.27g", "proteinas" : "0,6g", "sodio" : "2mg"},
}


for comida in comidas:
    print(comida["nome"], comida["calorias"], comida["carboidratros liquidos"], comida["caeboidrato"], comida["proteinas"], comida["sodio"], sep=", ")

main()