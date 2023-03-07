<?php
#geçmişe girileceği zaman bu kodlar çalışır
#Öncelikle vei tabanı bağlantısı yapılır ve 30 GÜN önceki verileri silerek başlar
$mysqli = new mysqli("127.0.0.1", "root", "", "web");
if ($mysqli->connect_errno) {
    echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}
$exec = $mysqli->query("DELETE FROM history WHERE HTarih <=  DATE_SUB(NOW(), INTERVAL 30 DAY) ");

#Tarihin formatlayıp çağrıldıgında ingilizce yerine türkçe karşılığı gelmesi için eklenen replace metodu
$mysqli->set_charset("utf8");
$ingilizce = array(
	'January',
	'February',
	'March',
	'April',
	'May',
	'Jun',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December',
	'Monday',
	'Tuesday',
	'Wednesday',
	'Thursday',
	'Friday',
	'Saturday',
	'Sunday'
);

$turkce = array(
	'Ocak',
	'Şubat',
	'Mart',
	'Nisan',
	'Mayıs',
	'Haziran',
	'Temmuz',
	'Ağustos',
	'Eylül',
	'Ekim',
	'Kasım',
	'Aralık',
	'Pazartesi',
    'Salı',
    'Çarşamba',
    'Perşembe',
    'Cuma',
    'Cumartesi',
    'Pazar'

);
$tarih = str_replace($ingilizce,$turkce,date('d F Y l'));
$tarihy= str_replace($ingilizce,$turkce,date('d F Y l',strtotime("-1 days")));
$date3=date('Y-m-d',strtotime("-1 days"));
$date4=date('Y-m-d',strtotime("-30 days"));

$exec3 = $mysqli->query("select Count(*) from history where HTarih BETWEEN '$date4'and'$date3'  ");
$data3=mysqli_fetch_assoc($exec3);
$count3 = $data3["Count(*)"];




?>
<!doctype html>
<html lang="tr" >
<head>
<meta charset="utf-8">
<title>Geçmiş</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<style>

body{
background-color:#eee;

}
.head{
position:fixed;

height:50px;
width:200px;
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
    background-image: url('icons/tarayicilogo4.png');
    background-position:center;
    border-color:red;
    background-repeat: no-repeat;
    background-attachment: inherit;
    background-size: 30px;
    background-color: transparent;
}
<?php
    #yüksekliğini belirlemek için tarih olanlrın count sayısının düzenlenmiş hali yükseklik olarak eklenir
    $date=date('Y-m-d');

    $exec = $mysqli->query("SELECT Count(*) FROM history WHERE HTarih LIKE '$date%' ");
    $data=mysqli_fetch_assoc($exec);
    $count = $data["Count(*)"];

    $mctheigt= ($count*50)+75;

?>
.mct{


    box-shadow: 0px -1px 2px 2px #444444;
    position: relative;
    width: 1017px;
    height:<?php echo $mctheigt ?>px;



    overflow-y:visible;

    border:1px solid;

    border-radius:15px;
    color:black;
    background-color: #eee;
    border-color: #eee  ;
}


.maindiv{
    position: relative;
    width: 1000px;
    height:50px;
    background-color: transparent;
}
.chckbtn{
    position: relative;
    width: 20px;
    height:20px;
    top:15px;
    left:15px;
    border: 2px solid red;
    border-radius:15px;

}


.mtime{
    position: relative;
    text-align:center;
    width: 150px;
    height:50px;
    top:10px;
    left:25px;
    background-color: #eee;
    color:black;
    text-decoration:none;
}
.mtime:hover{
color:black;
}

