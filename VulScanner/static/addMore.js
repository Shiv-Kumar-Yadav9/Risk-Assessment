<script type="text/javascript">
var ct = 1;
function add_feed()
{
	ct++;
	var div1 = document.createElement('div');
	div1.id = ct;
	div1.innerHTML = document.getElementById('newlinktpl').innerHTML;
	document.getElementById('newlink').appendChild(div1);
}
</script>