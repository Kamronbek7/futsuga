<?php

require('../includes/menu.php');
require('../includes/main.php');

$platforms = [
    "Windows", "Linux", "Mac OS", "Source code"
];

echo $main_html . title('Home');?>
<style>
    .block {
        width: 25%;
        float: left;
    }
</style>
<?php
echo $main_body;

foreach($platforms as $pltf) {
    echo '<h1>' . $pltf . '</h1>' . '<hr>';
}

echo $cls_html;

?>