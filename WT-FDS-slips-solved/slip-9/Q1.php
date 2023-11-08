<!DOCTYPE html>
<html>
<head>
	<title>String Operations</title>
</head>
<body>
	<form method="post">
		Enter a string:
		<input type="text" name="string">
		<br><br>
		Select a separator:
		<select name="separator">
			<option value="#">#</option>
			<option value="|">|</option>
			<option value="%">%</option>
			<option value="@">@</option>
			<option value="!">!</option>
			<option value=",">,</option>
		</select>
		<br><br>
		<input type="submit" name="submit" value="Submit">
	</form>
	<br>
	<?php
		$string = $_POST['string'];
		$separator = $_POST['separator'];
		$words = explode(',', $string);
		echo "<b>Words in the string:</b><br>";
		foreach ($words as $word) {
			echo "- $word<br>";
		}
		$new_separator = str_replace(',', $separator, $string);
		echo "<br><b>New string with replaced separator:</b><br>";
		echo "- $new_separator<br>";
		
		$lws=strrpos($string,',')+1;
		$last=substr($string,$lws);
 		
		echo "<br><b>Last word in the string:</b><br>";
		echo "- $last<br>";
	?>
</body>
</html>