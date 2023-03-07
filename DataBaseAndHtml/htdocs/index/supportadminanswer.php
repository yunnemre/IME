<?php
#ALERT DEĞERİ OLUŞTUURLAMSI
$alert="";
#Mail atmak için gerekli classların eklenmesi
require '../login/Exception.php';
require '../login/PHPMailer.php';
require '../login/SMTP.php';

use PHPMailer\PHPMailer\PHPMailer;

session_start();
#Tekrar mail atmaması için döngüde artırılacak değer
$_SESSION['ct']=0;
#Urldeki id çekilmesi
if(isset($_GET["id"])) {
    $id = $_GET["id"];
    #Veri tabanı bağlantısı yapılması
    $mysqli = new mysqli("127.0.0.1", "root", "", "web");
    if ($mysqli->connect_errno) {
        echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
    }
    #İd ye göre fprmun içeri çekilmesi
    $info = $mysqli->query("SELECT * FROM support WHERE Id='$id' ");
    $cntrl2 = mysqli_fetch_assoc($info);
    $inf = $cntrl2["Id"];

    #destek cevaplanıp post edilmesi durumunda
    if ($_POST) {
        $answertxt=$_POST['answertxt'];
        #Mail gönderilecek bilgilerin girilmesi ve içeriğin eklenmesi ve yollanması
        if ($_SESSION['ct'] == 0) {
            $mail = new PHPMailer();

            $mail->Host = 'smtp.gmail.com';
            $mail->Username = 'knavesmusic55@gmail.com';
            $mail->Password = 'ssmigfer7844';
            $mail->Port = 465;
            $mail->SMTPSecure = 'ssl';

            $mail->isSMTP();
            $mail->SMTPAuth = true;


            $mail->CharSet = "UTF-8";
            $mail->setLanguage('tr', 'language/');


            $mail->setFrom('knavesmusic55@gmail.com', 'AngryDolphinTeam');
            $mail->addAddress($cntrl2['email'], 'SS');
            $mail->Subject = 'Support';
            $mail->isHTML(true);
            $mail->Body = "
    <head>
        <meta charset='UTF-8'>
        <title>Title</title>
        <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3' crossorigin='anonymous'>
    </head>
    <body>
    <img src='icons/tarayicilogo4.png' class='' style='width:150px;position:relative;left:290px;top:30px;padding-bottom:30px;' alt='logo' >
    <tbody>
    
    <tr>
        <td>
    
            <table style='font-family:Ainslie;FONT-SIZE:18px;padding-right:20px;padding-left:20px;width:672px;margin-left:14px;' id='m_816282346627023878723Table_01' cellspacing='0' cellpadding='0' bgcolor='#FFFFFF'>
                <tbody><tr>
                    <td colspan='5' width='600' height='10'></td>
                </tr>
                <tr>
                    <td colspan='5' width='600' height='15'><span><p style='text-align: center;'> Şifre Değiştirme Linki </p></span></td>
                </tr>
    
                <tr bgcolor='#dbdbdb'>
                <tr bgcolor='#dbdbdb'>
                    <td width='25' height='275' style='border-top-left-radius:10px;border-bottom-left-radius:10px;'>
                        <center>
                            <b style='font-size: 10px;'>$answertxt</b>
                        </center>
                    </td>
    
    
                </tr>
                <tr>
                    <td colspan='5' height='10'></td>
                </tr>
    
                <tr>
                    <td colspan='5' width='600' height='25' style='font-size:25px;text-align: center; font-family: Gabriola'>Saygılarımızla AngryDolphinTeam...</td>
                </tr>
                <tr>
                    <td colspan='5' width='600' height='5'></td>
                </tr>
    
                <tr>
                    <td colspan='5' width='600' height='5'></td>
                </tr>
                </tbody></table>
        </td>
    </tr>
    
    
    </tbody>
    
    <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js' integrity='sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p' crossorigin='anonymous'></script>
    <script src='https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js' integrity='sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB' crossorigin='anonymous'></script>
    <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js' integrity='sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13' crossorigin='anonymous'></script>
    </body>
    </html>
    ";
            $mail_gonder = $mail->send();
            if ($mail_gonder) {
                echo "";
                $query = $mysqli->query('UPDATE support SET durum ="kontrol edildi" where Id="$id"');
                $ginf = "Eposta Başarılı bir şekilde Gönderildi. Epostanızı kontrol ediniz";
            } else {
                echo 'Mail gönderilemedi. Mail hata mesajı: ' . $mail->ErrorInfo;

            }

            $_SESSION['ct']++;
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
        box-shadow: 0px -1px 2px 2px #444444;
        position: relative;
        width: 1317px;
        height:850px;
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
        width: 1315px;
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
        float: left;
        left: 75px;
        width: 1160px;
        height:200px;
        padding-top:30px;
        background-color: transparent;
        text-align:left;
        text-decoration:none;
        color:black;
    }
    .mbaslik{
        position: relative;

        text-align:center;
        width: max-content;
        height:200px;
        top:40px;
        left:80px;
        background-color: transparent;
        text-decoration:none;
        color:black;
    }
    .headertoday{
        position: relative;
        width: 1317px;
        height:80px;
    }

    .manswer{
        position: relative;
        float: left;
        left: 75px;
        width: 960px;
        height:400px;
        padding-top:30px;
    }

</style>

<body>
<!--İcon ve yazı kısmın eklenmesi-->
<div style="background-color: #eee">
    <a href="Adminindex.php">
        <div class="head fw-bold " >Admin Page
            <div class="icon"></div>

        </div>
    </a>
    <!--Menu kısmının eklenmesi-->
    <div class="menu" style="float: left" >

        <a class="" href="http://localhost:63342/htdocs/index/Adminindex.php"   >
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
<!--İçeriğin ve psot edilecek formun eklnemesi-->
<div id="hesapbilgileri" style="position:absolute;left:230px;top:50px;width: auto;height: auto;border: 2px solid #fccb90;border-top-right-radius: 15px;border-top-left-radius: 15px;">

    <p id="alert" class=" text-center " style="color:red;padding-right: 600px;margin-top: 10px;float: right"> <?php echo $alert?></p>
    <div class="">

        <div class="mct vertical-menu">
            <div class="headertoday fw-bold" style="text-align:left;padding-left:50px;padding-top:12px;border:1px solid;
    border-top-left-radius:15px;
    border-top-right-radius:15px;
    border-color: #eee #eee black  #eee;">Destek Cevap <br>
                <p id="alert" style="color:red;"> <?php echo $alert?></p>
            </div>
            <?php

            $sorgu = $mysqli->query("SELECT * FROM support WHERE Id='$id' ");
            $hcek=mysqli_fetch_assoc($sorgu)
                ?>
                <div href="#" >
                    <div class="maindiv">
                        <label for="<?php echo $hcek['Id'] ?>" style="position: absolute;">E-Posta:</label>
                        <a class="mtime"  id="<?php echo $hcek['Id'] ?>" ><?php echo $hcek['email'] ?> </a>
                        <label for="baslik" style="position: absolute;left: 220px;color: #0d6efd;" >Konu:</label>
                        <a class="mbaslik" id="baslik" ><?php echo $hcek['baslik'] ?></a>
                    </div>

                    <div class="" style="width: auto;height: auto;border-bottom: 1px solid black">
                        <label for="icerik" style="position: absolute;left: 10px;top:200px;color:#0d6efd;" >İçerik:</label>
                        <a class="mdata"  id="icerik"><?php echo $hcek['icerik'] ?></a>
                    </div>
                        <form id="answer" method="post">
                            <div class="" style="width: auto;height: auto;">
                                <label for="icerik" style="position: absolute;left: 10px;top:200px;color:#0d6efd;" >İçerik:</label>
                                <textarea  class="manswer"  name="answertxt"></textarea>
                                <button type="submit" form="answer" class="btn btn-success" style="position:relative;top:550px;right: 50px;width: 100px;height: 50px;" id="icerik">Cevapla</button>
                            </div>

                        </form>

                </a>


        </div>

    </div>



    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
