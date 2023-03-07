<?php
#Kullanıcı girişine yönlendirildiği zaman bu sayfaya bağlanıyor yönlendirilirken eklnene user çağrılır vebilgi eklenir
#İnfo için kullanılacak boş değerler
$ginf="";
$alert="";
session_start();
if(isset($_GET["user"])) {
    #URL içindeki users alır
    $username = $_GET["user"];
    $_SESSION['username']=$username;
    #Veri tabanı bağlanbtısı yapılır
    $mysqli = new mysqli("127.0.0.1", "root", "", "webadminoruser");
    if ($mysqli->connect_errno) {
        echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
    }
    #Giriş yapılan user bilgisini veri tabanından çeker ve bilgileri geçici olarka depolar
    $info = $mysqli->query("SELECT * FROM kytblgileri WHERE kullaniciadi='$username' ");
    $cntrl2 = mysqli_fetch_assoc($info);
    $inf=$cntrl2["email"];
    $infpass=$cntrl2["password"];
    #Şifre veya kullanıcı adı değiştirildiğinde burayay gelerke post eder
    if ($_POST) {
        #gelen kullancıı adı ile sifreyi depolar
        $changeuser= $_POST['klniciadi'];
        $changepass=$_POST['ptxt'];
        #Eper öcneden depolan sifre post edilen şifre ve kullancıı adı ile eşit ise hiçbir şey yapılmaz
        if ($username==$changeuser and $changepass==$infpass){
            $ginf = "";
        #Eğer şifre ve kullanıcı adı ikiside değişik ise update işlemine geçer yeni kullanici adini kullanılıyorm u diye baakr kullanılmıyor ise
            #sifre ve kullanıcı adını değiştirir
        }elseif ($username!=$changeuser and $changepass!=$infpass){

            $sorgu = $mysqli->query("SELECT Count(*) FROM kytblgileri WHERE kullaniciadi='$changeuser' ");
            $cntrl = mysqli_fetch_assoc($sorgu);
            $count = $cntrl["Count(*)"];

            if ($count==0){
                $query = $mysqli->query('UPDATE kytblgileri SET password ="'.$changepass.'", kullaniciadi="'.$changeuser.'" WHERE kullaniciadi ="'.$username.'"');
                header("location:http://localhost:63342/htdocs/index/index.php?user=".$changeuser." ");

            }else{
                $alert="Bu kullanici adi mevcut başka bir tane deneyin";
            }

        #Kullanıcı adı aynı şifre değişik ise yapılacaklar
        }elseif ($username==$changeuser and $changepass!=$infpass){
            $query = $mysqli->query('UPDATE kytblgileri SET password ="'.$changepass.'" WHERE kullaniciadi ="'.$username.'"');
            header("location:http://localhost:63342/htdocs/index/index.php?user=".$username." ");
        #Sadece şifre değişmiş ise yapılacaklar
        }elseif ($username!=$changeuser and $changepass==$infpass){
            $sorgu = $mysqli->query("SELECT Count(*) FROM kytblgileri WHERE kullaniciadi='$changeuser' ");
            $cntrl = mysqli_fetch_assoc($sorgu);
            $count = $cntrl["Count(*)"];

            if ($count==0){
                $query = $mysqli->query('UPDATE kytblgileri SET  kullaniciadi="'.$changeuser.'" WHERE kullaniciadi ="'.$username.'"');
                header("location:http://localhost:63342/htdocs/index/index.php?user=".$changeuser." ");

            }else{
                $alert="Bu kullanici adi mevcut başka bir tane deneyin";
            }
        }

}

}
?>
<!--Sitenin Tasarımı -->
<!doctype html>

<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Hesap</title>
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
<!-- İcon ve hesap yönetimi ytazıısının bulundugu kısım-->
<div style="background-color: #eee">
<a href="index.php">
    <div class="head fw-bold " >Hesap Yönetimi
        <div class="icon"></div>

    </div>
</a>
    <!--Menu kısımın oluşututurulaması -->
<div class="menu" style="float: left" >

        <a class=""    >
            <div class="menua" style="background-color: #fccb90;"> Hesap Bilgileri</div>
        </a>



        <a href="http://localhost/history/data.php" >
            <div class="menua" >Geçmiş</div>
        </a>



        <a href="http://localhost/download/download.php">
            <div class="menua" >İndirilenler</div>
        </a>



        <a href="http://localhost:63342/htdocs/index/support.php?user=<?php echo $_SESSION['username'] ?>">
            <div class="menua" >Destek al</div>
        </a>



</div>
</div>
<!--Hesap kullanıcı biligilerinin ve güncelleme kısımının oluşuturulduğu alan -->
<div id="hesapbilgileri" style="position:absolute;left:230px;width: auto;height: auto;border: 2px solid #fccb90;border-top-right-radius: 15px;border-top-left-radius: 15px;">
    <div class="mt-1" style="height: 100px;width: 900px;padding-left: 200px;">
        <h4 class="text-muted text-center pt-5 fw-bolder" style="padding-right: 100px;border: 1px solid;border-color: transparent transparent black transparent;">Hesap Bilgileri</h4>
    </div>

    <div style="height: 100px;width: 120px;padding-left: 180px;">
        <p  class="text-muted text-center pt-3  fw-bolder" style="float: right;">EPosta:</p>
        <label class="text-muted text-center pt-3 ps-lg-5  fw-normal"><?php echo $inf ?></label>
    </div>

    <div style="height: 100px;width: 120px;padding-left: 180px;">
        <p  class="text-muted text-center pt-3  fw-bolder" style="float: right;">Kullanıcı Adı:</p>
        <label class="text-muted text-center pt-3 ps-lg-5  fw-normal"><?php echo $username ?></label>

    </div>

    <div  class="mb-2" style="height: 100px;width: 120px;padding-left: 180px;">
        <p  class="text-muted text-center pt-3  fw-bolder" style="float: right;">Şifre:</p>
        <label class="text-muted text-center pt-3 ps-lg-5  fw-normal">*************</label>
    </div>

    <p id="alert" class=" text-center " style="color:red;padding-right: 600px;margin-top: 10px;float: right"> <?php echo $alert?></p>
    <p class="" style="color: green;"><?php echo $ginf ?></p>
    <div class="">
        <!--Bilgileri güncelle açılır menu tasarımı -->
    <nav class="navbar" style="width: 200px; ">
        <div class="container-fluid">
            <button class="navbar-toggler  btn-outline-primary " type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="">Bilgileri Güncelle</span>
            </button>

        </div>
    </nav>
        <!--Bilgileri güncelle içeriği -->
    <div class="collapse" id="navbarToggleExternalContent" >
        <div class="bg-white p-4">
            <span class="text-muted" style="color:red;"></span>
            <form id="guncelle" action="" method="post">



                <div class="form-outline mb-4">
                    <label class="form-label" for="form2Example11">Kullanıcı adı</label>
                    <input type="text" id="form2Example11" class="form-control"
                           placeholder="Eposta ya da Kullanıcı adı" name="klniciadi" value="<?php echo $username ?>"/>

                </div>


                <div class="form-outline mb-4 ">
                    <label class="form-label" for="form2Example22" >Şifre</label>
                    <input type="text" id="form2Example22" class="form-control" name="ptxt"  value="<?php echo $infpass ?>"/>

                </div>
                <div class=" pt-1 mb-1 pb-1 ps-4">
                    <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-1" type="Submit" name="gncelle" form="guncelle" >Güncelle</button>
                </div>
            </form>
        </div>
    </div>
    </div>

</div>



<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
