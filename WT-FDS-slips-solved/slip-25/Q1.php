<?php
    $fname = $_POST['fname'];
    $op = $_POST['op'];
    switch($op){
        case 1:
            echo "<br>Type of file : ".filetype("$fname");
            break;
        case 2:
            echo "<br>Last Access Time: ".date("d M Y,h:m:s",fileatime("$fname"));
            break;
        case 3:
            echo "<br>Size of file : ".filesize("$fname");
            break;
        case 4:
            unlink("$fname");
    }
?>