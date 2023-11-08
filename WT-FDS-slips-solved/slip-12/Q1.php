<?php
    function calculate($num1, $num2, $operation = '+') {
        switch ($operation) {
            case '+':
                return $num1 + $num2;
            case '-':
                return $num1 - $num2;
            case '*':
                return $num1 * $num2;
            case '/':
                if ($num2 != 0) {
                    return $num1 / $num2;
                } else {
                    return "Division by zero is not allowed.";
                }
            default:
                return "Invalid operation";
        }
    }


    $num1 = $_POST['num1'];
    $num2 = $_POST['num2'];
    $operation = $_POST['op'];
    $result = calculate($num1, $num2, $operation);
    echo "Result: $result";
?>
    
