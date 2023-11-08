<?php
    $code = $_POST['code'];
    $subject = $_POST['subject'];
    $mks = $_POST['mks'];
    $AllNumbers = explode(":", $code);
    $AllNames = explode(":", $subject);
    $AllMarks = explode(":", $mks);
?>
<table border="1">
    <tr>
        <td>SERIAL NUMBER</td>
        <td>SUBJECT NAME</td>
        <td>SUBJECT MARKS</td> 
    </tr>
    <?php
    $sum = 0; 
    for ($i = 0; $i < count($AllNumbers); $i++) {
        echo "<tr>";
        echo "<td >" . $AllNumbers[$i] . "</td>";
        echo "<td>" . $AllNames[$i] . "</td>";
        echo "<td>" . $AllMarks[$i] . "</td>";
        $sum = $sum + $AllMarks[$i];
        echo "</tr>";
    }
    ?>
    <tr>
        <td colspan=2>TOTAL</td>
        <td><?= $sum ?></td>
    </tr>
    <tr>
        <td colspan="2">PERCENTAGE</td>
        <?php
        $per = $sum / 5;
        ?>
        <td><?= $per ?></td>
    </tr>
    <?php
        if ($per >= 80)
            $grade = 'O';
        else if ($per >= 70 && $per < 80)
            $grade = "A";
        else if ($per >= 60 && $per < 70)
            $grade = "B";
        else if ($per >= 50 && $per < 60)
            $grade = "C";
        else if ($per >= 40 && $per < 50)
            $grade = "PASS";
        else
            $grade = "FAIL";
    ?>
    <tr>
        <td colspan=2>GRADE</td>
        <td><?= $grade ?></td>
    </tr>
</table>