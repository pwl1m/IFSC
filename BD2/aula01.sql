-- @@@@@@@@@@@@@@@@
-- @INICIO REVISÃO@
-- @@@@@@@@@@@@@@@@
-- O comando 
INSERT
-- INSERT INTO tabela (lista atributos)
-- VALUES (lista de valores)
-- Exemplo:
INSERT INTO filmes (cod_filme, titulo_original, titulo, duracao, ano_lancamento, cod_diretor, cod_genero)
VALUES (143, 'Pretty Woman', 'Uma Linda Mulher', NULL, '1990', 76, 6);

-- O comando 
UPDATE
--  UPDATE tabela 
-- SET atributo=valor1, atributo2=valor2 
-- WHERE condicao;
-- Exemplo:
UPDATE filmes SET cod_genero='10', duracao='119' WHERE cod_filme='143';

-- O comando
DELETE
-- DELETE FROM tabela WHERE condicao
-- Exemplo:
DELETE FROM filmes WHERE cod_filme=143;

-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
-- exibe o título do filme e o nome do respectivo diretor
SELECT titulo, nome_diretor
 FROM filmes, diretores
 WHERE filmes.cod_diretor = diretores.cod_diretor
-- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

-- ou com apelidos para tabelas
SELECT titulo, nome_diretor
 FROM filmes f, diretores d
 WHERE f.cod_diretor = d.cod_diretor

-- elimina linhas iguais
SELECT DISTINCT ano_lancamento FROM filmes
-- nome temporário para coluna
SELECT titulo, ano_lancamento AS 'Ano de lançamento' FROM filmes

-- diferente do ano 2000
SELECT titulo, ano_lancamento
 FROM filmes 
 WHERE ano_lancamento <> 2000

-- ou
SELECT titulo, ano_lancamento
 FROM filmes 
 WHERE ano_lancamento != 2000

-- filmes que NÃO foram lançados entre 2000 e 2005
SELECT titulo, ano_lancamento
 FROM filmes 
 WHERE ano_lancamento NOT BETWEEN 2000 AND 2005

-- Exibe o título do filme e o nome do respectivo diretor e respectivo gênero
SELECT f.titulo, d.nome_diretor, g.nome_genero
 FROM filmes f, diretores d, generos g
 WHERE f.cod_diretor = d.cod_diretor 
 AND f.cod_genero=g.cod_genero;

-- exibe os filmes ordenados pelo ano de lancamento mais antigo para mais  novo removendo campos nulos ou vazios
select titulo, ano_lancamento 
    from filmes 
        where ano_lancamento is not null 
            and ano_lancamento !=''
                order by ano_lancamento;

select titulo, ano_lancamento     
    from filmes 
            where ano_lancamento !='' 
                order by ano_lancamento;

-- exibir os tres primeiros com maior duracao
select titulo, duracao, ano_lancamento
    from filmes
        order by duracao DESC
            LIMIT 3;

-- exibir o 3 4 e 5 com maior duracao
select titulo, duracao, ano_lancamento from filmes order by duracao 
DESC LIMIT 2,3; -- a partir do X (2), e Y 3 filmes
DESC LIMIT 10,10; -- a partir do 10, 10 filmes

-- Exibe os filmes de suspense ou drama
SELECT f.titulo, g.nome_genero
FROM filmes f, generos g
WHERE f.cod_genero=g.cod_genero
AND (g.nome_genero='Suspense' OR g.nome_genero='Drama');

-- descobrir os filmes com o codigo e nome do diretor Tim Hill ou não esta nulo
SELECT f.titulo, d.cod_diretor, d.nome_diretor
FROM filmes f, diretores d
WHERE f.cod_diretor=d.cod_diretor
and d.nome_diretor is not null;
and d.nome_diretor='Tim Hill';

-- exeibe os filmes cujo titulo original comecam com 'the'
select titulo_original
from filmes
where titulo_original like 'The%'; -- % ele diz que pode ter qualquer coisa depois desse caracter

