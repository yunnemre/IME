<?php
#Uarı değerin,inb olustuurlamsı ve veribağlantısının kurulması
 $alert="";
$mysqli = new mysqli("127.0.0.1", "root", "", "web");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
?>

<!doctype html>

<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Admin</title>
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
        left:20px;
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


    <?php
        #destek mesajlarının eklenecegi kısmın yuksekliğ-i hesaplanması
       $date=date('Y-m-d');

       $exec = $mysqli->query("SELECT Count(*) FROM support WHERE durum LIKE 'kontrol edilmedi' ");
       $data=mysqli_fetch_assoc($exec);
       $count = $data["Count(*)"];

       $dctheigt= ($count*100)+100;

   ?>
    .mct{


        box-shadow: 0px -1px 2px 2px #444444;
        position: relative;
        width: 1017px;
        height:<?php echo $dctheigt ?>px;
        overflow-y:visible;
        border:1px solid;
        border-top-right-radius:15px;
        border-top-left-radius:15px;
        color:black;
        background-color: #eee;
        border-color: #eee  ;
    }


    .maindiv{
        position: relative;
        width: 1015px;
        height:100px;
        background-color: transparent;
        border:1px solid ;
        border-color: transparent transparent black transparent;
    }

    .mtime{
        position: relative;
        text-align:center;
        width: 150px;
        height:100px;
        top:40px;
        left:25px;
        background-color: transparent;
        color:black;
        text-decoration:none;

    }
    .mtime:hover{
        color:black;
    }
    .mdata:hover{
        color:black;
    }
    .mbaslik:hover{
        color:black;
    }

    .mdata{
        position: relative;
        float: right;
        right: 150px;
        width: 360px;
        height:100px;
        padding-top:30px;

        background-color: transparent;
        text-align:left;
        text-decoration:none;
        color:black;
    }
    .mbaslik{
        position: relative;

        text-align:center;
        width: 250px;
        height:100px;
        top:40px;
        left:80px;



        background-color: transparent;

        text-decoration:none;
        color:black;
    }
    .headertoday{

        position: relative;
        width: 1017px;
        height:80px;


    }


</style>

<body>
<!-- İcon ve admin yazısının eklendiği kısım-->
<div style="background-color: #eee">
<a href="Adminindex.php">
    <div class="head fw-bold " >Admin Page
        <div class="icon"></div>

    </div>
</a>
    <!--Menünün eklendiği kısım -->
<div class="menu" style="float: left" >

        <a class=""  href="http://localhost:63342/htdocs/index/Adminindex.php"   >
            <div class="menua" style="background-color: #fccb90;">Destek Ver</div>
        </a>



        <a href="http://localhost:63342/htdocs/index/kullaniciindex.php" >
            <div class="menua" >Kullanıcı Bilgileri</div>
        </a>



        <a href="http://localhost">
            <div class="menua" >Dosyalar</div>
        </a>



</div>
</div>
<!--Genel div -->
<div id="hesapbilgileri" style="position:absolute;left:230px;top:50px;width: auto;height: auto;border: 2px solid #fccb90;border-top-right-radius: 15px;border-top-left-radius: 15px;">
    <!-- Uyarı tagi-->
<p id="alert" class=" text-center " style="color:red;padding-right: 600px;margin-top: 10px;float: right"> <?php echo $alert?></p>
<div class="">
    <!--Destek kutuucklarının eklendiği kısım -->
    <div class="mct vertical-menu">
        <div class="headertoday fw-bold" style="text-align:left;padding-left:50px;padding-top:12px;border:1px solid;
    border-top-left-radius:15px;
    border-top-right-radius:15px;
    border-color: #eee #eee black  #eee;">Cevaplanmamış Talepler</div>
        <?php

        $sorgu = $mysqli->query("SELECT * FROM support WHERE durum LIKE 'kontrol edilmedi' ORDER BY durum DESC");
        while ($hcek=mysqli_fetch_assoc($sorgu)){
            ?>

            <a href="#" >
                <div class="maindiv">
                    <label for="<?php echo $hcek['Id'] ?>" style="position: absolute;">E-Posta:</label>
                    <a class="mtime"  id="<?php echo $hcek['Id'] ?>" ><?php echo $hcek['email'] ?> </a>
                    <label for="baslik" style="position: absolute;left: 220px;color: #0d6efd;" >Konu:</label>
                    <a class="mbaslik" id="baslik" ><?php echo $hcek['baslik'] ?></a>
                    <label for="icerik" style="position: absolute;left: 480px;color:#0d6efd;" >İçerik:</label>
                    <a class="mdata"  id="icerik"><?php echo $hcek['icerik'] ?></a>
                    <button class="btn btn-outline-primary" id="<?php echo $hcek['Id'] ?>" name="id" style="float: right;position: relative;top: 22px;left: 350px;" onclick="bekle(this.id)">Cevapla </button>

                </div>
            </a>

        <?php }
        ?>
    </div>

</div>
    <!--Desteklerden tıklanmdiği desteğin id(bu id hemde gönderen kişin,iin idsiyle aynıdır) site urlsinin yönlendirilirken eklnenir
     Ve cevaplamam ksımına geçilir-->
    <script>
        function bekle(clicked_id){
            var som=`http://localhost:63342/htdocs/index/supportadminanswer.php?id=${clicked_id}`;
            window.location = som;
        }

    </script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