.mdata{
    position: relative;
    float:right;
    width: 660px;
    height:50px;
    padding-top:12px;

    background-color: transparent;
    text-align:left;
    text-decoration:none;
    color:black;
}
.mdata:hover{
//color:bisque;
}
.deltebtn{
    position: relative;
    top:5px;
    left:-150px;
    width: 90px;
    height: 35px;
    text-align:center;



}
.alldeltebtn{
    position: relative;
    top:70px;
    left:110px;
    width: 20px;
    height: 20px;
    text-align:center;
    color:white;
    display:none;


}
.headertoday{

    position: relative;
    width: 1017px;
    height:52px;


}
<?php
#Yine bu sefer dün için oluşuturlan kısmın yüksekliği hesaplanıp eklenir
    $date2=date('Y-m-d',strtotime("-1 days"));

    $exec2 = $mysqli->query("SELECT Count(*) FROM history WHERE HTarih LIKE '$date2%' ");
    $data2=mysqli_fetch_assoc($exec2);
    $count2 = $data2["Count(*)"];

    $mctheigt2= ($count2*50)+75;
    $mctheigt3= ($count3*50)+75;

?>

.mct2{


    box-shadow: 0px -1px 2px 2px #444444;
    position: relative;
    width: 1017px;
    height:<?php echo $mctheigt2 ?>px;
    top:50px;
    margin-bottom:100px;


    overflow-y:visible;

    border:1px solid;

    border-radius:15px;
    color:black;
    background-color: #eee;
    border-color: #eee ;
}


.maindiv2{
    position: relative;
    width: 1000px;
    height:50px;
    background-color: transparent;
}
.chckbtn2{
    position: relative;
    width: 20px;
    height:20px;
    top:15px;
    left:15px;
    border: 2px solid red;
    border-radius:15px;

}


.mtime2{
    position: relative;
    text-align:center;
    width: 150px;
    height:50px;
    top:10px;
    left:25px;
    background-color: #eee;
    color:black;
    text-decoration:none;
}
.mtime2:hover{
color:black;
}

.mdata2{
    position: relative;
    float:right;
    width: 660px;
    height:50px;
    padding-top:12px;

    background-color: transparent;
    text-align:left;
    text-decoration:none;
    color:black;
}
.mdata2:hover{
color:#b44593;
}

.headertoday2{

    position: relative;
    width: 1017px;
    height:52px;


}




.mct3{

    box-shadow: 0px -1px 2px 2px #444444;
    position: relative;
    width: 1017px;
    height: <?php echo $mctheigt3 ?>px;
    top:20px;


    overflow-y:visible;
    border:1px solid;

    border-radius:15px;
    color:black;
    background-color: #eee;
    border-color: #eee ;
}


.maindiv3{
    position: relative;
    width: 1000px;
    height:50px;
    background-color: transparent;
}
.chckbtn3{
    position: relative;
    width: 20px;
    height:20px;
    top:15px;
    left:15px;
    border: 2px solid red;
    border-radius:15px;

}


.mtime3{
    position: relative;
    text-align:center;
    width: 150px;
    height:50px;
    top:10px;
    left:25px;
    background-color: #eee;
    color:black;
    text-decoration:none;
}
.mtime3:hover{
color:black;
}

.mdata3{
    position: relative;
    float:right;
    width: 660px;
    height:50px;
    padding-top:12px;

    background-color: transparent;
    text-align:left;
    text-decoration:none;
    color:black;
}
.mdata3:hover{
color:;
}

.headertoday3{

    position: relative;
    width: 1017px;
    height:52px;


}

.mct4{

    position: relative;
    width: 1017px;
    height:<?php echo $mctheigt2+$mctheigt+$mctheigt3 ?>px;
    margin-bottom:200px;
     top:70px;
    left:250px;

    overflow-y:visible;

    border:1px solid;
    border-color: transparent;

    border-radius:15px;
    color:white;
    background-color: transparent;

}
.lbltmnsc{
    position: relative;
    top:65px;
    left:250px;
    width: 145px;
    height: 35px;
    display: inline-block;
    text-align:center;
    color:black;

}
.countsil{
    position: fixed;
    top:0px;
    left:0px;
    width: 100%;
    height: 50px;
    background: rgba(255, 255, 255, 0.87);
    z-index: 2;
    border:1px solid #E8EAF6;
    border-radius:5px;
    display: none;
    text-align:center;
    color:blue;


}
.closeslct{
    position: fixed;
    float:left;
    top:10px;
    left:300px;
    width: 20px;
    height: 20px;

    display: inline-block;
    text-align:center;



}


