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
    <?php        
        echo '<h1>Testes com PHP</h1>';
        $nome = 'Paulo';
        echo 'meu nome é: '.$nome;
        echo "<br>meu nome é: $nome.";
        echo '<br>meu nome é: $nome.<br>';

        $a = 5;
        $b = 5;
        echo '<br>'.$a+$b;

        if($a>$b){
            echo '<p> a é maior que b</p>';
        }
        elseif($b>$a){
            echo '<p> b é maior que a</p>';
        }
        else{
            echo '<p>a e b são iguais</p>';
        }
    ?>
    </div>
</body>
</html>