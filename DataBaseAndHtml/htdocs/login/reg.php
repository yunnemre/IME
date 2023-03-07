<?php
#hATA DEĞERİ OLUŞTURULUR
$alert="";
session_start();
#Post edilen kayıt bilgileri depolanır
if ($_POST) {
    $_SESSION['nickname'] = $_POST['nickname'];
    $_SESSION['emailt'] = $_POST['emailt'];
    $_SESSION['passw'] = $_POST['passw'];

    #Database bağlantısı kurulur
    $mysqli = new mysqli("127.0.0.1", "root", "", "webadminoruser");
    if ($mysqli->connect_errno) {
        echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
    }
    #Databasede email veya aynı kullanıcıadı var mı diye kontrol edilir eğer var ise ona göre hata mesajı veriri yok ise emailcontol sayfasına yönlendirir
    $mysqli->set_charset("utf8");
    $nickname=$_SESSION['nickname'];
    $email=$_SESSION['emailt'];
    $sorgu = $mysqli->query("SELECT Count(*) FROM kytblgileri WHERE kullaniciadi='$nickname' ");
    $cntrl = mysqli_fetch_assoc($sorgu);
    $count = $cntrl["Count(*)"];
    $sorgu2 = $mysqli->query("SELECT Count(*) FROM kytblgileri WHERE email='$email ' ");
    $cntrl2 = mysqli_fetch_assoc($sorgu2);
    $count2 = $cntrl2["Count(*)"];
    if ($count and $count2== 1) {

        $alert="Bu kullanıcı adı ve Eposta kullanılıyor";

    } else if($count== 1) {

        $alert="Bu Kullanıcı adı kullanılıyor";
    }

    else if ($count2 == 1) {

        $alert="Bu Eposta kullanılıyor";

    } else {
        session_start();
        $_SESSION['say']=0;
        if(isset($_POST['emailt'])){
            $_SESSION['emailt']=$_POST['emailt'];
            header("location:emailcontrol.php");
        }


    }

}
?>
<!doctype html>
<html lang="tr">
<head>
    <meta charset="utf-8">
    <title>Kayıt Ol</title>
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
    .gradient-custom-3 {
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

    @media (min-width: 769px) {
        .gradient-custom-3 {
            border-top-left-radius: .3rem;
            border-bottom-left-radius: .3rem;
        }
    }
</style>
<body>

<!--Kayıt  ol kısmı tasarımı-->
<div id="tab2" class="tab2">
    <section class="h-100 gradient-form" style="background-color: #eee;">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-xl-10">
                    <div class="card rounded-3 text-black ">
                        <div class="row g-0">

                            <div class="col-lg-6 d-flex align-items-center gradient-custom-3 " >

                                <div class="text-white px-3 py-4 p-md-4 mx-md-4">
                                    <h4 class="mb-4 ">Biz sadece bir şirketten daha fazlasıyız</h4>
                                    <p class="small mb-0">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                                        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                                        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                                </div>
                            </div>
                            <div class="col-lg-6" >
                                <div class="card-body p-md-5 mx-md-4 " >

                                    <div class="text-center">
                                        <img src="icons/tarayicilogo4.png"
                                             style="width: 60px;" alt="logo">
                                        <h4 class="mt-1 mb-2 pb-1">Kayıt Formu</h4>

                                    </div>

                                    <form id="kayitfrm" method="post" action="" >
                                        <p>Lütfen Formu doldurun</p>
                                        <p id="alert" style="color:red;"> <?php echo $alert?></p>

                                        <div class="form-outline mb-4">
                                            <input type="text" id="form2Example11" class="form-control"
                                                   placeholder="" name="nickname" required="required" />
                                            <label class="form-label" for="form2Example11">Kullanıcı adı</label>
                                        </div>

                                        <div class="form-outline mb-4">
                                            <input type="email" id="form2Example11" class="form-control"
                                                   placeholder="Eposta Adresiniz" name="emailt" required="required" />
                                            <label class="form-label" for="form2Example11">Eposta</label>
                                        </div>

                                        <div class="form-outline mb-4">
                                            <input type="password" id="form2Example22" class="form-control" name="passw" required="required" />
                                            <label class="form-label" for="form2Example22">Şifre</label>

                                        </div>

                                        <div class="text-center pt-1 mb-5 pb-1">
                                            <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-3" type="submit" form="kayitfrm">Kayıt Ol</button>

                                        </div>

                                        <div class="d-flex align-items-center justify-content-center pb-4">
                                            <p class="mb-0 me-2">Zaten bir hesabın var mı?</p>
                                            <a href="login.php" class="btn btn-outline-danger">Giriş Yap</a>
                                        </div>

                                    </form>

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