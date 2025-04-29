from app.funcao import funcao_ola_turma

def test_funcao_ola_turma_retorna_ola_jornda():
    saida = funcao_ola_turma()
    gabarito = 'ola_jornada'
    assert saida == gabarito