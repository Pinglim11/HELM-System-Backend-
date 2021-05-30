//VARIABLES
let emphisform = document.querySelectorAll(".emphis-form");
let container = document.querySelector("#emphisform-container");
let addButton = container.querySelector("#emphisadd-form");
let removeButton = container.querySelector("#emphisremove-form");
let totalForms = container.querySelector("#4_form-TOTAL_FORMS");
let blocker = container.querySelector('emphisblocker');

let familyform = document.querySelectorAll(".family-form");
let familycontainer = document.querySelector("#familyform-container");
let familyaddButton = familycontainer.querySelector("#familyadd-form");
let familyremoveButton = familycontainer.querySelector("#familyremove-form");
let familytotalForms = familycontainer.querySelector("#6_form-TOTAL_FORMS");
let familyblocker = familycontainer.querySelector('familyblocker');

let educationform = document.querySelectorAll(".education-form");
let educationcontainer = document.querySelector("#educationform-container");
let educationaddButton = educationcontainer.querySelector("#educationadd-form");
let educationremoveButton = educationcontainer.querySelector("#educationremove-form");
let educationtotalForms = educationcontainer.querySelector("#5_form-TOTAL_FORMS");
let educationblocker = educationcontainer.querySelector('educationblocker');

let childform = document.querySelectorAll(".child-form");
let childcontainer = document.querySelector("#childform-container");
let childaddButton = childcontainer.querySelector("#childadd-form");
let childremoveButton = childcontainer.querySelector("#childremove-form");
let childtotalForms = childcontainer.querySelector("#8_form-TOTAL_FORMS");
let childblocker = childcontainer.querySelector('childblocker');
//EVENTS
addButton.addEventListener('click', function() {
     addForm(emphisform,blocker,container,totalForms,removeButton);
});
removeButton.addEventListener('click',function() {
     removeForm(".emphis-form",totalForms,removeButton);
}); 

familyaddButton.addEventListener('click', function() {
     addForm(familyform,familyblocker,familycontainer,familytotalForms,familyremoveButton);
});
familyremoveButton.addEventListener('click',function() {
     removeForm(".family-form",familytotalForms,familyremoveButton);
}); 

educationaddButton.addEventListener('click', function() {
     addForm(educationform,educationblocker,educationcontainer,educationtotalForms,educationremoveButton);
});
educationremoveButton.addEventListener('click',function() {
     removeForm(".education-form",educationtotalForms,educationremoveButton);
}); 

childaddButton.addEventListener('click', function() {
     addForm(childform,childblocker,childcontainer,childtotalForms,childremoveButton);
});
childremoveButton.addEventListener('click',function() {
     removeForm(".child-form",childtotalForms,childremoveButton);
}); 

displayRemove(totalForms,removeButton)
displayRemove(familytotalForms,familyremoveButton)
displayRemove(educationtotalForms,educationremoveButton)
displayRemove(childtotalForms,childremoveButton)
//FUNCTIONS
function addForm(allforms,block,contain,managementform,remove,check) {
	let newForm = allforms[0].cloneNode(true); //Clone the bird form
	if (check == true){
		newForm.childNodes[1].style.display = "none";
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