</style>
<body>
<!--İcon ve geçmiş yazısının bulundugu alan -->
<a href="data.php">
<div class="head fw-bold " >Geçmiş
<div class="icon"></div>

</div>
</a>
<!--Silme div tasarımı bulunduğu kısım -->
<div>
<button class="lbltmnsc btn btn-outline-dark"  onclick="control()" > Tümünü Seç</button>
<input type="checkbox" class="alldeltebtn  " id="chc" onclick="selects()"  >
</div>
    <div class="countsil" id="div2">
        <button class="closeslct  btn-close" aria-label="Close" style="float:right;" name="submit" type="submit" onclick="clsoedivbtn()" ></button>
        <label for="html" id="ss" style="color white;float:left;padding-left:350px;padding-top:12px;"></label>
        <button class="deltebtn  btn btn-outline-primary" style="float:right;" name="submit" type="submit" form="myForm" >Sil</button>
    </div>
<!-- Seçili ckeckboxların post edileceği form ve gönderileceği php dosyası-->
    <form action="checkbox-form.php" method="post" id="myForm">

        <!-- Genel bugun,dün ve öncesini içine alan mct4 divi-->
<div class="mct4 vertical-menu">
    <!--Sadece bugunu kapsayan div -->
    <div class="mct vertical-menu">
                <div class="headertoday fw-bold" style="text-align:left;padding-left:50px;padding-top:12px;border:1px solid;
    border-top-left-radius:15px;
    border-top-right-radius:15px;
    border-color: #eee #eee black  #eee;">Bugün - <?php echo $tarih; ?> </div>
<?php
#Tarih çekilir ve sorgu yapılır bugunuın tarihi olanlar çekilir ve while döngüsü ile eklnemeye başlar
    $date=date('Y-m-d');

    $sorgu = $mysqli->query("SELECT * FROM history WHERE HTarih LIKE '$date%' ORDER BY HTarih DESC");
    while ($hcek=mysqli_fetch_assoc($sorgu)){

    ?>
                <a href="#" >
                        <div class="maindiv">

                    <input class="chckbtn"  type="checkbox" id="<?php echo  $hcek['Id'] ?>" name="ossm[]"  value="<?php echo  $hcek['Id'] ?>" onclick="checkTotalCheckedBoxes()">
                    <a class="mtime" ><?php echo $hcek['HTarih'] ?> </a>
                    <a class="mdata"  href="<?php echo $hcek['HPage'] ?>"><?php echo $hcek['HPage'] ?></a>

                </div>
            </a>

<?php }
?>
</div>
    <!--Sadece dünü kapsayan div -->
<div class="mct2 vertical-menu">
                <div class="headertoday2 fw-bold" style="text-align:left;padding-left:50px;padding-top:12px;border:1px solid;
    border-top-left-radius:15px;
    border-top-right-radius:15px;
    border-color: #eee #eee black  #eee;">Dün - <?php echo $tarihy; ?> </div>
<?php
    $date=date('Y-m-d',strtotime("-1 days"));

    $sorgu = $mysqli->query("SELECT * FROM history WHERE HTarih LIKE '$date%' ORDER BY HTarih DESC");
    while ($hcek=mysqli_fetch_assoc($sorgu)){

    ?>
                <a href="#" >
                        <div class="maindiv2">

                    <input class="chckbtn2"  type="checkbox" id="<?php echo  $hcek['Id'] ?>" name="ossm[]"  value="<?php echo  $hcek['Id'] ?>" onclick="checkTotalCheckedBoxes()">
                    <a class="mtime2" ><?php echo $hcek['HTarih'] ?> </a>
                    <a class="mdata2"  href="<?php echo $hcek['HPage'] ?>"><?php echo $hcek['HPage'] ?></a>

                </div>
            </a>

<?php }
?>

