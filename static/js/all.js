function check_empty()
{
    var inputs = document.getElementById("post_new");
	for (var i = 0; i < inputs.length; i++)
	{
		if (inputs.elements[i].type == "text")
		{
			if(inputs.elements[i].value == '')
			{
				return false;
			}
			else
			{
				return true;
			}
		}
	}
}