def save_file(aluno):
    try:
        f = open("students.txt", "a")
        f.write(student + "/n")
        f.close
    except Exception as error:
        print("Não foi possivel salvar o arquivo")
        print(error)


students = []
def read_file():
    try:
        f = open("students.txt", "r")
        for aluno in f.readlines():
            students.append(aluno)
        f.close()
    except Exception as error:
        print("Could not read file")

'''
COMANDO Open:
    "w" - escrever no arquivo
    "r" - Ler o arquivo
    "a" - Acrescentar para um novo ou para um arquivo existente
    "rb" - ler um arquivo binario
    "wb" - escrever em um arquivo binario 
'''