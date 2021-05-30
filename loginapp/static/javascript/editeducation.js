//VARIABLES


let educationform = document.querySelectorAll(".education-form");
let educationcontainer = document.querySelector("#educationform-container");
let educationaddButton = educationcontainer.querySelector("#educationadd-form");
let educationremoveButton = educationcontainer.querySelector("#educationremove-form");
let educationtotalForms = educationcontainer.querySelector("#id_form-TOTAL_FORMS");
let educationblocker = educationcontainer.querySelector('educationblocker');
//EVENTS
educationaddButton.addEventListener('click', function() {
     addForm(educationform,educationblocker,educationcontainer,educationtotalForms,educationremoveButton,true);
});
educationremoveButton.addEventListener('click',function() {
     removeForm(".education-form",educationtotalForms,educationremoveButton);
}); 




displayRemove(educationtotalForms,educationremoveButton)


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
		newForm.children[0].children[0].children[0].children[1].children[0].children[1].style.display = "none";
	}
	let formRegex = RegExp(`form-(\\d){1}-`,'g'); //Regex to find all instances of the form number
	let num = Number(managementform.getAttribute("value")); 
	newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${num}-`); //Update the new form to have the correct form number
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
