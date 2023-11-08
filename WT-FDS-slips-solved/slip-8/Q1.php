<!DOCTYPE html>
<html>
<head>
    <title>String Operations</title>
</head>
<body>
    <h2>String Operations</h2>
    <form method="post">
        Large String: <input type="text" name="large_string" required><br><br>
        Small String: <input type="text" name="small_string" required><br><br>
        <input type="submit" name="submit" value="Submit">
    </form>

    <?php
        $largeString = strtolower($_POST['large_string']);
        $smallString = strtolower($_POST['small_string']);
        
        if(strpos($largeString, $smallString) === 0) {
            echo "The small string appears at the start of the large string.<br>";
        } else {
            echo "The small string does not appear at the start of the large string.<br>";
        }
        
        $position = strpos($largeString, $smallString);
        if($position !== false) {
            echo "The position of the small string in the large string is: $position<br>";
        } else {
            echo "The small string was not found in the large string.<br>";
        }
        
        $n = 5; // Change this value to number of characters to compare.
        
        if(substr($largeString,0,$n) === substr($smallString,0,$n) ) {
            echo "The first $n characters of both strings are the same";
        } else {
            echo "The first $n characters of both strings are different";
        }
    ?>
</body>
</html>
