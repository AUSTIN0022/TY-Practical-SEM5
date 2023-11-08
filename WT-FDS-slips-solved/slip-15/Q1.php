<?php
    $string = $_POST["string"];
    $operation = $_POST["op"];
    // Display the result based on the selected operation
    switch ($operation) {
        case '1':
            echo "First Five words: " . FiveWords($string) . "<br>";
            break;
        case '2':
            echo "String in lowercase: " . strtolower($string) . "<br>";
            break;
        case '3':
            echo "String in Title Case: " . ucwords(strtolower($string)) . "<br>";
            break;
        case '4':
            echo "Padded String: " . str_pad($string,30,"*",STR_PAD_BOTH) . "<br>";
            break;
        case '5':
            echo "String with leading whitespaces removed: " . ltrim($string) . "<br>";
            break;
        case '6':
            echo "Reverse of the string: " . strrev($string) . "<br>";
            break;
        default:
            echo "Invalid operation selected.";
    }
    function FiveWords($str) {

        $words = str_word_count($str,1);
        $FirstFive = array_slice($words,0,5);
        $result = implode('',$FirstFive);
        return $result;

    }
?>
    