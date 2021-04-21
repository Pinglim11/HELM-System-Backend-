let emphisform = document.querySelectorAll(".emphis-form");
let container = document.querySelector("#emphisform-container");
let addButton = container.querySelector("#emphisadd-form");
let removeButton = container.querySelector("#emphisremove-form");
let totalForms = container.querySelector("#id_form-TOTAL_FORMS");
let formNum = emphisform.length-1;
let blocker = container.querySelector('emphisblocker');
let newForms = [];
addButton.addEventListener('click', addForm);
removeButton.addEventListener('click', removeForm);
function addForm(e) {
	e.preventDefault();

	let newForm = emphisform[0].cloneNode(true); //Clone the bird form
	let formRegex = RegExp(`form-(\\d){1}-`,'g'); //Regex to find all instances of the form number
	
	formNum++ //Increment the form number
	newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`); //Update the new form to have the correct form number
	container.insertBefore(newForm, blocker); //Insert the new form at the end of the list of forms

	totalForms.setAttribute('value', `${formNum+1}`); //Increment the number of total forms in the management form
	newForms.push(newForm);
	displayRemove();
}
function displayRemove() {
if(totalForms.getAttribute("value") == 1) {
	removeButton.style.display = "none";
} else {
	removeButton.style.display = "inline";
}
}
function removeForm(e) {
	e.preventDefault();

	let removal = newForms[newForms.length - 1]; 
	
	formNum-- //Reduce the form number
 
	totalForms.setAttribute('value', `${formNum + 1}`); //Increment the number of total forms in the management form
	removal.remove();
	newForms.pop();
	displayRemove();
}
displayRemove();