-- exeibe os filmes cujo titulo original tenha a letra u
select titulo_original
from filmes
where titulo_original like '%u%';

-- exibir nomes que o nome do ator tenha letra A
SELECT DISTINCT a.nome_ator, e.cod_filme, f.titulo
from filmes f, elenco e, atores a
where f.cod_filme=e.cod_filme
and a.nome_ator like '%xx';

-- exibe os filmes cujo titulo terminam com "vivo"
select titulo
from filmes
where titulo_original like '%vivo';

-- exibir filmes que tenham a palavra "rei"
select titulo
from filmes
where titulo like '%rei%';

-- @@@@@@@@@@@@@
-- @FIM REVISÃO@
-- @@@@@@@@@@@@@
-- ######################
-- @@@@@@@@@@@@@@@@
-- @INICIO LISTA 1@
-- @@@@@@@@@@@@@@@@

-- 1 Mostrar filmes onde palavra amor ou love no titulo ou titulo original
select titulo, titulo_original 
from filmes
where titulo <> titulo_original
like 'amor%';
-- ERRADA

-- 2 Exibir os filmes cujo título é igual ao título original
select titulo, titulo_original 
from filmes
where titulo = titulo_original

-- 3. Exibir o título e a a duração do filme mais longo.
SELECT titulo, duracao 
FROM filmes 
ORDER BY duracao 
DESC LIMIT;

-- 4. Exibir os filmes feitos pelo diretor Christopher Nolan.
SELECT f.titulo, d.nome_diretor
FROM filmes f, diretores d
WHERE f.cod_diretor=d.cod_diretor
and d.nome_diretor='Christopher Nolan';


-- 5. Exibir o título e o ano de lançamento dos 3 filmes mais recentes feitos pelo ator Brad Pitt.
SELECT titulo, ano_lancamento
FROM filmes, elenco, atores
WHERE filmes.cod_filme = elenco.cod_filme 
AND elenco.cod_ator = atores.cod_ator
AND nome_ator='Brad Pitt'
ORDER BY ano_lancamento
DESC LIMIT 3;

--6. Exibir filmes entre 60 e 80 minutos.
SELECT titulo,duracao
FROM filmes
where duracao
BETWEEN 60 and 80;


-- 7. Exibir os atores (sem repetição) de qualquer filme da série Harry Potter.
SELECT DISTINCT a.nome_ator, titulo
FROM filmes f, elenco e, atores a 
WHERE f.cod_filme= e.cod_filme 
AND e.cod_ator = a.cod_ator
AND f.titulo LIKE '%Harry Potter%' ORDER BY nome_ator;


-- 8. Exibir os registros da tabela filmes que não contenham um diretor.
SELECT titulo,cod_diretor
FROM filmes
WHERE cod_diretor
IS NULL;

-- 9. Exibir a lista de diretores (sem repetição) que dirigiram algum filme entre 1990 e 1995 (incluindo 1990 e 1995).
SELECT DISTINCT f.titulo, d.nome_diretor, f.ano_lancamento
FROM filmes f, diretores d
WHERE f.cod_diretor = d.cod_diretor 
AND f.ano_lancamento 
BETWEEN 1990 and 1995;

-- 10. ExIbir os filmes de suspense feitos pelo ator Al Pacino.[NAO FEITO]
SELECT f.titulo, a.nome_ator, g.nome_genero
FROM filmeS f, generos g, atores a, elenco e
WHERE f.cod_genero=g.cod_genero
AND f.cod_filme=e.cod_filme
AND e.cod_ator=a.cod_ator
AND nome_genero='Suspense'
AND nome_ator='Al Pacino';
-- @@@@@@@@@@@@@
-- @FIM LISTA 1@
-- @@@@@@@@@@@@@
-- ######################
-- @@@@@@@@
-- @AULA 2@
-- @@@@@@@@
