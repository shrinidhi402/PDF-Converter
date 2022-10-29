<?php

 $targetfolder = "pdfcopy/";

 $targetfolder = $targetfolder . basename( $_FILES['file']['name']) ;

if(move_uploaded_file($_FILES['file']['tmp_name'], $targetfolder))

 {

 echo "Your file ". basename( $_FILES['file']['name']). " is converted. click the below button to download";

 }

 else {

 echo "Problem uploading file";

 }
$x = 'python C:\xampp\htdocs\PROJECT\pdftoexcel.py -i '.$_FILES['file']['name'];
// echo $x;
 $command = escapeshellcmd($x);
 $output = shell_exec($command);
//  echo $output;
//  $f = fopen("file.csv", "w");
// fwrite($f, $output);
// fclose($f);
 ?>


 <!DOCTYPE html>
 <html lang="en">
 <head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>download page</title>
     <style>
         .download{
             text-align:center;
            
             background-color: white;
             text-decoration: none;
             color: blue;
             font-size: 30px;
         }
         .Back{
        background-color:rgb(97, 187, 247);
        border-radius: 10px;
        padding: 15px;
        text-decoration: none;
    color: white;
    font-size: 16px;
    border: none;
    cursor: pointer;
  }
  .align-center{
            display: flex;
          position: relative;
          
        }
     </style>
 </head>
 <body>
 <a  class ="Back" href="homepage.html">Back</a>
     <br>
     <div class="align-center">
     <a class="download" href="demo7.csv" download="marks.csv"> download file</a>
     </div>
   
<br>

 </body>
 </html>