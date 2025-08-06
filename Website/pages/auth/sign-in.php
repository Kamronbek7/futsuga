<?php
// header('Content-Type: applicatin/json;charset=utf-8');
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // echo '<script>alert("post");</script>';
    echo json_encode($_REQUEST, true);
}
?>