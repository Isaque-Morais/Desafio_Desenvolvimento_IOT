from typing import AnyStr


def numero_cnpj_iguais(numero, cnpj, lista_de_erros):
    """Verifica se numero e cnpj são iguais"""
    if numero == cnpj:
            lista_de_erros['cnpj'] = 'O CNPJ não pode ter o mesmo Nº da nota.'

#falta fazer a validação para receber apenas números nos campos
def campo_tem_alguma_letra(valor_campo, nome_campo, lista_de_erros):
    """"Verifica se possui alguma letra neste campo"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua letras neste campo.'

