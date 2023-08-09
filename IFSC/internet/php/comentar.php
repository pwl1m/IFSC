<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>testes php</title>
</head>
<body>
<div class="container">
    <h2>Deixe aqui seu comentario</h2>
    <form action="recebe_comentario.php" method="post">
        <div>
            <input type="text" name="nome" placeholder="digite seu nome" required>
        </div>
        <div>
            <textarea name="comentario" rows="10" required></textarea>
        </div>
        <div>
            <input type="submit" value="salvar">
        </div>

    </form>
</div>
</body>
</html>