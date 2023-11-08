<html>
    <body>
        <form  method="post">
            <h2>Enter choice :</h2>
            <input type="radio" name="ch" value=1> split the array into chunks<br>
            <input type="radio" name="ch" value=2> Sort array by values without changing key <br>
            <input type="radio" name="ch" value=3> Filter Even elements from array <br>
            <br>
            <input type="submit" value="SUBMIT"> <input type="reset" value="CLEAR">
        </form>
        <?php
            function is_even($var)
            {
                if($var%2==0)
                    return $var;
            }
            
            $choice=$_POST['ch'];
            $arr=array('a'=>1,'b'=>2,'c'=>3,'d'=>4,'e'=>5,'f'=>6,'g'=>7,'h'=>8);
            switch($choice)
            {
                case 1: print_r(array_chunk($arr,2));
                    break;
                case 2:
                        asort($arr);
                        echo "Array in ascending order:<br>";
                        print_r($arr);
                        arsort($arr);
                        echo "<br>Array in descending order:<br>";
                        print_r($arr);
                    break;
                case 3:
                        print_r(array_filter($arr,'is_even'));
                    break;
            }
        ?>
    </body>
</html>
