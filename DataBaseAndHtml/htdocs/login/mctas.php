<?php
#Link veya herhangi bir hata veya bilgi için oluştuurlan iki adet boş ifadeler oluşturulur
$ginf="";
$uyari="";
#Database bağlantısı yapılır
$mysqli = new mysqli("127.0.0.1", "root", "", "webadminoruser");
if ($mysqli->connect_errno) {
    $uyari= "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
#Post edilen yeni şifre çekilir
if(@$_POST["newpass"]) {

    #link içinde yenile koduna bağlı hash kodu kullanıcı databaseindne kontrol edilir eğer ikiside bir döngüye girer
    if(isset($_GET["yenile"])) {
        $hash = $_GET["yenile"];
        $sifre = $_POST["newpass"];
        $query = $mysqli->query('SELECT  count(*) FROM kytblgileri WHERE hash ="'.$hash.'"');
        $cntrl2 = mysqli_fetch_assoc($query);

        $count2 = $cntrl2["count(*)"];

        #yeni bir hash olusturulur ve yeni şifre ile beraber hepsi databaseden update metodu ile güncellenir ve başarılı alerti gösterilir
        if($count2==1) {
            $yeniHash=bin2hex(random_bytes(8));

            $query = $mysqli->query('UPDATE kytblgileri SET password ="'.$sifre.'", hash ="'.$yeniHash.'" WHERE hash ="'.$hash.'"');

            echo '<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script><script>swal({title: "Good job!",text: "Şifre Değişimi başarıyla gerçekleşmiştir!",icon: "success",button: "Anasayfa Dönğlüyor",});</script  >';


        #Eger hash kodları aynı değil ise Geçersiz link hatası verir
        }else if($count2==0) {
            $uyari="Geçersiz Link!!!!";
            echo '<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script><script>swal({title: "Geçersiz Link!",text: "Geçersiz Link",icon: "error",button: "Anasayfa Dönülüyor",});</script  >';

        }else{
            $uyari="Geçersiz Link!!!!";
        }
    }else {
        $uyari="Geçersiz Link!!!!";
    }
}
?>
<!doctype html>
<html lang="tr">
<head>
    <meta charset="utf-8">
    <title>Şifre Değiştirme</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/sweetalert/2.1.2/sweetalert.min.js"></script>

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
<!--Şifre değiştirme alanı oluşturulur-->
<section class="h-100 gradient-form d-flex align-items-center " style="background-color: #eee;">
    <div class="container py-5 h-100 " >
        <div class="row d-flex justify-content-center align-items-baseline pt-5  h-75">
            <div class="col-lg-5 ">
                <div class="card  text-black border-top-3 " id="corner1">


                    <div class="col-lg-5 " style="width: auto;" >
                        <div class="card-body p-md-5 mx-md-4 " >

                            <div class="d-flex justify-content-center align-items-top">
                                <img src="icons/tarayicilogo4.png"
                                     style="width: 55px; height: 55px; " alt="logo" >
                                <h4 class="mt-3 mb-4 pb-1 ms-0 " style="width: auto;text-align:center;">Giriş Yaparken Sorun mu Yaşıyorsun?</h4>

                            </div>

                            <form  id="pswy" action="" method="post">
                                <p class="pt-1 mt-1 ms-1 text-muted">E-posta adresini veya kullanıcı adını gir ve hesabına yeniden girebilmen için sana bir bağlantı gönderelim.</p>
                                <p class="pt-2 mt-1 ms-1" style="color: red;"><?php echo $uyari ?></p>
                                <p class="" style="color: green;"><?php echo $ginf ?></p>

                                <div class="form-outline mb-2">
                                    <label class="form-label" for="form2Example11" >Yeni şifrenizi giriniz</label>
                                    <input type="password"  id="form2Example11" name="newpass" class="form-control form-control-lg text-center "  required="required"  autocomplete="off"
                                           placeholder="Yeni şifrenizi giriniz"  />
                                    <label class="form-label" for="form2Example22" >Tekrar giriniz</label>
                                    <input type="password"  id="form2Example22" name="newpass" class="form-control form-control-lg text-center "  required="required"  autocomplete="off"
                                           placeholder="Yeni şifrenizi giriniz"  />


                                </div>




                                <div class="text-center pt-3 mb-3 pb-1">
                                    <button class="btn btn-primary btn-block fa-lg gradient-custom-2 mb-1" type="submit" form="pswy">Değiştir</button>

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

