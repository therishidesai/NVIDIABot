<html>
<form name="input" action="gitpull.php" method="get">
<input type="submit" value="Upload Code">
</form>
<?php
if($_SESSION['success']==1){
	echo "success";
	$_SESSION['success']=0;
}
?>
</html>
