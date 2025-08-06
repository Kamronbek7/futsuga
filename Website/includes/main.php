<?php

function title($name) {
    return "<title>". $name . "</title>";
}

function code_color($type, $text) {
    $code = '';
    switch($type) {
        case 'conf':
            $code = 'orange';
        default:
            ;
    }
    return $code . $text . $code;
}
function code($text, $type='Fustuga') {
    return '<pre class=".code">'. $text. '</pre>';
}

$main_html = '
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Kamronbek Quchqorov">';
$main_body = '</head><body>';
$cls_html = '</body></html>';
$contact = '';

?>

<style>
    body {
        color: #fff;
        background-color: #2b2b2b;
        margin: 0;
        padding: 0;
    }
    pre {
        color: lime;
        text-align: left;
        border: 1px solid #fff;
        margin: 10px;
        padding: 7px;
        border-radius: 12px;
        box-shadow: 5px 5px 2px #fff;
    }
    pre:hover {
        background-color: #000;
    }
    h1 {
        text-align: center;
    }
</style>