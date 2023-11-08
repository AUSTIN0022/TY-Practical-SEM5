<html>
    <body>
        <form  method="POST" >
            <center>MENU</center>
            1.Insert an element in queue<br>
            2.Delete element from queue<br>
            3.Display the containts of queue<br>
            Enter your choice : 
            <input type="text" name="t1"><br>
            <input type="submit" name="b1">
        </form>
        <?php
            $ch=$_POST['t1'];
            $a=array(10,20,1,2,3,4,5,6);
            switch($ch)
            {
                case 1:echo"<br>ORIGINAL QUEUE IS :";
                        foreach($a as $v) {
                            echo"$v\t";
                        }
                        array_unshift($a,'7');
                        echo"<br>After inserting an element queue is :";
                        foreach($a as $v) {
                            echo"$v\t";
                        }
                    break;
                case 2:echo"<br>ORIGINAL QUEUE IS :";
                        foreach($a as $v) {
                            echo"$v\t";
                        }
                        $e=array_shift($a);
                        echo"<br>Queue after deleting one element : ";
                        foreach($a as $v) {
                            echo"$v\t";
                        }
                    break;
                case 3:echo"<br>ORIGINAL QUEUE IS :";
                        foreach($a as $v) {
                            echo"$v\t";
                        }
                    break;
                default :echo"Invalid choice";
            }
        ?>
    </body>
</html>