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
select titulo, titulo original
from filmes
where (titulo like '%amor%' OR '%love%')
or (titulo_original like '%amor%' or '%love%');
-- ERRADA

-- 2 Exibir os filmes cujo título é igual ao título original
select titulo, titulo_original 
from filmes
where titulo = titulo_original;



-- 3. Exibir o título e a a duração do filme mais longo.
SELECT titulo, duracao 
FROM filmes 
ORDER BY duracao 
DESC LIMIT 3;

--OR

select titulo, duracao
from filmes
where (select max(duracao) from filmes);

--or

select titulo, duracao
from filmes
where duracao=(select duracao from filmes order by duracao desc limit 1);

-- 4. Exibir os filmes feitos pelo diretor Christopher Nolan.
SELECT f.titulo, d.nome_diretor
FROM filmes f, diretores d
WHERE f.cod_diretor=d.cod_diretor
and d.nome_diretor='Christopher Nolan';

SELECT f.titulo, d.nome_diretor
from filmes f
INNER JOIN diretores d
ON f.cod_diretor=d.cod_diretor
WHERE d.nome_diretor='Christopher Nolan';



-- 5. Exibir o título e o ano de lançamento dos 3 filmes mais recentes feitos pelo ator Brad Pitt.
SELECT titulo, ano_lancamento
FROM filmes, elenco, atores
WHERE filmes.cod_filme = elenco.cod_filme 
AND elenco.cod_ator = atores.cod_ator
AND nome_ator='Brad Pitt'
ORDER BY ano_lancamento
DESC LIMIT 3;

SELECT f.titulo, f.ano_lancamento, a.nome_ator
FROM filmes f
INNER JOIN elenco e
ON f.cod_filme = e.cod_filme
INNER JOIN atores a
ON a.cod_ator=e.cod_ator
WHERE a.nome_ator='Brad PItt'
ORDER BY f.ano_lancamento DESC
LIMIT 3;


--6. Exibir filmes entre 60 e 80 minutos.
SELECT titulo,duracao
FROM filmes
where duracao
BETWEEN 60 and 80;


-- 7. Exibir os atores (sem repetição) de qualquer filme da série Harry Potter.
SELECT DISTINCT a.nome_ator
FROM filmes f, elenco e, atores a 
WHERE f.cod_filme= e.cod_filme 
AND e.cod_ator = a.cod_ator
AND f.titulo LIKE '%Harry Potter%' ORDER BY nome_ator;

--OR E MAIS CORRETA

SELECT DISTINCT a.nome_ator
FROM atores a
INNER JOIN elenco e
ON a.cod_ator=e.cod_ator
INNER JOIN filmes f
ON f.cod_filme=e.cod_filme
WHERE f.titulo LIKE '%Harry Potter%';

-- 8. Exibir os registros da tabela filmes que não contenham um diretor.
SELECT titulo,cod_diretor
FROM filmes
WHERE cod_diretor
IS NULL;

-- 9. Exibir a lista de diretores (sem repetição) que dirigiram algum filme entre 1990 e 1995 (incluindo 1990 e 1995).

SELECT DISTINCT nome_diretor
FROM diretores
WHERE cod_diretor IN
(SELECT cod_diretor
FROM filmes
WHERE ano_lancamento 
BETWEEN '1990' AND '1995');

--OR

SELECT d.nome_diretor, f.ano_lancamento
FROM ditores d 
INNER JOIN filmes f
ON f.cod_diretor=d.cod_diretor
WHERE f.ano_lancamento BETWEEN '1990' AND '1995';


-- 10. ExIbir os filmes de suspense feitos pelo ator Al Pacino.
SELECT f.titulo, a.nome_ator, g.nome_genero
FROM filmeS f, generos g, atores a, elenco e
WHERE f.cod_genero=g.cod_genero
AND e.cod_ator=a.cod_ator
AND f.cod_filme=e.cod_filme
AND nome_genero='Suspense'
AND nome_ator='Al Pacino';

-- OR

SELECT f.titulo, a.nome_ator, g.nome_genero
FROM filmes f
INNER JOIN elenco e
ON f.cod_filme=e.cod_filme
INNER JOIN atores a
ON a.cod_ator=e.cod_ator
INNER JOIN generos g
ON f.cod_genero=g.cod_genero
WHERE a.nome_ator='Al Pacino'
AND g.nome_genero='Suspense';


-- @@@@@@@@@@@@@
-- @FIM LISTA 1@
-- @@@@@@@@@@@@@

-- @@@@@@@@
-- @AULA 2@
-- @@@@@@@@

-- qual o comando SQL que exibe todos os filmes/series/shows de 2006 e seus respectivos diretores?
-- o filme e os respectivos diretores
SELECT f.titulo, d.nome_diretor, f.ano_lancamento
FROM filmes f 
INNER JOIN diretores d
ON f.cod_diretor = d.cod_diretor
WHERE f.ano_lancamento = 2006;

-- e que ele ta trazendo o filme que tem diretor mas tambem o filme que nao tem diretor
SELECT titulo, ano_lancamento, nome_diretor
FROM filmes f 
LEFT JOIN diretores d
ON f.cod_diretor=d.cod_diretor
WHERE ano_lancamento=2006;

