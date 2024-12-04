
alunos = {
"nome": "hermione",
"casa": "grifinórnia",
"pratono": "lontra",
}
{
"nome": "harry",
"casa": "grifinórnia",
"pratono": "veado"
}
{
"nome": "rony",
"casa": "grifinórnia",
"pratono": "cachorro"
}
{
"nome": "draco",
"casa": "sonserina",
"pratono": "Jack Russell terrier"
}


print("alunos\t, casa")
for aluno in alunos:
    print(aluno, alunos[aluno], sep= "\t")