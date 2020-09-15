
let theme = localStorage.getItem('theme')
if(theme==null){
	setTheme('light')
}
else{
	setTheme(theme)
}



let themeDots = document.getElementsByClassName('theme-dot')

for(var i=0; i<themeDots.length; i++){
	
	themeDots[i].addEventListener('click',function()
	{
		let mode = this.dataset.mode
		console.log("optionClicked",mode);
		setTheme(mode)
	})
 
}
function setTheme(mode){
	if(mode=='light')
		document.getElementById('theme-style').href= static + '/default.css'
	if(mode=='green')
		document.getElementById('theme-style').href= static + '/green.css'
	if(mode=='orange')
		document.getElementById('theme-style').href= static + '/orange.css'
	if(mode=='blue')
		document.getElementById('theme-style').href= static + '/blue.css'

	localStorage.setItem('theme',mode)
}