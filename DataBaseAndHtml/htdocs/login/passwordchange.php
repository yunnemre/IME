<?php
#Mail göndermek için gerekli dosyalar ekleniyor
require 'Exception.php';
require 'PHPMailer.php';
require 'SMTP.php';

use PHPMailer\PHPMailer\PHPMailer;
$uyari="";
$ginf="";
session_start();
#Tek bir defa mail atsın diye döngü içinde artılacak değerler oluşturuluyor
$_SESSION['ct']=0;
$_SESSION['esend']=0;
if ($_SESSION['esend']==0)
    #Post edilen mail adresi yada kullnaıcı adı kontrol edilir ve ait oldugu  mail döngüsüne sokulur
    if ($_POST) {
    $_SESSION['nckormail'] = $_POST['nckormail'];


    $mysqli = new mysqli("127.0.0.1", "root", "", "webadminoruser");
    if ($mysqli->connect_errno) {
        $uyari= "Bağlantı Hatası: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
    }

    $mysqli->set_charset("utf8");
    $nickname = $_SESSION['nckormail'];
    $email = $_SESSION['nckormail'];
    $sorgu = $mysqli->query("SELECT Count(*) FROM kytblgileri WHERE kullaniciadi='$nickname' ");
    $cntrl = mysqli_fetch_assoc($sorgu);
    $count = $cntrl["Count(*)"];
    $sorgu2 = $mysqli->query("SELECT Count(*) FROM kytblgileri WHERE email='$email ' ");
    $cntrl2 = mysqli_fetch_assoc($sorgu2);
    $count2 = $cntrl2["Count(*)"];
    if ($count == 1) {
        $ec = $mysqli->query("SELECT email,hash FROM kytblgileri WHERE kullaniciadi='$nickname' ");
        $ecs = mysqli_fetch_assoc($ec);
        $ecst = $ecs["email"];

        $ecsh = $ecs["hash"];


        if ($_SESSION['ct'] == 0) {
            #Mail yollamak için oluşturulur mailin içine eklenne mctas urlsine ait özel link tıklananrak sifre değiştirme kısmına gidilir
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
            $mail->addAddress($ecst, 'SS');
            $mail->Subject = 'Parolanı Mı Unuttun';
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
                <td width='25' height='75' style='border-top-left-radius:10px;border-bottom-left-radius:10px;'>
                    <center>
                        <b href='http://localhost/login/mctas.php?yenile=$ecsh' style='font-size: 10px;'>http://localhost/login/mctas.php?yenile=$ecsh</b>
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
                $ginf = "Eposta Başarılı bir şekilde Gönderildi. Epostanızı kontrol ediniz";
            } else {
                echo 'Mail gönderilemedi. Mail hata mesajı: ' . $mail->ErrorInfo;

            }

            $_SESSION['ct']++;
            $_SESSION['esend']++;
        }

    } else if ($count2 == 1) {

        $ec2 = $mysqli->query("SELECT hash FROM kytblgileri WHERE email='$email' ");
        $ecs2 = mysqli_fetch_assoc($ec2);
        $ecsh2 = $ecs2["hash"];

        #Mail yollamak için oluşturulur mailin içine eklenne mctas urlsine ait özel link tıklananrak sifre değiştirme kısmına gidilir
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
            $mail->addAddress($email, 'SS');
            $mail->Subject = 'Parolanı Mı Unuttun';
            $mail->isHTML(true);
            $mail->Body = "
<head>
    <meta charset='UTF-8'>
    <title>Title</title>
    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3' crossorigin='anonymous'>
</head>
<body>
<img src='icons/tarayicilogo4.png' class='' style='width:150px;position:relative;left:290px;top:30px;padding-bottom:30px;'  >
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
                <td width='25' height='75' style='border-top-left-radius:10px;border-bottom-left-radius:10px;'>
                    <center>
                        <b href='http://localhost/login/mctas.php?yenile=$ecsh2' style='font-size: 10px;'>http://localhost/login/mctas.php?yenile=$ecsh2</b>
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
                $ginf = "Eposta Başarılı bir şekilde Gönderildi. Epostanızı kontrol ediniz";
            } else {
                $uyari= 'Mail gönderilemedi. Mail hata mesajı: ' . $mail->ErrorInfo;

            }

            $_SESSION['ct']++;
            $_SESSION['esend']++;
        }
    }else {

        $uyari = "Geçersiz Kullanıcıadı veya Eposta";

    }
}


?>
<!doctype html>
<html lang="tr">
<head>
    <meta charset="utf-8">
    <title>Şifre mi Unuttum</title>
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
<!--Şifremi unuttum tasarımı -->
<section class="h-100 gradient-form d-flex align-items-center " style="background-color: #eee;">
    <div class="container py-5 h-100 " >
        <div class="row d-flex justify-content-center align-items-baseline pt-5  h-75">
            <div class="col-lg-5 ">
                <div class="card  text-black border-top-3 " id="corner1">


                    <div class="col-lg-5 " style="width: auto;" >
                        <div class="card-body p-md-5 mx-md-4 " >

                            <div class="d-flex justify-content-center align-items-top">
                                <img src="icons/tarayicilogo4.png"
                                     style="width: 55px; height: 55px; "  alt="logo">
                                <h4 class="mt-3 mb-4 pb-1 ms-0 " style="width: auto;text-align:center;">Giriş Yaparken Sorun mu Yaşıyorsun?</h4>

                            </div>

                            <form  id="pswy" action="" method="post">
                                <p class="pt-1 mt-1 ms-1 text-muted">E-posta adresini veya kullanıcı adını gir ve hesabına yeniden girebilmen için sana bir bağlantı gönderelim.</p>
                                <p class="pt-2 mt-1 ms-1" style="color: red;"><?php echo $uyari ?></p>
                                <p class="" style="color: green;"><?php echo $ginf ?></p>

                                <div class="form-outline mb-2">
                                    <label for="form2Example11"></label>
                                    <input type="text" id="form2Example11" name="nckormail" class="form-control form-control-lg text-center " required="required" autocomplete="off"
                                                                               placeholder="Eposta veya Kullanıcı adınızı giriniz"  />


                                </div>




                                <div class="text-center pt-3 mb-3 pb-1">
                                    <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-1" type="submit" form="pswy">Giriş Bağlantsı Gönder</button>

                                </div>

                                <div class="d-flex align-items-center justify-content-center pb-2 pt-3">
                                    <p class="mb-0 me-2">Ya da Hesap Oluştur </p>
                                    <a href="reg.php" type="button" class="btn btn-outline-danger">Kayıt Ol</a>
                                </div>

                            </form>

                        </div>
                    </div>


                </div>
            </div>
        </div>
    </div>
</section>
<script>

</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
