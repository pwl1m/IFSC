

distinct -- elimina linhas iguais

SELECT titulo, ano_lancamento FROM filme WHERE ano_lancamento BETWEEN 2000 AND 2005;

--
SELECT f.titulo,d.nome_diretor, g.nome_genero 
FROM filme f diretor d genero g 
WHERE f.cod_diretor=d.cod_diretor
and f.cod_genero=g.cod_genero;

--
SELECT f.titulo, d.nome_diretor
FROM filmes f, diretores d, generos g 
WHERE f.cod_diretor=d.cod_diretor
and f.cod_genero=g.cod_genero
and g.nome_genero='Suspense';

-- exibe os filmes ordenados pelo ano de lancamento mais antigo para mais  novo removendo campos nulos ou vazios
select titulo, ano_lancamento 
    from filmes 
        where ano_lancamento is not null 
            and ano_lancamento !='' 
                order by ano_lancamento


-- exibir os tres primeiros com maior duracao
select titulo, duracao, ano_lancamento
    from filmes
        order by duracao DESC
            LIMIT 3


-- exibir o 3 4 e 5 com maior duracao
select titulo, duracao, ano_lancamento
    from filmes
        order by duracao DESC
            LIMIT 2,3


-- Exibe os filmes de suspense ou drama
SELECT f.titulo, g.nome_genero
FROM filmes f, generos g
WHERE f.cod_genero=g.cod_genero
AND (g.nome_genero='Suspense' OR g.nome_genero='Drama');
        

-- exeibe os filmes cujo titulo original omecam com the
select titulo_original
from filmes
where titulo_original like 'The%'; -- % ele diz que pode ter qualquer coisa depois desse caracter

-- exibe os filmes cujo titulo terminam com "vivo"
select titulo
from filmes
where titulo_original like '%vivo';

-- exibir filmes que tenham a palavra "rei"
select titulo
from filmes
where titulo like '%rei%';

-- 1 Mostrar filmes onde palavra amor ou love no titulo ou titulo original
select titulo, titulo_original 
from filmes
where titulo or titulo_original
like ('%amor%' or '%love%');
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
SELECT titulo 
FROM filmes f, diretores d
WHERE  f.cod_diretor = d.cod_diretor AND
d.nome_diretor='Cristopher Nolan';
-- ERRADA

-- 5. Exibir o título e o ano de lançamento dos 3 filmes mais recentes feitos pelo ator Brad Pitt.
SELECT titulo, ano_lancamento -- 
FROM filmes f, elenco e, atores a --
WHERE f.cod_filme = e.cod_filme AND --
e.cod_ator = a.cod_ator AND --
nome_ator='Brad Pitt' --
ORDER BY ano_lancamento --
DESC LIMIT 3; --

SELECT titulo, ano_lancamento -- 
FROM filmes f, elenco e, atores a --
WHERE f.cod_filme= e.cod_filme -- SE CONECNTAM
    AND e.cod_ator = a.cod_ator 
    AND a.nome_ator='Brad Pitt' -- SE CONECNTAM 
    ORDER BY ano_lancamento --
    DESC LIMIT 3; --


--6. Exibir filmes curtos, entre 60 e 80 minutos.
SELECT titulo,duracao
FROM filmes
where duracao
BETWEEN 60 and 80;


-- 7. Exibir os atores (sem repetição) de qualquer filme da série Harry Potter.
select distinct a.nome_ator
FROM filmes f, elenco e, atores a 
WHERE f.cod_filme= e.cod_filme 
AND e.cod_ator = a.cod_ator
AND f.titulo LIKE '%Harry Potter%' ORDER BY nome_ator;


-- 8. Exibir os registros da tabela filmes que não contenham um diretor.
SELECT titulo,cod_diretor
FROM filmes
WHERE cod_diretor
IS NULL;

-- 9. Exibir a lista de diretores (sem repetição) que dirigiram algum filme entre 1990 e 1995
-- (incluindo 1990 e 1995).
SELECT d.cod_diretor, f.ano_lancamento
FROM filmes f, diretores d
WHERE f.cod_diretor = d.cod_diretor AND f.ano_lancamento = d.nome_diretor
BETWEEN 1990 and 1995;
-- ERRADA

-- 10. ExIbir os filmes de suspense feitos pelo ator Al Pacino.[NAO FEITO]
SELECT titulo
FROM filme f, generos g, atores a, elenco e
WHERE f.cod_genero=g.cod_genero -- ligou a tabela filme com genero
WHERE f.cod_filme=e.cod_filme --
AND e.cod_ator=a.cod_ator 
AND nome_genero='Suspense' 
AND nome_ator='Al Pacino';

-- qual o comando SQL que exibe todos os filmes/series/shows de 2006 e seus respectivos diretores?
SELECT f.titulo, d.nome_diretor, f.ano_lancamento
FROM filmes f 
INNER JOIN diretores d
ON f.cod_diretor = d.cod_diretor
WHERE f.ano_lancamento = 2006;
-- ERRADO

-- CORRETA
SELECT TITULO, ano_lancamento, nome_diretor
FROM filmes f 
LEFT JOIN diretores d
ON f.cod_diretor=d.cod_diretor
WHERE ano_lancamento=2006;


-- qual o comando sql que exibe todos os filmes/series/shows que não possuem diretores?
SELECT IFNULL (f.titulo, '----') as filmes, d.nome_diretor
FROM filmes f RIGHT JOIN diretores d
ON f.cod_diretor=d.cod_diretor;
-- MAIS DIFICIL

-- MAIS FACIL
SELECT TITULO, cod_diretor
FROM filmes f 
WHERE cod_diretor IS NULL;


-- qual o comando sql que exibe todos os diretores que nao possuem nenhum filme?
SELECT nome_diretor
    FROM filmes f RIGHT JOIN diretores d 
        ON f.cod_diretor=d.cod_diretor
            WHERE f.cod_filme IS NULL;

-- encontrar filmes do respectivo ator 
SELECT f.titulo
FROM filmes f 
LEFT JOIN elenco e ON f.cod_filme=e.cod_filme
LEFT JOIN atores a ON e.cod_ator=a.cod_ator 
WHERE a.nome_ator='Orlando Bloom' AND
f.titulo IN
(SELECT f.titulo
FROM filmes f 
LEFT JOIN elenco e ON f.cod_filme=e.cod_filme
LEFT JOIN atores a ON e.cod_ator=a.cod_ator 
WHERE a.nome_ator='Johnny Depp')












