<!DOCTYPE html>
<html>
<head>
    <title>String Operations</title>
</head>
<body>
    <h2>String Operations</h2>
    <form method="post">
        Enter a sentence: <input type="text" name="sentence"><br><br>
        Enter a word: <input type="text" name="word"><br><br>
        Position: <input type="number" name="position"><br><br>
        Number of characters: <input type="number" name="num_chars"><br><br>
        <input type="submit" name="submit" value="Perform Operations">
    </form>

    <?php
        $sentence = $_POST['sentence'];
        $word = $_POST['word'];
        $position = $_POST['position'];
        $numChars = $_POST['num_chars'];

        echo "<h3>Modified Sentence:</h3>";
        // Delete a small part from the first string
        $deletedPart = substr($sentence, $position, $numChars);
        $newSentence = substr_replace($sentence, "", $position, $numChars);
        echo "<p>$newSentence</p>";

        // Insert the given small string into the first string at the specified position
        $newSentence = substr_replace($newSentence, $word, $position, 0);
        echo "<p>$newSentence</p>";

        // Replace some characters/words in the first string at the specified position
        $newSentence = substr_replace($newSentence, $word, $position, strlen($word));
        echo "<p>$newSentence</p>";
    ?>
</body>
</html>
