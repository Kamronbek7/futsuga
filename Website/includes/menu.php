<?php
$menu_height = '30px';
?>

<style>
    body {
        margin: 0;
        padding: 0;
    }
    .menu {
        background-color: #1b1b1b;
        width: 100%;
        /* border-radius: 20px; */
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
        background-color: #1b1b1b;
    }
    .menu a:hover {
        background: linear-gradient(to right, blue, red);
    }
</style>

<nav class="menu">
  <a href="/">🏠 Home</a>
  <a href="/builder.php">🔧 Builder</a>
  <a href="/guide.php">📘 Guide</a>
  <a href="/examples.php">📂 Examples</a>
  <a href="/download.php">⬇️ Download</a>
  <a href="/faq.php">❓ FAQ</a>
</nav>