<?php
#Email yolamak için gerekli classlar eklenir
require 'Exception.php';
require 'PHPMailer.php';
require 'SMTP.php';

use PHPMailer\PHPMailer\PHPMailer;
$uyari="";
#Kayıt sornsı buraya $_Session['kod'] 6 haneli bir random kod olusturur o kod mail içinerisine eklenir ve dögü durdurulur
session_start();
    if($_SESSION['say']==0){
        $_SESSION['kod']=mb_strtoupper(bin2hex(random_bytes(3)));
        $_SESSION['say']++;
    }

    if($_SESSION['say']==1){
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
        $mail->addAddress($_SESSION['emailt'], 'ynns1002@gmail.comdeneme');
        $mail->Subject = 'Eposta doğrulama';
        $mail->isHTML(true);
        $saas=$_SESSION['kod'];
        $mail->Body ="
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

        <table style='FONT-SIZE:18px;padding-right:20px;padding-left:20px;width:672px;margin-left:14px;' id='m_8' cellspacing='0' cellpadding='0' bgcolor='#FFFFFF'>
            <tbody><tr>
                <td colspan='5' width='600' height='10'></td>
            </tr>
            <tr>
                <td colspan='5' width='600' height='15'><span><p style='text-align: center;'> Doğrulama Kodunuz </p></span></td>
            </tr>

            <tr bgcolor='#dbdbdb'>
            <tr bgcolor='#dbdbdb'>
                <td width='25' height='75' style='border-top-left-radius:10px;border-bottom-left-radius:10px;'>
                    <center>
                        <b style='font-size: 30px;'>".$_SESSION['kod']."</b>
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
        if($mail_gonder){
            echo "";
        }else{
            echo 'Mail gönderilemedi. Mail hata mesajı: '.$mail->ErrorInfo;

        }
        $_SESSION['hash']=bin2hex(random_bytes(8));

        $_SESSION['say']++;
    }



?>
<?php

#Kodu girdikten sonra doğru ise kod session ile buraya getirilimis bilgiler kaydedilir
if ($_GET) {
    if($_GET['kods']== $_SESSION['kod']){
        $mysqli = new mysqli("127.0.0.1", "root", "", "webadminoruser");
        if ($mysqli->connect_errno) {
            echo "Bağlantı başarısız: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
        }

        $mysqli->set_charset("utf8");
        $nickname=$_SESSION['nickname'];
        $email=$_SESSION['emailt'];
        $pass=$_SESSION['passw'];
        $hash=$_SESSION['hash'];
        $sorgu = $mysqli->query("INSERT INTO kytblgileri (kullaniciadi, email, password,hash) VALUES ('$nickname', '$email', '$pass','$hash') ");
        $cntrl = mysqli_fetch_assoc($sorgu);
        header("location:login.php");


    }else{
        $uyari="Yanlış girdiniz";

    }
}
?>
<!doctype html>
<html lang="tr">
<head>
    <meta charset="utf-8">
    <title>Eposta Doğrulama Sistemi</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<style>
    .gradient-custom-2 {

        background: #fccb90;


        background: -webkit-linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);


        background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
    }


    @media (min-width: 768px) {
        .gradient-form {
            height: 100vh !important;
        }
    }
    @media (min-width: 769px) {
        .gradient-custom-2 {
            border-top-right-radius: .3rem;
            border-bottom-right-radius: .3rem;
        }
    }
    #corner1 {
        border-top-left-radius: 100px;
        border-top-right-radius: 10px;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 100px;
    }
</style>
<body>
<!--Mail kod girilcek alanın oluşturulamsı-->
<section class="h-100 gradient-form d-flex align-items-center " style="background-color: #eee;">
    <div class="container py-5 h-100 " >
        <div class="row d-flex justify-content-center align-items-baseline pt-5  h-75">
            <div class="col-lg-5 ">
                <div class="card  text-black border-top-3 " id="corner1">


                        <div class="col-lg-5 " style="width: auto;" >
                            <div class="card-body p-md-5 mx-md-4 " >

                                <div class="d-flex justify-content-center align-items-top">
                                    <img src="icons/tarayicilogo4.png"
                                         style="width: 55px; height: 55px;padding-right: 5px; " alt="logo" >
                                    <h4 class="mt-3 mb-4 pb-4 ms-1 " style="width: auto;">E-Posta Doğrulama</h4>
                                </div>

                                <form  id="sc" action="" method="get">
                                    <p class="pt-2 mt-1 ms-1">E-Postanızı kontrol edin</p>
                                    <p class="pt-2 mt-1 ms-1" style="color: red;"><?php echo $uyari ?></p>

                                    <div class="form-outline mb-2">
                                        <label for="form2Example11"></label>
                                        <input type="text" id="form2Example11" name="kods" class="form-control form-control-lg text-center " pattern="{6}" required="required" maxlength="6" autocomplete="off"
                                                                                   placeholder="E-mail'e gelen 6 haneli kodu giriniz"  />

                                    </div>


                                    <div class="text-center pt-3 mb-3 pb-1">
                                        <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-1" type="submit" form="sc">Doğrula</button>

                                    </div>

                                    <div class="d-flex align-items-center justify-content-center pb-2 pt-3">
                                        <p class="mb-0 me-2">Kod gelmedi mi?</p>
                                        <button type="button" class="btn btn-outline-danger">Tekrar gönder</button>
                                    </div>

                                </form>

                            </div>
                        </div>


                </div>
            </div>
        </div>
    </div>
</section>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
