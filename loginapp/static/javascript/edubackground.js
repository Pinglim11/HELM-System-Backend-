let educationform = document.querySelectorAll(".education-form");
let educationcontainer = document.querySelector("#educationform-container");
let educationaddButton = educationcontainer.querySelector("#educationadd-form");
let educationremoveButton = educationcontainer.querySelector("#educationremove-form");
let educationtotalForms = educationcontainer.querySelector("#id_form-TOTAL_FORMS");
let educationformNum = educationform.length-1;
let educationblocker = educationcontainer.querySelector('educationblocker');
let educationnewForms = [];
educationaddButton.addEventListener('click', eaddForm);
educationremoveButton.addEventListener('click', eremoveForm);
function eaddForm(e) {
	e.preventDefault();

	let newForm = educationform[0].cloneNode(true); //Clone the bird form
	let formRegex = RegExp(`form-(\\d){1}-`,'g'); //Regex to find all instances of the form number
	
	educationformNum++ //Increment the form number
	newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${educationformNum}-`); //Update the new form to have the correct form number
	educationcontainer.insertBefore(newForm, educationblocker); //Insert the new form at the end of the list of forms

	educationtotalForms.setAttribute('value', `${educationformNum+1}`); //Increment the number of total forms in the management form
	educationnewForms.push(newForm);
	edisplayRemove();
}
function edisplayRemove() {
if(educationtotalForms.getAttribute("value") == 1) {
	educationremoveButton.style.display = "none";
} else {
	educationremoveButton.style.display = "inline";
}
}
function eremoveForm(e) {
	e.preventDefault();

	let removal = educationnewForms[educationnewForms.length - 1]; 
	
	educationformNum-- //Reduce the form number
 
	educationtotalForms.setAttribute('value', `${educationformNum + 1}`); //Increment the number of total forms in the management form
	removal.remove();
	educationnewForms.pop();
	edisplayRemove();
}
edisplayRemove();