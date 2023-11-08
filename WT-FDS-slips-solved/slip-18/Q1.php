<!DOCTYPE html>
<html>
<head>
	<title>Associative Array Operations</title>
</head>
<body>
	<h1>Associative Array Operations</h1>
	<form method="post">
		Choose an operation:
		<select name="choice">
            <option></option>
			<option value="reverse">Reverse the order of key-value</option>
			<option value="traverse">Traverse in random order</option>
			<option value="convert">Convert into individual variables</option>
			<option value="display">Display array along with key</option>
		</select>
		<input type="submit" value="Submit">
	</form>
	<?php
		// Initialize the associative array
		$arr = array("apple" => 2,"banana" => 4,"cherry" => 6,"date" => 8,"berry" => 10);

		// Perform the selected operation
			$choice = $_POST['choice'];
			switch ($choice) {
			    case 'reverse':
                        $reverse_arr = array();
                        foreach ($arr as $key => $value) {
                            $reverse_arr[$value] = $key;
                        }
                        print_r($reverse_arr);
			        break;
			    case 'traverse':
                        $keys = array_keys($arr);
                        shuffle($keys);
                        foreach ($keys as $key) {
                            echo "$key: " . $arr[$key] . "<br>";
                        }
			        break;
			    case 'convert':
                        extract($arr);
                        echo "apple: $apple<br>";
                        echo "banana: $banana<br>";
                        echo "cherry: $cherry<br>";
                        echo "date: $date<br>";
                        echo "berry: $berry<br>";
			        break;
			    case 'display':
                        foreach ($arr as $key => $value) {
                            echo "$key: $value<br>";
                        }
			        break;
			    default:
			            echo "Invalid choice<br>";
			        break;
			}
	?>
</body>
</html>