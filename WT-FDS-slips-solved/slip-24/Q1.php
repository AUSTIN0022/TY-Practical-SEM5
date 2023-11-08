<html>
    <body>
        <form  method="POST">
            Enter 1st file name
            <input type="text" name=txt1><br>
            Enter 2nd file name
            <input type="text" name=txt2><br>
            <input type="submit" value="ok">
        </form>
        
        <?php
            $f1=$_POST['txt1'];
            $f2=$_POST['txt2'];
            $file1=fopen($f1,"r")or die("cant open file");
            $file2=fopen($f2,"w")or exit("cant open file");
            while(!feof($file1)){
                $data=fread($file1,filesize($f1));
                fwrite($file2,$data);
            }
            echo "file copied";
            fclose($file1);
            fclose($file2);
        ?>
  </body>
</html>
