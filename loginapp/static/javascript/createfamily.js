//VARIABLES


let familyform = document.querySelectorAll(".family-form");
let familycontainer = document.querySelector("#familyform-container");
let familyaddButton = familycontainer.querySelector("#familyadd-form");
let familyremoveButton = familycontainer.querySelector("#familyremove-form");
let familytotalForms = familycontainer.querySelector("#id_6-TOTAL_FORMS");
let familyblocker = familycontainer.querySelector('familyblocker');
//EVENTS
familyaddButton.addEventListener('click', function() {
     addForm(familyform,familyblocker,familycontainer,familytotalForms,familyremoveButton);
});
familyremoveButton.addEventListener('click',function() {
     removeForm(".family-form",familytotalForms,familyremoveButton);
}); 



displayRemove(familytotalForms,familyremoveButton)

//FUNCTIONS
function addForm(allforms,block,contain,managementform,remove,check) {
	let newForm = allforms[0].cloneNode(true); //Clone the bird form
	let inputs = newForm.getElementsByTagName('input');
	let selects = newForm.getElementsByTagName('select');
	let tempind = 0;

	while (tempind < inputs.length){
		inputs[tempind].setAttribute('value','');
		tempind +=1;
		
	}
	tempind = 0;
	
	
	while (tempind < selects.length){
		selects[tempind].selectedIndex = 0;
		tempind +=1;
		
	}
	
	
	
	if (check == true){
		newForm.childNodes[1].style.display = "none";
	}
	let formRegex = RegExp(`id_6-(\\d){1}-`,'g'); //Regex to find all instances of the form number
	let num = Number(managementform.getAttribute("value")); 
	newForm.innerHTML = newForm.innerHTML.replace(formRegex, `id_6-${num}-`); //Update the new form to have the correct form number
	newForm.innerHTML = newForm.innerHTML.replace(RegExp(`6-(\\d){1}-`,'g'), `6-${num}-`); //Update the new form to have the correct form number
	contain.insertBefore(newForm, block); //Insert the new form at the end of the list of forms

	managementform.setAttribute('value', `${num+1}`); //Increment the number of total forms in the management form
	displayRemove(managementform,remove);
}
function displayRemove(manageform,remove) {
if(manageform.getAttribute("value") == 1) {
	remove.style.display = "none";
} else {
	remove.style.display = "inline";
}
}
function removeForm(formtext,managementform,remove) {
	let allforms = document.querySelectorAll(formtext);
	let removal = allforms[allforms.length - 1]; 
	let num = Number(managementform.getAttribute("value"));

 
	managementform.setAttribute('value', `${num - 1}`); //Increment the number of total forms in the management form
	removal.remove();
	displayRemove(managementform,remove);
}