</div>
    <!--Sadece dün ve bügun hariç hepsini kapsayan div -->
    <div class="mct3 vertical-menu">
        <div class="headertoday3 fw-bold" style="text-align:left;padding-left:50px;padding-top:12px;border:1px solid;
    border-top-left-radius:15px;
    border-top-right-radius:15px;
    border-color: #eee #eee black  #eee;">Dün - <?php echo $tarihy; ?> </div>
        <?php
        $date=date('Y-m-d',strtotime("-1 days"));

        $sorgu4 = $mysqli->query("select * from history where HTarih BETWEEN '$date4'and'$date3' ORDER by HTarih DESC ");
        while ($hcek=mysqli_fetch_assoc($sorgu4)){

            ?>
            <a href="#" >
                <div class="maindiv3">

                    <input class="chckbtn3"  type="checkbox" id="<?php echo  $hcek['Id'] ?>" name="ossm[]"  value="<?php echo  $hcek['Id'] ?>" onclick="checkTotalCheckedBoxes()">
                    <a class="mtime3" ><?php echo $hcek['HTarih'] ?> </a>
                    <a class="mdata3"  href="<?php echo $hcek['HPage'] ?>"><?php echo $hcek['HPage'] ?></a>

                </div>
            </a>

        <?php }
        ?>

</div>
</form>


<script type="text/javascript">
    <!--Tümünü şeç butonuna tıklnadıgında bütün checkbox kutularını dönerek hepsini chechked yapar hepsi seçili iken tam tersini yapar -->
    function control(){
    if (document.getElementById('chc').checked)
  {
      document.getElementById('chc').checked=false;
      var ele=document.getElementsByName('ossm[]');
                for(var i=0; i<ele.length; i++){
                    if(ele[i].type=='checkbox')
                        ele[i].checked=false;
                }

  }
  else {
      document.getElementById('chc').checked=true;
      var ele=document.getElementsByName('ossm[]');
                for(var i=0; i<ele.length; i++){
                    if(ele[i].type=='checkbox')
                        ele[i].checked=true;
                }


  }
  <!--Seçili checkbox kutusunuın ysayını ögrenmek için bu scripte yönlendirilir-->
  checkTotalCheckedBoxes();
}
</script>
<script language="JavaScript">
    <!--Seçili olanları -->
function selects(){
if (document.getElementById('chc').checked)
  {
      var ele=document.getElementsByName('ossm[]');
                for(var i=0; i<ele.length; i++){
                    if(ele[i].type=='checkbox')
                        ele[i].checked=true;
                }

  }
  else {
      var ele=document.getElementsByName('ossm[]');
                for(var i=0; i<ele.length; i++){
                    if(ele[i].type=='checkbox')
                        ele[i].checked=false;
                }


  }
}


</script>
<script>
    <!--şecili olan checkbox butonların sayısı hesaplanır -->
function checkTotalCheckedBoxes()
{
     var checkLength = 0;
     var boxes = document.getElementsByName("ossm[]");

     for (var i = 0; i < boxes.length; i++)
     {
         boxes[i].checked ? checkLength++ : null;
     }

     document.getElementById('ss').innerText = checkLength+'x';
     if (checkLength==0){

        document.getElementById('div2').style.display = 'none';
     }
     else{
        document.getElementById('div2').style.display = 'block';
     }
}

</script>
<script>
    <!--silme divin görününmü kapatmak için olusturulan script -->
function clsoedivbtn()
{
        document.getElementById('div2').style.display = 'none';
        var ele=document.getElementsByName('ossm[]');
                for(var i=0; i<ele.length; i++){
                    if(ele[i].type=='checkbox')
                        ele[i].checked=false;
     }

}

</script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js" integrity="sha384-7+zCNj/IqJ95wo16oMtfsKbZ9ccEh31eOz1HGyDuCQ6wgnyJNSYdrPa03rtR1zdB" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js" integrity="sha384-QJHtvGhmr9XOIpI6YVutG+2QOK9T+ZnN4kzFN1RtK3zEFEIsxhlmWl5/YESvpZ13" crossorigin="anonymous"></script>
</body>
</body>
</html>

