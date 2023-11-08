<?php
        // Get input values from the form
        $number1 = $_POST["number1"];
        $number2 = $_POST["number2"];
        // Function to find the modulus
        function findModulus($a, $b) {
            return $a % $b;
        }
        // Function to find the power
        function findPower($a, $b) {
            return pow($a, $b);
        }
        // Function to find the sum of first n numbers
        function findSum($n) {
            return ($n * ($n + 1)) / 2;
        }
        // Function to find the factorial
        function findFactorial($n) {
            if ($n === 0) {
                return 1;
            } else {
                return $n * findFactorial($n - 1);
            }
        }
        // Calculate and display results
        echo "Modulus of $number1 and $number2 is " . findModulus($number1, $number2) . "<br>";
        echo "Power of $number1 raised to $number2 is " . findPower($number1, $number2) . "<br>";
        echo "Sum of first $number1 numbers is " . findSum($number1) . "<br>";
        echo "Factorial of $number2 is " . findFactorial($number2) . "<br>";
    ?>