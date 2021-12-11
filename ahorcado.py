import random
import os


def run():
    words=[]

    #with open ("./data.txt", "r", encoding="utf-8") as f:
    with open ("/home/adrian/Documentos/proyectos/ahorcado/data.txt", "r", encoding="utf*8") as f:
        for line in f:
            words.append(line.strip())
        
    selected_word=random.choice(words)
    selected_word_list=[letter for letter in selected_word]
    selected_word_list_space=["_"]*len(selected_word_list)
    letter_index_dict={}
    for idx, letter in enumerate(selected_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter]=[]
        letter_index_dict[letter].append(idx)

    #print(selected_word)
    #print(selected_word_list)
    #print(selected_word_list_space)
    #print(letter_index_dict)
    #prueba de git

    while True:
        os.system("clear")
        print("Adivina la palabra!")
        for element in selected_word_list_space:
            print(element+" ",end="")
        print("\n")

        letter=input("Ingresa una letra: ").strip()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in selected_word_list:
            for idx in letter_index_dict[letter]:
                selected_word_list_space[idx]=letter

        if "_" not in selected_word_list_space:
            os.system("clear")
            print("Ganaste! la palabra era", selected_word)
            break
        

if __name__ == "__main__":
    run()