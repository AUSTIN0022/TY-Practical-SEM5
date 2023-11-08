<!DOCTYPE html>
<html>
<head>
    <style>
        table {
            border-collapse: collapse;
        }
        td {
            width: 50px;
            height: 50px;
            text-align: center;
        }
        .white {
            background-color: white;
        }
        .black {
            background-color: black;
        }
    </style>
</head>
<body>
    <h1>Chessboard</h1>
    <table>
        <?php
        $rows = 8;
        $columns = 8;

        for ($row = 1; $row <= $rows; $row++) {
            echo "<tr>";
            for ($col = 1; $col <= $columns; $col++) {
                $class = ($row + $col) % 2 == 0 ? 'white' : 'black';
                echo "<td class='$class'></td>";
            }
            echo "</tr>";
        }
        ?>
    </table>
</body>
</html>
