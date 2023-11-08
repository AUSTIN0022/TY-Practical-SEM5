<?php
    $ch=$_POST['t1'];
    $a=array(10,20,1,2,3,4,5,6);
    switch($ch)
    {
        case 1:echo"<br>ORIGINAL STACK IS :";
                foreach($a as $v) {
                    echo"$v\t";
                }
                array_push($a,'7','66');
                echo"<br>After inserting an element stack is :";
                foreach($a as $v) {
                    echo"$v\t";
                }
            break;
        case 2:echo"<br>ORIGINAL STACK IS :";
                foreach($a as $v) {
                    echo"$v\t";
                }
                $e=array_pop($a);
                echo"<br>After deleting an element stack is :";
                foreach($a as $v) {
                    echo"$v\t";
                }
            break;
        case 3:echo"<br>ORIGINAL STACK IS :";
                foreach($a as $v) {
                    echo"$v\t";
                }
            break;
        default :echo"Invalid choice";
    }
?>