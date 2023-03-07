<?php
$username = $_POST['nickname'];
$email=$_POST['emailt'];
$password = $_POST['passw'];
echo $username;
echo "<br />";
echo $email;
echo "<br />";
echo $password;

$mysqli = new mysqli("127.0.0.1", "root", "", "webadminoruser");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

$mysqli->set_charset("utf8");

$sorgu = $mysqli->query("SELECT Count(*) FROM kytblgileri WHERE kullaniciadi='$username' ");
$cntrl=mysqli_fetch_assoc($sorgu);
$count = $cntrl["Count(*)"];
if ($count==1){
    echo"Bu kullanıcı adını girmesisiniz<br>";

    header("location:login.php?_ijt=86vi5bbupeaoklnif3bju7vaad&_ij_reload=RELOAD_ON_SAVE#tab2");

    die();

}
else{
    echo "giris serbest<br>";
}
$sorgu2 = $mysqli->query("SELECT Count(*) FROM kytblgileri WHERE email='$email' ");
$cntrl2=mysqli_fetch_assoc($sorgu2);
$count2 = $cntrl2["Count(*)"];
if ($count2==1){
    echo"Bu kullanıcı emaili giremezsiniz girmesisiniz<br>";

    header("location:login.php?_ijt=86vi5bbupeaoklnif3bju7vaad&_ij_reload=RELOAD_ON_SAVE#tab2");

    die();
}
else{
    echo "giris eserbest<br>";
}


?>