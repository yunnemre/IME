<?php
#Geçmiş sayfasınndan post edilen silinmesi gereken kutuları geçmiş datamabseinbdne siler
#Ve tekrar data php sayfasına yönlendirir
$mysqli = new mysqli("127.0.0.1", "root", "", "web");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

$mysqli->set_charset("utf8");

if(isset($_POST["ossm"])){
  $hobi = $_POST['ossm'];

  foreach($hobi as $h){

      echo $h;
      $sorgu = $mysqli->query("DELETE FROM history WHERE Id=$h");


  }
}
else{
    echo("");

}
header("location:http://localhost:63342/htdocs/history/data.php");
      die();
?>