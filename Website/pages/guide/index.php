<?php

require('../../includes/menu.php');
require('../../includes/main.php');
require('data.php');

echo $main_html . title('Guide');

?>

<?php echo $main_body;

echo '<ol>';
foreach($themes as $theme) {
    echo '<h1><li>' . $theme . '</li></h1>' . '<hr>';
} echo '</ol>';

echo $cls_html;

?>