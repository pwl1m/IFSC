<?php
// recebe comentario
$nome = $_POST['NOME'];
$comentario = $_POST['comentario'];
date_default_timezone_set('America/Sao_Paulo');

// criar uma variavel com todo o texto
$msg = '<div class="comentario">';
$msg .= "<small>$nome - ".date('d/m/Y h:i').'</small>';
$msg .= "<p>$comentario</p>";
$msg .= '</div>';
$msg .= "\n\n";

// salvar no arquivo texto
file_put_contents('comentarios.txt', $msg, FILE_APPEND);

// redireciona...
header('Location: comentarios.php');