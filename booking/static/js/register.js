
document.addEventListener('DOMContentLoaded', function () {
  var select = document.querySelectorAll('select');
  var selectInstance = M.FormSelect.init(select, {});

  var datePicker = document.querySelectorAll('.datepicker');
  var datePickerInstance = M.Datepicker.init(datePicker, {});
});

const petTemplate = document.getElementById('petRowTemplate');
const petContainer = document.getElementById('petContainer');
const addAnotherPetBtn = document.getElementById('addPetBtn');

addAnotherPetBtn.addEventListener('click', (e) => {
  const allListPets = petContainer.querySelectorAll('.pet-row');
  const lastPetRow = allListPets[allListPets.length - 1];
  const countRow = parseFloat(lastPetRow.getAttribute('data-pet-row'));
  const newRowNum = countRow + 1;

  const newNode = petTemplate.content.cloneNode(true);

  // update row number to keep track
  newNode.querySelector('.pet-row').setAttribute('data-pet-row', newRowNum);
  const allInputs = newNode.querySelectorAll('.card-content .input-field');

  allInputs.forEach((item) => {
    const input = item.querySelector('input');
    const label = item.querySelector('label');
    const selectPet = item.querySelector('select');

    if (input && label) {

      if (item.classList.contains('input-name')) {
        const fieldName = `pet.${newRowNum}.nombreMascota`;
        input.setAttribute('id', fieldName);
        input.setAttribute('data-pet-row', newRowNum);
        input.setAttribute('name', fieldName);
        label.setAttribute('for', fieldName);
      } else if (item.classList.contains('input-age')) {
        const fieldName = `pet.${newRowNum}.edadMascota`;
        input.setAttribute('id', fieldName);
        input.setAttribute('name', fieldName);
        label.setAttribute('for', fieldName);
      } else {
        const fieldName = `pet.${newRowNum}.generoMascota`;
        input.setAttribute('id', fieldName);
        input.setAttribute('name', fieldName);
        label.setAttribute('for', fieldName);
      }
    }

    if (selectPet) {
      if (selectPet.classList.contains('species')) {
        const fieldName = `pet.${newRowNum}.especieMascota`;
        selectPet.setAttribute('name', fieldName);
      } else {
        const fieldName = `pet.${newRowNum}.razaMascota`;
        selectPet.setAttribute('name', fieldName);
      }

    }
    setTimeout(() => M.AutoInit(), 0);

  });

  petContainer.appendChild(newNode);

});