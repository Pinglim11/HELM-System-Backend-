let childform = document.querySelectorAll(".child-form");
let childcontainer = document.querySelector("#childform-container");
let childaddButton = childcontainer.querySelector("#childadd-form");
let childremoveButton = childcontainer.querySelector("#childremove-form");
let childtotalForms = childcontainer.querySelector("#id_form-TOTAL_FORMS");
let childformNum = childform.length-1;
let childblocker = childcontainer.querySelector('childblocker');
let childnewForms = [];
childaddButton.addEventListener('click', caddForm);
childremoveButton.addEventListener('click', cremoveForm);
function caddForm(e) {
	e.preventDefault();

	let newForm = childform[0].cloneNode(true); //Clone the bird form
	let formRegex = RegExp(`form-(\\d){1}-`,'g'); //Regex to find all instances of the form number
	
	childformNum++ //Increment the form number
	newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${childformNum}-`); //Update the new form to have the correct form number
	childcontainer.insertBefore(newForm, childblocker); //Insert the new form at the end of the list of forms

	childtotalForms.setAttribute('value', `${childformNum+1}`); //Increment the number of total forms in the management form
	childnewForms.push(newForm);
	cdisplayRemove();
}
function cdisplayRemove() {
if(childtotalForms.getAttribute("value") == 1) {
	childremoveButton.style.display = "none";
} else {
	childremoveButton.style.display = "inline";
}
}
function cremoveForm(e) {
	e.preventDefault();

	let removal = childnewForms[childnewForms.length - 1]; 
	
	childformNum-- //Reduce the form number
 
	childtotalForms.setAttribute('value', `${childformNum + 1}`); //Increment the number of total forms in the management form
	removal.remove();
	childnewForms.pop();
	cdisplayRemove();
}
cdisplayRemove();