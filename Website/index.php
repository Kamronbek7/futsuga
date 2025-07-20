<?php

require('includes/menu.php');
require('includes/main.php');

echo $main_html . title('Home');

?>

<?php echo $main_body;
echo code('init:
    TOKEN=env');
?>
<?= $cls_html ?>
