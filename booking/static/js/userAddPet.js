document.addEventListener('DOMContentLoaded', function () {
  var select = document.querySelectorAll('select');
  var selectInstance = M.FormSelect.init(select, {});
});

const btnAddPet = document.getElementById('addPet');
const petTemplate = document.getElementById('petRowTemplate');
const petFormContainer = document.querySelector('#addPetForm .modal-content');

btnAddPet.addEventListener('click', (e) => {
  e.preventDefault();

  const elem = document.getElementById('petModal');
  const modal = M.Modal.init(elem);
  const newRowNum = petCount + 1;

  const currNode = petFormContainer.querySelector('.pet-row');

  if (!currNode) {

    const newNode = petTemplate.content.cloneNode(true);
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
    });

    petFormContainer.appendChild(newNode);
  }

  setTimeout(() =>{
    M.AutoInit();
    modal.open();
  }, 0);

})