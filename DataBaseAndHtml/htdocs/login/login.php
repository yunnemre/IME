<?php
#Alert değeri giriş kısımında oluşan hata ekranan bilgilendirme vermek için oluşuturlan değer
# eğer şifrte veya parola yanlış girildiğinde döndürülen döngüden değer alır
$alert="";
session_start();
if ($_POST) {
    $_SESSION['klniciadi'] = $_POST['klniciadi'];
    $_SESSION['gptxt'] = $_POST['gptxt'];
    #Sifre ve kullanıcı adı veya mail post alınır

    #Veritabanına bağlantı kurulur
    $mysqli = new mysqli("127.0.0.1", "root", "", "webadminoruser");
    if ($mysqli->connect_errno) {
        echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
    }
    #Sorgu ile eğer count sayısı 1 ise kullanıcıadı doğrudur sonra sifre kontrolune geçilir
    #BUiki türlu yapılır admin girişi mi kullanıcı girişi mi oldugundunu anlamak için count sistemi kullandım
    $adm = $mysqli->query("SELECT Count(*) FROM admingrs WHERE AdminUserName='".$_SESSION['klniciadi']."' ");
    $cntrl3 = mysqli_fetch_assoc($adm);
    $count = $mysqli->query("SELECT Count(*) FROM kytblgileri WHERE kullaniciadi='".$_SESSION['klniciadi']."' OR email='".$_SESSION['klniciadi']."' ");
    $cntrl2 = mysqli_fetch_assoc($count);
    if($cntrl2['Count(*)']==1){
        #Sorguda eger kullanici adi count 1 çıkarsa bu döngüye girip kullanıcı bilgilerini kontrol eder ve sifre kontrolune geçer
        $sorgu = $mysqli->query("SELECT kullaniciadi,password,email FROM kytblgileri WHERE kullaniciadi='".$_SESSION['klniciadi']."' OR email='".$_SESSION['klniciadi']."' ");
        $cntrl = mysqli_fetch_array($sorgu);


        if($_SESSION['gptxt']==$cntrl["password"]){
            $count = $mysqli->query("SELECT kullaniciadi FROM kytblgileri WHERE kullaniciadi='".$_SESSION['klniciadi']."' OR email='".$_SESSION['klniciadi']."' ");
            $sonuc = mysqli_fetch_assoc($count);
            #Yönlendirilirken kullancı adı sayfaya eklenir
            header("location:http://localhost:63342/htdocs/index/index.php?user=".$sonuc['kullaniciadi']."");
            die;

        }else{

            $alert="Kullanici adını veya şifreyi yanlış girdiniz. Tekrar deneyin" ;
        }


    #Eğer admin girişi ise buraya yönlenir ve aynı şekilde şifre doğru ise admin sayfasına yönlendirilir
    }elseif ($cntrl3['Count(*)']==1){
        $sorgu = $mysqli->query("SELECT AdminUserName,password FROM admingrs WHERE AdminUserName='".$_SESSION['klniciadi']."' ");
        $cntrl = mysqli_fetch_array($sorgu);


        if($_SESSION['gptxt']==$cntrl["password"]){
            header("location:/index/Adminindex.php");
            die;
        }else{

            $alert="Kullanici adını veya şifreyi yanlış girdiniz. Tekrar deneyin" ;
        }
    #Herhangi bir döngüye girmediyse alert fonksiyonuna değer verilir ve çıkılır
    }else{
        $alert="Kullanici adını veya şifreyi yanlış girdiniz. Tekrar deneyin" ;
    }





}
?>
<!-- Login(Girş sayfası )Tasarımı-->
<!doctype html>
<html lang="tr">
<head>
    <meta charset="utf-8">
    <title>Giriş Yap </title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<style>
    body{
        overflow: hidden;


    }
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


</style>
<body>
<!--Giriş sablonun tasarlandıgı kısım -->
<div class="tab-content" style="background-color: #eee;">

    <ul class="tab" id="myTab" style="display: none;">
        <li class="activetab"><a href="" id="yunnn">Ana Sayfa</a></li>

    </ul>

    <div id="tab1" class="tab active tab">
        <section class="h-100 gradient-form" style="background-color: #eee;">
            <div class="container py-5 h-100" >
                <div class="row d-flex justify-content-center align-items-center h-100">
                    <div class="col-xl-10">
                        <div class="card rounded-3 text-black">
                            <div class="row g-0">
                                <div class="col-lg-6">
                                    <div class="card-body p-md-5 mx-md-4">

                                        <div class="text-center">
                                            <img src="icons/tarayicilogo4.png"
                                                 style="width: 120px;" alt="logo">
                                            <h4 class="mt-1 mb-5 pb-1">Biz AngryDolphin Ekibiyiz</h4>
                                        </div>

                                        <form id="formgirisyp" action="" method="post">
                                            <p>Lütfen Hesabınıza giriş yapın</p>
                                            <p id="alert" style="color:red;"> <?php echo $alert?></p>

                                            <div class="form-outline mb-4">
                                                <input type="text" id="form2Example11" class="form-control"
                                                       placeholder="Eposta ya da Kullanıcı adı" name="klniciadi"/>
                                                <label class="form-label" for="form2Example11">Kullanıcı adı</label>
                                            </div>


                                            <div class="form-outline mb-4 ">
                                                <input type="password" id="form2Example22" class="form-control" name="gptxt" />
                                                <label class="form-label" for="form2Example22" >Şifre</label>
                                            </div>

                                            <div class="text-center pt-1 mb-5 pb-1 ps-4">
                                                <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="Submit" name="grssb" >Giriş Yap</button>
                                                <a class="text-muted" href="passwordchange.php">Parolanızı mı unuttunuz?</a>
                                            </div>

                                            <div class="d-flex align-items-center justify-content-center pb-4">
                                                <p class="mb-0 me-2">Hesabın yok mu?</p>
                                                <a href="reg.php" class="btn btn-outline-danger" id="ssyunn"  >Kayıt Ol</a>
                                            </div>

                                        </form>

                                    </div>
                                </div>

                                <div class="col-lg-6 d-flex align-items-center gradient-custom-2">
                                    <div class="text-white px-3 py-4 p-md-4 mx-md-4 ">
                                        <h4 class="mb-4 ">Biz sadece bir şirketten daha fazlasıyız</h4>
                                        <p class="small mb-0">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                                            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                                            exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</html>
