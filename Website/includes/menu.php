<?php
$menu_height = '30px';

$h1_hover_color1 = 'blue';
$h1_hover_color2 = 'purple';

$h1_color1 = '#000055';
$h1_color2 = 'blue';
?>

<style>
    .menu {
        /* background-color: #1b1b1b; */
        background: linear-gradient(to right, <?= $h1_color1 . ',' . $h1_color2 ?>);
        width: 100%;
        height: <?= $menu_height ?>;
    }
    .menu a {
        color: white;
        text-decoration: none;
        text-align: center;
        width: 16.65%;
        float: left;
        height: <?= $menu_height ?>;
        border: 0px none;
        /* background-color: #1b1b1b; */
        background: linear-gradient(to right, <?= $h1_color1 . ',' . $h1_color2 ?>);
    }
    .menu a:hover {
        background: linear-gradient(to right, <?= $h1_hover_color1 ?>, <?= $h1_hover_color2 ?>);
    }
    a.r:hover {
        background: linear-gradient(to left, <?= $h1_hover_color1 ?>, <?= $h1_hover_color2 ?>);
    }
</style>

<nav class="menu">
  <a href="/">🏠 Home</a>
  <a href="/pages/builder.php" class="r">🔧 Builder</a>
  <a href="/pages/guide.php">📘 Guide</a>
  <a href="/pages/examples.php" class="r">📂 Examples</a>
  <a href="/pages/download.php">⬇️ Download</a>
  <a href="/pages/faq.php" class="r">❓ FAQ</a>
</nav>