<?php
#alert değerin atanması
$alert="";
#BURAYA YÖNLENDİRİLİRKEN GELEN İD kONTROL EDİLİP DEPOLANIR
if(isset($_GET["id"])) {
    $id = $_GET["id"];
    #database bağlantısı yapılır
    $mysqli = new mysqli("127.0.0.1", "root", "", "webadminoruser");
    if ($mysqli->connect_errno) {
        echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
    }
    #Gelen idye göre kişinin verileri çekilir
    $info = $mysqli->query("SELECT * FROM kytblgileri WHERE Id='$id' ");
    $cntrl2 = mysqli_fetch_assoc($info);
    $inf = $cntrl2["Id"];
    #Şifre vs değiştirip post kontrol kısmı
    if ($_POST) {
        $changeuser = $_POST['nadi'];
        $changepass = $_POST['npass'];
        $changeemail = $_POST['nemail'];
        #Eger hepsi aynıo ise dokunmaz değil ise günceller
        if ($cntrl2['kullaniciadi'] == $changeuser and $changepass == $cntrl2['password'] and $changeemail == $cntrl2['email']) {
            $alert="";

        } else {
            $query = $mysqli->query('UPDATE kytblgileri SET password ="'.$changepass.'", kullaniciadi="'.$changeuser.'",email ="'.$changeemail.'" WHERE Id ="'.$id.'"');

        }
    }
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



    .mct{
        box-shadow: 0 -1px 2px 2px #444444;
        position: relative;
        width: 1017px;
        height:180px;
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
        right: 50px;
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
        float: left;
        left: 525px;
        width: 260px;
        height:100px;
        padding-top:40px;
        background-color: transparent;
        text-align:left;
        text-decoration:none;
        color:black;

    }
    .mbaslik{
        position: relative;
        float: left;
        text-align:center;
        width: max-content;
        height:50px;
        top:40px;
        left:40px;
        background-color: transparent;
        text-decoration:none;
        color:black;
    }
    .headertoday{
        position: relative;
        width: 1017px;
        height:80px;
    }

    .mhash{
        position: relative;
        float: right;

        width: 160px;
        height:100px;
        padding-top:40px;
        background-color: transparent;
        text-align:left;
        text-decoration:none;
        color:black;
    }
    .mhash:hover{
        color:black;
    }

</style>

<body>
<!--icon ve admin yazısının eklendiği kısım-->
<div style="background-color: #eee">
    <a href="Adminindex.php">
        <div class="head fw-bold " >Admin Page
            <div class="icon"></div>

        </div>
    </a>
    <!--Menu kısımın eklendiği yer-->
    <div class="menu" style="float: left" >

        <a class="" href="http://localhost:63342/htdocs/index/Adminindex.php"   >
            <div class="menua" style="">Destek Ver</div>
        </a>



        <a href="http://localhost:63342/htdocs/index/kullaniciindex.php" >
            <div class="menua" style="background-color: #fccb90;" >Kullanıcı Bilgileri</div>
        </a>



        <a href="http://localhost">
            <div class="menua" >Dosyalar</div>
        </a>


    </div>
</div>
<!--Kullanıcı öceki bilgileri ve güncellemke içinb alan eklenir-->
<div id="hesapbilgileri" style="position:absolute;left:230px;top:50px;width: auto;height: auto;border: 2px solid #fccb90;border-top-right-radius: 15px;border-top-left-radius: 15px;">

    <p id="alert" class=" text-center " style="color:red;padding-right: 600px;margin-top: 10px;float: right"> <?php echo $alert?></p>
    <div class="">

        <div class="mct vertical-menu">
            <div class="headertoday fw-bold" style="text-align:left;padding-left:50px;padding-top:12px;border:1px solid;
    border-top-left-radius:15px;
    border-top-right-radius:15px;
    border-color: #eee #eee black  #eee;">Kullanıcı Bilgileri Düzenle <br>
                <p id="alert" style="color:red;"> <?php echo $alert?></p>
            </div>
            <?php

            $sorgu = $mysqli->query("SELECT * FROM kytblgileri where Id='$id' ");
             $hcek2=mysqli_fetch_assoc($sorgu)
                ?>

                <a href="#" >
                    <div class="maindiv">
                        <label for="<?php echo $hcek2['Id'] ?>" style="position: absolute;left: 5px;">E-Posta:</label>
                        <a class="mtime"  id="<?php echo $hcek2['Id'] ?>" ><?php echo $hcek2['email'] ?> </a>
                        <label for="baslik" style="position: absolute;left: 230px;color: #0d6efd;" >Kullanıcı Adı:</label>
                        <a class="mbaslik" id="baslik" ><?php echo $hcek2['kullaniciadi'] ?></a>
                        <label for="icerik" style="position: absolute;left: 530px;color:#0d6efd;" >Şifre</label>
                        <a class="mdata"  id="icerik"><?php echo $hcek2['password'] ?></a>
                        <label for="icerik" style="position: absolute;left: 780px;color:#0d6efd;" >hash</label>
                        <a class="mhash"  id="icerik"><?php echo $hcek2['hash'] ?></a>
                    </div>
                </a>

            </div>

        </div>


    <form id="changeuserinf" action="" method="post">

        <p id="alert" style="color:red;"> <?php echo $alert?></p>

        <div class="form-outline mb-4">
            <input type="text" id="form2Example11" class="form-control"
                    name="nadi" value="<?php echo $hcek2['kullaniciadi'] ?>"/>
            <label class="form-label" for="form2Example11" style="color: #b8bb26"   >Kullanıcı adı</label>
        </div>

        <div class="form-outline mb-4 ">
            <input type="email" id="form2Example22" class="form-control" name="nemail"  value="<?php echo $hcek2['email'] ?>"/>
            <label class="form-label " style="color: #b8bb26" for="form2Example22" >Eposta</label>
        </div>

        <div class="form-outline mb-4 ">
            <input type="text" id="form2Example22" class="form-control" name="npass" value="<?php echo $hcek2['password'] ?>" />
            <label class="form-label" for="form2Example22" style="color: #b8bb26" >Şifre</label>
        </div>

        <button class="btn btn-outline-primary me-1 mb-1" style=" float: right"  type="submit" form="changeuserinf">Değiştir</button>


    </form>

</div>


        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
