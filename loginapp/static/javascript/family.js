let familyform = document.querySelectorAll(".family-form");
let familycontainer = document.querySelector("#familyform-container");
let familyaddButton = familycontainer.querySelector("#familyadd-form");
let familyremoveButton = familycontainer.querySelector("#familyremove-form");
let familytotalForms = familycontainer.querySelector("#id_form-TOTAL_FORMS");
let familyformNum = familyform.length-1;
let familyblocker = familycontainer.querySelector('familyblocker');
let familynewForms = [];
familyaddButton.addEventListener('click', faddForm);
familyremoveButton.addEventListener('click', fremoveForm);
function faddForm(e) {
	e.preventDefault();

	let newForm = familyform[0].cloneNode(true); //Clone the bird form
	let formRegex = RegExp(`form-(\\d){1}-`,'g'); //Regex to find all instances of the form number
	
	familyformNum++ //Increment the form number
	newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${familyformNum}-`); //Update the new form to have the correct form number
	familycontainer.insertBefore(newForm, blocker); //Insert the new form at the end of the list of forms

	familytotalForms.setAttribute('value', `${familyformNum+1}`); //Increment the number of total forms in the management form
	familynewForms.push(newForm);
	fdisplayRemove();
}
function fdisplayRemove() {
if(familytotalForms.getAttribute("value") == 1) {
	familyremoveButton.style.display = "none";
} else {
	familyremoveButton.style.display = "inline";
}
}
function fremoveForm(e) {
	e.preventDefault();

	let removal = familynewForms[familynewForms.length - 1]; 
	
	familyformNum-- //Reduce the form number
 
	familytotalForms.setAttribute('value', `${familyformNum + 1}`); //Increment the number of total forms in the management form
	removal.remove();
	familynewForms.pop();
	fdisplayRemove();
}
fdisplayRemove();