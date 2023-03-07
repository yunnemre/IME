<?php
#Aler değeri oluşturulur
$alert="";
session_start();
#url içindeki user kısmı çekilir ve depolanır
if(isset($_GET["user"])) {
    $username = $_GET["user"];
    $_SESSION['username']= $username;
    #Database bağlantısı yapılır ve yolanan username email alınır
    $mysqli = new mysqli("127.0.0.1", "root", "", "webadminoruser");
    if ($mysqli->connect_errno) {
        echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
    }

    $info = $mysqli->query("SELECT email FROM kytblgileri WHERE kullaniciadi='$username' ");
    $cntrl2 = mysqli_fetch_assoc($info);
    $inf=$cntrl2["email"];
    #Destek ksımında içierikleri post edilip database eklenir
    if($_POST){
        $baslik= $_POST['baslik'];
        $destektext=$_POST['destektxt'];

        $mysql = new mysqli("127.0.0.1", "root", "", "web");
        if ($mysql->connect_errno) {
            echo "Failed to connect to MySQL: (" . $mysql->connect_errno . ") " . $mysql->connect_error;
        }

        $sorgu = $mysql->query("INSERT INTO support (email, baslik, icerik) VALUES ('$inf', '$baslik', '$destektext') ");


    }
}
?>
<!doctype html>

<html lang="tr" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <title>Destek Al</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">

</head>
<style>
    body{
        background-color:white;
    }
    .head{
        position:fixed;
        height:50px;
        width:220px;
        border:2px solid;
        border-color:transparent transparent black transparent;
        color:black;
        text-align:center;
        padding:10px;
        padding-left:30px;
        font-size:20px;

    }
    .icon{
        position: fixed;
        width: 30px;
        height:30px;
        top:7px;
        left:15px;
        background-image: url('/../login/icons/tarayicilogo4.png');
        background-position:center;
        border-color:red;
        background-repeat: no-repeat;
        background-attachment: inherit;
        background-size: 30px;
        background-color: transparent;
    }

    .menu{

        position: fixed;
        top:55px;

        width:250px;
        height: 1050px;
    }
    .menua{
        color: black;
        border: 1px solid transparent;
        border-top-right-radius:10px;
        border-bottom-right-radius:10px ;
        width: 220px;
        height: 50px;
        font-size: large;
        padding: 10px;

    }
    .menua:hover{
        background-color: #fccb90;
        color:black;
        border-color: #fccb90;

    }
    .menua:link, a:visited {
        color: #444444;
        text-decoration: none;
        cursor: auto;

    }

    .menua:link:active, a:visited:active {
        color: black;


    }
    a{
        text-decoration: none;
        width: 220px;
        height: 50px;
    }



</style>

<body>
<!--İcon ve heap yönetimi yazısı kısmı-->
<div style="background-color: #eee">
    <a href="index.php">
        <div class="head fw-bold " >Hesap Yönetimi
            <div class="icon"></div>

        </div>
    </a>
    <!--Menu eklenmesi-->

    <div class="menu" style="float: left" >

        <a class="" href="http://localhost:63342/htdocs/index/index.php?user=<?php echo $_SESSION['username'] ?>"   >
            <div class="menua" style=""> Hesap Bilgileri</div>
        </a>



        <a href="http://localhost/history/data.php" >
            <div class="menua" >Geçmiş</div>
        </a>



        <a href="http://localhost/download/download.php">
            <div class="menua" >İndirilenler</div>
        </a>



        <a href="http://localhost/index/support.php">
            <div class="menua" style="background-color: #fccb90;">Destek al</div>
        </a>



    </div>
</div>
<!--Destek içerikleirin eklenmesi-->

<div id="hesapbilgileri" style="position:absolute;left:230px;width: auto;height: auto;border: 2px solid #fccb90;border-top-right-radius: 15px;border-top-left-radius: 15px;">
    <div class="mt-1" style="height: 100px;width: 900px;padding-left: 200px;">
        <h4 class="text-muted text-center pt-5 fw-bolder" style="padding-right: 100px;border: 1px solid;border-color: transparent transparent black transparent;">Hesap Bilgileri</h4>
    </div>

    <form id="destekgnder" action="" method="post">
        <p style="padding-left: 50px;">Konu:</p>
        <p id="alert" style="color:red;"> <?php echo $alert?></p>

        <div class="form-outline mb-4" style="padding-left: 150px;padding-right: 50px;">
            <input type="text" id="form223" class="form-control"
                                                placeholder="Başlık" name="baslik"/>
        </div>

        <p style="padding-left: 50px;">İçerik:</p>

        <div class="form-outline mb-4 " style="padding-left: 150px;padding-right: 50px;" >
            <textarea style="width:800px;height: 300px;" id="destektext" class="form-control" name="destektxt"></textarea>
        </div>

        <div class="text-center pt-1 mb-5 pb-1 ps-4">
            <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="Submit" name="gnder"  form="destekgnder">Gönder</button>
        </div>

    </form>



</div>




<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