-- traz os diretores que possuem filmes e tambem os diretores que nao possuem filmes caso o filme for de 2006
SELECT titulo, ano_lancamento, nome_diretor
FROM filmes f 
RIGHT JOIN diretores d
ON f.cod_diretor=d.cod_diretor
WHERE ano_lancamento=2006;

-- qual o comando sql que exibe todos os filmes/series/shows que não possuem diretores?
-- MAIS DIFICIL
SELECT IFNULL (f.titulo, '--!@#$%&--') 
as filmes, d.nome_diretor
FROM filmes f
RIGHT JOIN diretores d
ON f.cod_diretor=d.cod_diretor;

-- MAIS FACIL
select (TITULO, cod_diretor)
FROM filmes f 
WHERE cod_diretor IS NULL;

-- qual o comando sql que exibe todos os diretores que nao possuem nenhum filme?
SELECT nome_diretor
FROM filmes f 
RIGHT JOIN diretores d 
ON f.cod_diretor=d.cod_diretor
WHERE f.cod_filme IS NULL;

SELECT nome_diretor
FROM filmes f 
LEFT JOIN diretores d 
ON f.cod_diretor=d.cod_diretor
WHERE f.cod_filme IS NULL;

-- encontrar filmes do respectivo ator 
SELECT f.titulo
FROM filmes f
INNER JOIN elenco e
ON f.cod_filme=e.cod_filme
INNER JOIN atores a
ON e.cod_ator=a.cod_ator
WHERE a.nome_ator='Orlando Bloom'
AND f.titulo
IN
(SELECT f.titulo
FROM filmes f
INNER JOIN elenco e
ON f.cod_filme=e.cod_filme
INNER JOIN atores a
ON e.cod_ator=a.cod_ator
WHERE a.nome_ator='Johnny Depp');

-- fim aula 2

-- inicio lista 2

-- 1. Listar o título dos filmes e seu respectivo gênero, incluindo na lista os gêneros que não
-- possuem filmes.

SELECT titulo, nome_genero
FROM filmes f 
RIGHT JOIN generos g
ON f.cod_genero=g.cod_genero;

-- 2. Listar o nome dos atores que atuam nos 5 filmes de maior duração (Dica: usar relações
-- derivadas, order e limit)
--  PRIMEIRA ETAPA
(SELECT titulo, duracao 
FROM filmes
ORDER BY duracao DESC LIMIT 5) AS grandoes

SELECT DISTINCT a.nome_ator
FROM atores a
INNER JOIN elenco e
ON a.cod_ator=e.cod_ator
INNER JOIN (SELECT cod_filme -- tabela virtual
FROM filmes
ORDER BY duracao
DESC LIMIT 5) f -- é a tabela
ON f.cod_filme = e.cod_filme
ORDER BY a.nome_ator;

-- 3. Listar o nome dos atores, em ordem alfabética, que nunca gravaram um filme.

SELECT nome_ator
FROM atores
WHERE cod_ator NOT IN (SELECT cod_ator FROM elenco)
ORDER BY nome_ator; 

-- 4. Listar o título em português dos filmes que sejam dos seguintes gêneros: Infantil,
-- Aventura ou Show (usar consultas aninhadas e a cláusula IN).

SELECT titulo
FROM filmes
WHERE cod_genero IN( SELECT cod_genero FROM generos WHERE 
nome_genero = 'Infantil' OR
nome_genero = 'Aventura' OR
nome_genero = 'Show');

-- 5. Listar o título em português dos filmes dos gêneros: Ação, Infantil e Comédia, lançados
-- após 2005 (usar junção interna e a cláusula IN).

SELECT titulo
FROM filmes
WHERE ano_lancamento> 2005 AND cod_genero IN (
    SELECT cod_genero FROM generos WHERE nome_genero IN ('Ação', 'Infantil', 'Comédia')
);

--OR
-- primeira etapa
SELECT f.titulo, g.nome_genero
FROM filmes f INNER JOIN generos g
ON g.cod_genero=f.cod_genero;

-- segunda etapa
(SELECT cod_genero, nome_genero FROM generos WHERE nome_genero IN ('Ação', 'Infantil', 'Comédia')
) AS g

--juntando as etapas
SELECT f.titulo, g.nome_genero
FROM filmes f INNER JOIN (SELECT cod_genero, nome_genero FROM generos WHERE nome_genero IN ('Ação', 'Infantil', 'Comédia')
) AS g
ON g.cod_genero=f.cod_genero
WHERE ano_lancamento > 2005;

-- 6. Quais diretores não fizeram nenhum filme? Faça este comando SQL sem utilizar a palavra
-- NULL em todo código.

SELECT nome_diretor
FROM diretores
WHERE cod_diretor NOT IN (SELECT d.cod_diretor FROM diretores d INNER JOIN filmes f
ON d.cod_diretor=f.cod_diretor);

-- 7. Exibir a lista de filmes que não possui nenhum ator (elenco).

SELECT titulo, e.cod_ator
FROM filmes f LEFT JOIN elenco e
ON f.cod_filme = e.cod_filme
WHERE e.cod_filme IS NULL;

-- OR
SELECT titulo 
FROM filmes
WHERE cod_filme NOT IN (
    SELECT cod_filme FROM elenco
);