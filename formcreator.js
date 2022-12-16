const countElement = document.getElementById('id_form-TOTAL_FORMS')
const intialCountElement = document.getElementById('id_form-INITIAL_FORMS')
const max = 1000;


const addNewFieldBtn  = document.getElementById("addNewFieldBtn");
const spaceforAppend  = document.getElementById("spaceforAppend");




addNewFieldBtn.addEventListener("click",addNewField)



<label for="id_form-0-Employer_name">Employer name:</label>
<input type="text" name="form-0-Employer_name" maxlength="100" id="id_form-0-Employer_name">

function addNewField(e) {
  e.preventDefault();
 const newfieldcount =  intialCountElement + countElement + 1;
  if (countElement.value < 100) {
  const EmployementTemplate = `
  <div>
      <label for="id_form-${newfieldcount}-Employer_name">Previous Company Name #${newfieldcount} :</label>
      <input type="text" name="form-${newfieldcount}-Employer_name" maxlength="100" id="id_form-${newfieldcount}-Employer_name">
  </div>
  <div class="divide two margin-down">
      <div class="df">
          <label for="id_form-${newfieldcount}-Employer_Designation">Designation :</label>
          <input type="text" name="form-${newfieldcount}-Employer_Designation" maxlength="100" id="id_form-${newfieldcount}-Employer_Designation">
      </div>
      <div>
          <label for="id_form-${newfieldcount}-Employer_join_year">Joining Year</label>
          <input type="text" name="form-${newfieldcount}-Employer_join_year" maxlength="4" id="id_form-${newfieldcount}-Employer_join_year">
      </div>
  </div>`;

const div = document.createElement('div');
div.classList = "margin-down border-top";
div.innerHTML = EmployementTemplate;
spaceforAppend.append(div)
countElement.value = newfieldcount;
}

}
