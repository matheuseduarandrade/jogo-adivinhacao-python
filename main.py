secret_number = 42
secret_animal = "dragao"
secret_metal = "prata"

print("Bem-vindo ao jogo de adivinhação!" + "\n" + "*" * 33)
question_1 = int(input("Qual número estou pensando? "))
question_2 = input("Estou pensando em um animal mágico… Ele voa, é dourado e guarda tesouros. Qual é?")
question_3 = input("Em muitas lendas, qual metal é considerado mortal para lobisomens?")



while question_1 != secret_number or question_2.strip().lower() != secret_animal or question_3.strip().lower() != secret_metal:
    print("Haha! Você está preso no meu loop!")
    
    if question_1 != secret_number:
        question_1 = int(input("Tente novamente! Qual número estou pensando? "))
    if question_2.strip().lower() != secret_animal:
        question_2 = input("Tente novamente! Estou pensando em um animal mágico… Ele voa, é dourado e guarda tesouros. Qual é? ")
    if question_3.strip().lower() != secret_metal:
        question_3 = input("Tente novamente! Em muitas lendas, qual metal é considerado mortal para lobisomens? ")

print("\nMuito bem, trouxa! Você está livre agora!")