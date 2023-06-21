
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
WHERE a.nome_ator='Orlando Bloom' AND  a.nome_ator='Johnny Depp');
AND f.titulo
IN
(SELECT f.titulo
FROM filmes f
INNER JOIN elenco e
ON f.cod_filme=e.cod_filme
INNER JOIN atores a
ON e.cod_ator=a.cod_ator
WHERE a.nome_ator='Johnny Depp');