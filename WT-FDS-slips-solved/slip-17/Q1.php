<?php
    $a=array("Sagar"=>31,"Vicky"=>41,"Leena"=>39,"Ramesh"=>40);
    echo "original array is :<br> ";
    print_r($a);

    echo "<br>ascending order sort by value<br>";
    asort($a);
    print_r($a);

    echo "<br>ascending order sort by Key<br>";
    ksort($a);
    print_r($a);

    echo "<br>descending order sorting by Value<br>";
    arsort($a);
    print_r($a);
    
    echo "<br>descending order sorting by key<br>";
    krsort($a);
    print_r($a);
 
?>